
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def travily_search(query: str) -> str:
    """Perform an internet search using Tavily."""

    if not query or not query.strip():
        return "Please enter a search query."

    try:
        response = client.search(
            query=query,
            search_depth="fast",
            max_results=5
        )

        results = response.get("results", [])

        if not results:
            return "No search results found."

        return "\n\n".join(
            f"Title: {item.get('title', '')}\n"
            f"URL: {item.get('url', '')}\n"
            f"Content: {item.get('content', '')}"
            for item in results
        )

    except Exception as e:
        return f"Internet search failed: {e}"


result = travily_search("Best hotels in New York")
print(result)