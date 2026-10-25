import os
import certifi
from dotenv import load_dotenv
load_dotenv()

os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

from typing import TypedDict, Annotated
import operator
import uuid
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import(
    AnyMessage,
    HumanMessage,
    AIMessage,
    SystemMessage,
)
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from langchain_groq import ChatGroq

from tools.flight_tool import search_flights
from tools.travily_tool import tavily_search

#====================================
# load API key
#====================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing .  please add it to your .env file.")

#====================================
# llm
#====================================
llm = ChatGroq(
   #model="meta-llama/llama-prompt-guard-2-22m",
    model="openai/gpt-oss-120b",
   api_key=GROQ_API_KEY,
   temperature=0
)
#response = llm.invoke("hello how are your")
#print(response.content)
#====================================
# state
#====================================
class TravelState(TypedDict):
    messages : Annotated[list[AnyMessage], operator.add]
    user_query: str
    flight_results: str
    hotel_results: str
    itinerary : str
    llm_calls: int

#====================================
# flight agent
#====================================
def flight_agent(state: TravelState):
    query = state["user_query"]
    flight_data = search_flights(query)

    return{
        "flight_results" : flight_data,
        "messages" : [
            AIMessage(content="Flight result fetched.")
        ],
        "llm_calls": state.get("llm_calls", 0)+1
    }

# #====================================
# Hotel Agent
#====================================
def hotel_agent(state : TravelState):
    query = f"Best hotels for {state['user_query']}"
    hotel_results = tavily_search(query)

    return{
        "hotel_results":hotel_results,
        "message": [
            AIMessage(content="Hotel information fetched. ")

        ],
        "llm_calls": state.get("llm_calls",0)+1
    }
# #====================================
# Itinerary Agent
#====================================
def itinerary_agent(state: TravelState):
    prompt = f"""
Create a complete travel itinerary.

User Query:
{state['flight_results']}

Hotel Results:
{state['hotel_results']}

Make the itinerary practical, budget-aware, and easy to follow.



"""
    response = llm.invoke([
        SystemMessage(content="You are expert travel planner. "),
        HumanMessage(content=prompt)
    ])

    return{
        "itinerary" : response.content,
        "messages" : [response],
        "llm_calls" : state.get("llm_calls", 0) +1
    }
    
    
    # #====================================
# final Response Agent
#====================================
def final_agent(state: TravelState):
    final_prompt=f"""
Generate the final travel response for the user.

User Request:
{state['user_query']}

Flights:
{state['flight_results']}

Hotels:
{state['hotel_results']}

Itinerary:
{state['itinerary']}

Format the final answer beautifully using these sections:

1. Trip Summary
2. Flight Information
3. Hotel Suggestions
4. Day-by-Day Itinerary
5. Estimated Buget
6. Final Recommendations

Important:
- Be clear and practical
- Mention that live flight API may not provide ticket price if pricing is unabilable.
- Keep the response useful for real travel planning.

"""
    response = llm.invoke([
        SystemMessage(content="Your are a professional AI Travel booking assistant."),
        HumanMessage(content=final_prompt)
    ])  

    return{
        "messages" : [response],
        "llm_calls":state.get("llm_calls", 0)+1
    }
# checkpointer
connect = sqlite3.connect(database='travel.db', check_same_thread=False)
checkpoint = SqliteSaver(connect)

# #====================================
# Build Graph
#====================================

graph = StateGraph(TravelState)

graph.add_node("flight_agent", flight_agent)
graph.add_node("hotel_agent", hotel_agent)
graph.add_node("itinerary_agent",itinerary_agent)
graph.add_node("final-agent",final_agent)

graph.add_edge(START,"flight_agent")
graph.add_edge("flight_agent","hotel_agent")
graph.add_edge("hotel_agent","itinerary_agent")
graph.add_edge("itinerary_agent", "final_agen")
graph.add_edge("final_agent", END)

travel_graph = graph.compile(checkpointer=checkpoint)