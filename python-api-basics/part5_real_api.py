"""
Part 5: Real-World APIs - Weather & Crypto Dashboard
====================================================
Difficulty: Advanced

Learn:
- Working with multiple real APIs
- Data formatting and presentation
- Building a simple CLI dashboard
- Using environment variables for API keys (optional)
"""

import requests
from datetime import datetime


# City coordinates (latitude, longitude)
CITIES = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "hyderabad": (17.3850, 78.4867),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "tokyo": (35.6762, 139.6503),
    "sydney": (-33.8688, 151.2093),
}

# Popular cryptocurrencies
CRYPTO_IDS = {
    "bitcoin": "btc-bitcoin",
    "ethereum": "eth-ethereum",
    "dogecoin": "doge-dogecoin",
    "cardano": "ada-cardano",
    "solana": "sol-solana",
    "ripple": "xrp-xrp",
}


def get_weather(city_name):
    """
    Fetch weather data using Open-Meteo API (FREE, no API key needed).
    """
    city_lower = city_name.lower().strip()

    if city_lower not in CITIES:
        print(f"\nCity '{city_name}' not found.")
        print(f"Available cities: {', '.join(CITIES.keys())}")
        return None

    lat, lon = CITIES[city_lower]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,relative_humidity_2m",
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None


def display_weather(city_name):
    """Display formatted weather information."""
    data = get_weather(city_name)

    if not data:
        return

    current = data["current_weather"]

    print(f"\n{'=' * 40}")
    print(f"  Weather in {city_name.title()}")
    print(f"{'=' * 40}")
    print(f"  Temperature: {current['temperature']}°C")
    print(f"  Wind Speed: {current['windspeed']} km/h")
    print(f"  Wind Direction: {current['winddirection']}°")

    # Weather condition codes
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Foggy", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
        95: "Thunderstorm",
    }

    code = current.get("weathercode", 0)
    condition = weather_codes.get(code, "Unknown")
    print(f"  Condition: {condition}")
    print(f"{'=' * 40}")


def get_crypto_price(coin_name):
    """
    Fetch crypto data using CoinPaprika API (FREE, no API key needed).
    """
    coin_lower = coin_name.lower().strip()

    # Map common name to API ID
    coin_id = CRYPTO_IDS.get(coin_lower, coin_lower)

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching crypto data: {e}")
        return None


def display_crypto(coin_name):
    """Display formatted crypto information."""
    data = get_crypto_price(coin_name)

    if not data:
        print(f"\nCoin '{coin_name}' not found.")
        print(f"Available: {', '.join(CRYPTO_IDS.keys())}")
        return

    usd = data["quotes"]["USD"]

    print(f"\n{'=' * 40}")
    print(f"  {data['name']} ({data['symbol']})")
    print(f"{'=' * 40}")
    print(f"  Price: ${usd['price']:,.2f}")
    print(f"  Market Cap: ${usd['market_cap']:,.0f}")
    print(f"  24h Volume: ${usd['volume_24h']:,.0f}")
    print(f"  ")
    print(f"  1h Change:  {usd['percent_change_1h']:+.2f}%")
    print(f"  24h Change: {usd['percent_change_24h']:+.2f}%")
    print(f"  7d Change:  {usd['percent_change_7d']:+.2f}%")
    print(f"{'=' * 40}")


def get_top_cryptos(limit=5):
    """Fetch top cryptocurrencies by market cap."""
    url = "https://api.coinpaprika.com/v1/tickers"
    params = {"limit": limit}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


def display_top_cryptos():
    """Display top 5 cryptocurrencies."""
    data = get_top_cryptos(5)

    if not data:
        return

    print(f"\n{'=' * 55}")
    print(f"  Top 5 Cryptocurrencies by Market Cap")
    print(f"{'=' * 55}")
    print(f"  {'Rank':<6}{'Name':<15}{'Price':<15}{'24h Change'}")
    print(f"  {'-' * 50}")

    for coin in data:
        usd = coin["quotes"]["USD"]
        change = usd["percent_change_24h"]
        change_str = f"{change:+.2f}%"

        print(f"  {coin['rank']:<6}{coin['name']:<15}${usd['price']:>12,.2f}  {change_str}")

    print(f"{'=' * 55}")


