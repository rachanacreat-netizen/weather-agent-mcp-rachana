from weather_tool import get_weather

print("Weather Agent Started")
print("Type 'exit' to quit\n")

while True:

    query = input("Ask the agent: ").lower()

    if query == "exit":
        print("Agent shutting down...")
        break

    if "weather" in query:

        # Extract city
        words = query.replace("?", "").split()
        city = words[-1]

        print("\nAgent: Fetching weather information...\n")

        weather = get_weather(city)

        if weather:
            print(f"Weather in {city.title()}")
            print(f"Temperature: {weather['temperature']}")
            print(f"Condition: {weather['forecast']}\n")
        else:
            print("Weather service unavailable.\n")

    else:
        print("Sorry, I can only answer weather related queries.\n")