import requests


def get_user_info():
    """Fetch user info based on user input."""
    print("=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ")

    # Exercise 3: Input validation
    if not user_id.isdigit():
        print("❌ Invalid input! Please enter a number.")
        return

    user_id = int(user_id)

    if user_id < 1 or user_id > 10:
        print("❌ User ID must be between 1 and 10.")
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\nUser with ID {user_id} not found!")


def search_posts():
    """Search posts by user ID."""
    print("\n=== Post Search ===\n")

    user_id = input("Enter user ID to see their posts (1-10): ")

    # Exercise 3: Input validation
    if not user_id.isdigit():
        print("❌ Invalid input! Please enter a number.")
        return

    user_id = int(user_id)

    if user_id < 1 or user_id > 10:
        print("❌ User ID must be between 1 and 10.")
        return

    # Using query parameters
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        posts = response.json()

        if posts:
            print(f"\n--- Posts by User #{user_id} ---")
            for i, post in enumerate(posts, 1):
                print(f"{i}. {post['title']}")
        else:
            print("No posts found for this user.")
    else:
        print("❌ Failed to fetch posts.")


def get_crypto_price():
    """Fetch cryptocurrency price based on user input."""
    print("\n=== Cryptocurrency Price Checker ===\n")

    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")
    coin_id = input("Enter coin ID (e.g., btc-bitcoin): ").lower().strip()

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_usd = data['quotes']['USD']['price']
        change_24h = data['quotes']['USD']['percent_change_24h']

        print(f"\n--- {data['name']} ({data['symbol']}) ---")
        print(f"Price: ${price_usd:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")
    else:
        print(f"\nCoin '{coin_id}' not found!")
        print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")


# Exercise 1: Weather Function
def get_weather():
    """Fetch weather for a city using Open-Meteo API."""
    print("\n=== Weather Checker ===\n")

    city = input("Enter city name: ").strip()

    if city == "":
        print("❌ City name cannot be empty!")
        return

    # Step 1: Find latitude and longitude using Open-Meteo Geocoding API
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": city, "count": 1}

    geo_response = requests.get(geo_url, params=geo_params)

    if geo_response.status_code == 200:
        geo_data = geo_response.json()

        if "results" in geo_data:
            lat = geo_data["results"][0]["latitude"]
            lon = geo_data["results"][0]["longitude"]
            country = geo_data["results"][0]["country"]

            # Step 2: Get current weather
            weather_url = "https://api.open-meteo.com/v1/forecast"
            weather_params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
            }

            weather_response = requests.get(weather_url, params=weather_params)

            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                current = weather_data["current_weather"]

                print(f"\n🌍 City: {city.title()}, {country}")
                print(f"🌡 Temperature: {current['temperature']}°C")
                print(f"💨 Wind Speed: {current['windspeed']} km/h")
            else:
                print("❌ Failed to fetch weather data!")
        else:
            print("❌ City not found!")
    else:
        print("❌ Failed to fetch location data!")


# Exercise 2: Search todos by completion status
def search_todos():
    """Fetch todos based on completion status."""
    print("\n=== Todo Search ===\n")

    status = input("Enter status (true/false): ").lower().strip()

    if status not in ["true", "false"]:
        print("❌ Invalid input! Please enter true or false.")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed": status}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        todos = response.json()
        print(f"\n--- Todos Completed = {status} ---")
        print(f"Total Todos Found: {len(todos)}\n")

        for i, todo in enumerate(todos[:10], 1):  # first 10 todos
            print(f"{i}. {todo['title']}")
    else:
        print("❌ Failed to fetch todos!")


def main():
    """Main menu for the program."""
    print("=" * 45)
    print("   Dynamic API Query Demo (Part 3)")
    print("=" * 45)

    while True:
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. Check weather by city (NEW)")
        print("5. Search todos by completion status (NEW)")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            get_weather()
        elif choice == "5":
            search_todos()
        elif choice == "6":
            print("\n✅ Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