def dashboard():
    """Interactive dashboard combining weather and crypto."""
    print("\n" + "=" * 50)
    print("   Real-World API Dashboard")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Check Weather")
        print("  2. Check Crypto Price")
        print("  3. View Top 5 Cryptos")
        print("  4. Quick Dashboard (Delhi + Bitcoin)")
        print("  5. Exit")

        choice = input("\nSelect (1-5): ").strip()

        if choice == "1":
            print(f"\nAvailable: {', '.join(CITIES.keys())}")
            city = input("Enter city name: ")
            display_weather(city)

        elif choice == "2":
            print(f"\nAvailable: {', '.join(CRYPTO_IDS.keys())}")
            coin = input("Enter crypto name: ")
            display_crypto(coin)

        elif choice == "3":
            display_top_cryptos()

        elif choice == "4":
            display_weather("delhi")
            display_crypto("bitcoin")

        elif choice == "5":
            print("\nGoodbye! Happy coding!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    dashboard()


# --- CHALLENGE EXERCISES ---
#
# Exercise 1: Add more cities to the CITIES dictionary
#             Find coordinates at: https://www.latlong.net/
#
# Exercise 2: Create a function that compares prices of multiple cryptos
#             Display them in a formatted table
#
# Exercise 3: Add POST request example
#             Use: https://jsonplaceholder.typicode.com/posts
#             Send: requests.post(url, json={"title": "My Post", "body": "Content"})
#
# Exercise 4: Save results to a JSON file
#             import json
#             with open("results.json", "w") as f:
#                 json.dump(data, f, indent=2)
#
# Exercise 5: Add API key support for OpenWeatherMap
#             Sign up at: https://openweathermap.org/api
#             Use environment variables:
#             import os
#             api_key = os.environ.get("OPENWEATHER_API_KEY")

import requests
import json
import os
from datetime import datetime


# Exercise 1: More cities added
CITIES = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "hyderabad": (17.3850, 78.4867),
    "pune": (18.5204, 73.8567),
    "nagpur": (21.1458, 79.0882),
    "jaipur": (26.9124, 75.7873),
    "ahmedabad": (23.0225, 72.5714),
    "dubai": (25.2048, 55.2708),
    "paris": (48.8566, 2.3522),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "tokyo": (35.6762, 139.6503),
    "sydney": (-33.8688, 151.2093),
}

CRYPTO_IDS = {
    "bitcoin": "btc-bitcoin",
    "ethereum": "eth-ethereum",
    "dogecoin": "doge-dogecoin",
    "cardano": "ada-cardano",
    "solana": "sol-solana",
    "ripple": "xrp-xrp",
}


# Exercise 5: OpenWeatherMap API Key support
OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")


def save_to_json(filename, data):
    """Exercise 4: Save data to JSON file."""
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n✅ Data saved successfully to {filename}")
    except Exception as e:
        print(f"❌ Failed to save file: {e}")


# ---------------- WEATHER FUNCTIONS ---------------- #

def get_weather_open_meteo(city_name):
    """Fetch weather using Open-Meteo API."""
    city_lower = city_name.lower().strip()

    if city_lower not in CITIES:
        print(f"\n❌ City '{city_name}' not found.")
        print(f"Available cities: {', '.join(CITIES.keys())}")
        return None

    lat, lon = CITIES[city_lower]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"❌ Error fetching weather: {e}")
        return None


def get_weather_openweather(city_name):
    """
    Exercise 5: OpenWeatherMap weather (requires API key).
    Only works if OPENWEATHER_API_KEY is set.
    """
    if not OPENWEATHER_API_KEY:
        print("\n❌ OpenWeather API Key not found in environment variables.")
        print("Set it like: OPENWEATHER_API_KEY=yourkey")
        return None

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"❌ Error fetching OpenWeather data: {e}")
        return None


