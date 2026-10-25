
import os
import requests
from dotenv import load_dotenv

load_dotenv()

AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

def search_flights(query):
    """Search for flights using a flight number or airport IATA code."""

    if not AVIATIONSTACK_API_KEY:
        raise ValueError(
            "AVIATIONSTACK_API_KEY is missing from your .env file."
        )

    url = "https://api.aviationstack.com/v1/flights"

    query = query.strip().upper()

    # Choose a filter based on the query
    params = {"access_key": AVIATIONSTACK_API_KEY}

    if not query:
        raise ValueError("Please provide a flight number or airport code.")

    if query.isalpha() and len(query) == 3:
        params["dep_iata"] = query
    else:
        params["flight_iata"] = query

    try:
        response = requests.get(
            url,
            params=params,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return {"error": data["error"]}

        flights = []

        for flight in data.get("data", []):
            flights.append({
                "airline": flight.get("airline", {}).get("name"),
                "flight_number": flight.get("flight", {}).get("iata"),
                "status": flight.get("flight_status"),
                "departure_airport": flight.get("departure", {}).get("airport"),
                "departure_iata": flight.get("departure", {}).get("iata"),
                "departure_time": flight.get("departure", {}).get("scheduled"),
                "arrival_airport": flight.get("arrival", {}).get("airport"),
                "arrival_iata": flight.get("arrival", {}).get("iata"),
                "arrival_time": flight.get("arrival", {}).get("scheduled"),
            })

        return flights

    except requests.RequestException as error:
        return {"error": f"Flight API request failed: {error}"}


'''if __name__== "__main__":
    print(search_flights("plan a 7 days japan trip from banladesh"))
    print("end")'''



results = search_flights("japan")
print()
print(results)