def display_weather(city_name):
    """Display formatted weather info using Open-Meteo."""
    data = get_weather_open_meteo(city_name)

    if not data:
        return

    current = data["current_weather"]

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Foggy", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
        95: "Thunderstorm",
    }

    code = current.get("weathercode", 0)
    condition = weather_codes.get(code, "Unknown")

    print(f"\n{'=' * 45}")
    print(f" 🌍 Weather in {city_name.title()}")
    print(f"{'=' * 45}")
    print(f" Temperature: {current['temperature']}°C")
    print(f" Wind Speed: {current['windspeed']} km/h")
    print(f" Wind Direction: {current['winddirection']}°")
    print(f" Condition: {condition}")
    print(f"{'=' * 45}")

    save_choice = input("\nSave this weather data to JSON? (y/n): ").lower()
    if save_choice == "y":
        save_to_json(f"{city_name.lower()}_weather.json", data)


# ---------------- CRYPTO FUNCTIONS ---------------- #

def get_crypto_price(coin_name):
    """Fetch crypto data using CoinPaprika API."""
    coin_lower = coin_name.lower().strip()
    coin_id = CRYPTO_IDS.get(coin_lower, coin_lower)

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


def display_crypto(coin_name):
    """Display formatted crypto info."""
    data = get_crypto_price(coin_name)

    if not data:
        print(f"\n❌ Coin '{coin_name}' not found.")
        print(f"Available: {', '.join(CRYPTO_IDS.keys())}")
        return

    usd = data["quotes"]["USD"]

    print(f"\n{'=' * 50}")
    print(f" 💰 {data['name']} ({data['symbol']})")
    print(f"{'=' * 50}")
    print(f" Price: ${usd['price']:,.2f}")
    print(f" Market Cap: ${usd['market_cap']:,.0f}")
    print(f" 24h Volume: ${usd['volume_24h']:,.0f}")
    print(f"")
    print(f" 1h Change:  {usd['percent_change_1h']:+.2f}%")
    print(f" 24h Change: {usd['percent_change_24h']:+.2f}%")
    print(f" 7d Change:  {usd['percent_change_7d']:+.2f}%")
    print(f"{'=' * 50}")

    save_choice = input("\nSave this crypto data to JSON? (y/n): ").lower()
    if save_choice == "y":
        save_to_json(f"{coin_name.lower()}_crypto.json", data)


def get_top_cryptos(limit=5):
    """Fetch top cryptocurrencies by market cap."""
    url = "https://api.coinpaprika.com/v1/tickers"
    params = {"limit": limit}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


def display_top_cryptos():
    """Display top 5 cryptos."""
    data = get_top_cryptos(5)

    if not data:
        print("❌ Failed to fetch top cryptos.")
        return

    print(f"\n{'=' * 65}")
    print(f" 🚀 Top 5 Cryptocurrencies by Market Cap")
    print(f"{'=' * 65}")
    print(f"{'Rank':<6}{'Name':<15}{'Price':<18}{'24h Change'}")
    print(f"{'-' * 65}")

    for coin in data:
        usd = coin["quotes"]["USD"]
        print(f"{coin['rank']:<6}{coin['name']:<15}${usd['price']:>12,.2f}      {usd['percent_change_24h']:+.2f}%")

    print(f"{'=' * 65}")

    save_choice = input("\nSave this list to JSON? (y/n): ").lower()
    if save_choice == "y":
        save_to_json("top_5_cryptos.json", data)


# Exercise 2: Compare multiple cryptos
def compare_cryptos():
    """
    Compare multiple crypto prices in a table.
    Example input: bitcoin, ethereum, dogecoin
    """
    print("\n=== Crypto Comparison Tool ===\n")
    coins_input = input("Enter coin names separated by comma (e.g. bitcoin, ethereum): ")

    coins = [c.strip().lower() for c in coins_input.split(",") if c.strip()]

    if not coins:
        print("❌ No coins entered!")
        return

    results = []

    for coin in coins:
        data = get_crypto_price(coin)

        if data:
            usd = data["quotes"]["USD"]
            results.append({
                "name": data["name"],
                "symbol": data["symbol"],
                "price": usd["price"],
                "change_24h": usd["percent_change_24h"]
            })
        else:
            results.append({
                "name": coin,
                "symbol": "N/A",
                "price": None,
                "change_24h": None
            })

    print(f"\n{'=' * 65}")
    print(" 📊 Crypto Comparison Table")
    print(f"{'=' * 65}")
    print(f"{'Name':<15}{'Symbol':<10}{'Price (USD)':<20}{'24h Change'}")
    print(f"{'-' * 65}")

    for r in results:
        if r["price"] is None:
            print(f"{r['name']:<15}{r['symbol']:<10}{'Not Found':<20}{'N/A'}")
        else:
            print(f"{r['name']:<15}{r['symbol']:<10}${r['price']:>12,.2f}        {r['change_24h']:+.2f}%")

    print(f"{'=' * 65}")

    save_choice = input("\nSave this comparison to JSON? (y/n): ").lower()
    if save_choice == "y":
        save_to_json("crypto_comparison.json", results)


# Exercise 3: POST request example
def create_post():
    """Create a new post using JSONPlaceholder POST request."""
    print("\n=== Create a Post (POST Request Demo) ===\n")

    title = input("Enter post title: ").strip()
    body = input("Enter post content: ").strip()

    if not title or not body:
        print("❌ Title and Body cannot be empty!")
        return

    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": 1
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()

        print("\n✅ Post Created Successfully!")
        print(data)

        save_choice = input("\nSave this post response to JSON? (y/n): ").lower()
        if save_choice == "y":
            save_to_json("created_post.json", data)

    except requests.RequestException as e:
        print(f"❌ Failed to create post: {e}")


# ---------------- DASHBOARD ---------------- #

def dashboard():
    """Interactive dashboard combining weather + crypto + extras."""
    print("\n" + "=" * 60)
    print("   🌍 Real-World API Dashboard (Part 5)")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    while True:
        print("\nOptions:")
        print("  1. Check Weather (Open-Meteo)")
        print("  2. Check Crypto Price")
        print("  3. View Top 5 Cryptos")
        print("  4. Quick Dashboard (Delhi + Bitcoin)")
        print("  5. Compare Multiple Cryptos (NEW)")
        print("  6. Create a Post (POST Request) (NEW)")
        print("  7. Check Weather using OpenWeatherMap (API KEY) (NEW)")
        print("  8. Exit")

        choice = input("\nSelect (1-8): ").strip()

        if choice == "1":
            print(f"\nAvailable Cities: {', '.join(CITIES.keys())}")
            city = input("Enter city name: ")
            display_weather(city)

        elif choice == "2":
            print(f"\nAvailable Cryptos: {', '.join(CRYPTO_IDS.keys())}")
            coin = input("Enter crypto name: ")
            display_crypto(coin)

        elif choice == "3":
            display_top_cryptos()

        elif choice == "4":
            display_weather("delhi")
            display_crypto("bitcoin")

        elif choice == "5":
            compare_cryptos()

        elif choice == "6":
            create_post()

        elif choice == "7":
            city = input("Enter city name: ")
            data = get_weather_openweather(city)

            if data:
                print(f"\n{'=' * 45}")
                print(f" 🌍 OpenWeatherMap Weather - {city.title()}")
                print(f"{'=' * 45}")
                print(f" Temperature: {data['main']['temp']}°C")
                print(f" Feels Like: {data['main']['feels_like']}°C")
                print(f" Humidity: {data['main']['humidity']}%")
                print(f" Condition: {data['weather'][0]['description'].title()}")
                print(f"{'=' * 45}")

                save_choice = input("\nSave this weather data to JSON? (y/n): ").lower()
                if save_choice == "y":
                    save_to_json(f"{city.lower()}_openweather.json", data)

        elif choice == "8":
            print("\n✅ Goodbye! Happy coding! 🚀")
            break

        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    dashboard()
