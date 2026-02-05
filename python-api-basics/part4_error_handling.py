"""
Part 4: Robust Error Handling
=============================
Difficulty: Intermediate+

Learn:
- Try/except blocks for API requests
- Handling network errors
- Timeout handling
- Response validation
"""

import requests
from requests.exceptions import (
    ConnectionError,
    Timeout,
    HTTPError,
    RequestException
)


def safe_api_request(url, timeout=5):
    """Make an API request with proper error handling."""
    try:
        response = requests.get(url, timeout=timeout)

        # Raise exception for bad status codes (4xx, 5xx)
        response.raise_for_status()

        return {"success": True, "data": response.json()}

    except ConnectionError:
        return {"success": False, "error": "Connection failed. Check your internet."}

    except Timeout:
        return {"success": False, "error": f"Request timed out after {timeout} seconds."}

    except HTTPError as e:
        return {"success": False, "error": f"HTTP Error: {e.response.status_code}"}

    except RequestException as e:
        return {"success": False, "error": f"Request failed: {str(e)}"}


def demo_error_handling():
    """Demonstrate different error scenarios."""
    print("=== Error Handling Demo ===\n")

    # Test 1: Successful request
    print("--- Test 1: Valid URL ---")
    result = safe_api_request("https://jsonplaceholder.typicode.com/posts/1")
    if result["success"]:
        print(f"Success! Got post: {result['data']['title'][:30]}...")
    else:
        print(f"Failed: {result['error']}")

    # Test 2: 404 Error
    print("\n--- Test 2: Non-existent Resource (404) ---")
    result = safe_api_request("https://jsonplaceholder.typicode.com/posts/99999")
    if result["success"]:
        print(f"Success! Data: {result['data']}")
    else:
        print(f"Failed: {result['error']}")

    # Test 3: Invalid domain
    print("\n--- Test 3: Invalid Domain ---")
    result = safe_api_request("https://this-domain-does-not-exist-12345.com/api")
    if result["success"]:
        print(f"Success!")
    else:
        print(f"Failed: {result['error']}")

    # Test 4: Timeout (using very short timeout)
    print("\n--- Test 4: Timeout Simulation ---")
    result = safe_api_request("https://httpstat.us/200?sleep=5000", timeout=1)
    if result["success"]:
        print(f"Success!")
    else:
        print(f"Failed: {result['error']}")


def fetch_crypto_safely():
    """Fetch crypto data with full error handling."""
    print("\n=== Safe Crypto Price Checker ===\n")

    coin = input("Enter coin (btc-bitcoin, eth-ethereum): ").strip().lower()

    if not coin:
        print("Error: Please enter a coin name.")
        return

    url = f"https://api.coinpaprika.com/v1/tickers/{coin}"
    result = safe_api_request(url)

    if result["success"]:
        data = result["data"]
        print(f"\n{data['name']} ({data['symbol']})")
        print(f"Price: ${data['quotes']['USD']['price']:,.2f}")
        print(f"24h Change: {data['quotes']['USD']['percent_change_24h']:+.2f}%")
    else:
        print(f"\nError: {result['error']}")
        print("Tip: Try 'btc-bitcoin' or 'eth-ethereum'")


def validate_json_response():
    """Demonstrate JSON validation."""
    print("\n=== JSON Validation Demo ===\n")

    url = "https://jsonplaceholder.typicode.com/users/1"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Validate expected fields exist
        required_fields = ["name", "email", "phone"]
        missing = [f for f in required_fields if f not in data]

        if missing:
            print(f"Warning: Missing fields: {missing}")
        else:
            print("All required fields present!")
            print(f"Name: {data['name']}")
            print(f"Email: {data['email']}")
            print(f"Phone: {data['phone']}")

    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not valid JSON")

    except Exception as e:
        print(f"Error: {e}")


def main():
    """Run all demos."""
    demo_error_handling()
    print("\n" + "=" * 40 + "\n")
    validate_json_response()
    print("\n" + "=" * 40 + "\n")
    fetch_crypto_safely()


if __name__ == "__main__":
    main()


# --- EXERCISES ---
#
# Exercise 1: Add retry logic - if request fails, try again up to 3 times
#             Hint: Use a for loop and time.sleep() between retries
#
# Exercise 2: Create a function that validates crypto response
#             Check that 'quotes' and 'USD' keys exist before accessing
#
# Exercise 3: Add logging to track all API requests
#             import logging
#             logging.basicConfig(level=logging.INFO)


import requests
import time
import logging
from requests.exceptions import (
    ConnectionError,
    Timeout,
    HTTPError,
    RequestException
)

# Exercise 3: Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def safe_api_request(url, timeout=5, retries=3, delay=2):
    """
    Exercise 1: Retry logic included
    Make an API request with proper error handling + retry system.
    """

    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Request Attempt {attempt}: GET {url}")

            response = requests.get(url, timeout=timeout)

            # Raise exception for bad status codes (4xx, 5xx)
            response.raise_for_status()

            logging.info(f"Success Response: {response.status_code}")

            return {"success": True, "data": response.json()}

        except ConnectionError:
            error_msg = "Connection failed. Check your internet."
            logging.error(error_msg)

        except Timeout:
            error_msg = f"Request timed out after {timeout} seconds."
            logging.error(error_msg)

        except HTTPError as e:
            error_msg = f"HTTP Error: {e.response.status_code}"
            logging.error(error_msg)

        except RequestException as e:
            error_msg = f"Request failed: {str(e)}"
            logging.error(error_msg)

        # Retry if not last attempt
        if attempt < retries:
            logging.info(f"Retrying in {delay} seconds...")
            time.sleep(delay)

    return {"success": False, "error": error_msg}


# Exercise 2: Validate crypto response before accessing keys
def validate_crypto_response(data):
    """
    Validate crypto JSON response structure.
    Checks if quotes -> USD -> price exists.
    """

    if "quotes" not in data:
        return False, "Missing 'quotes' key in response."

    if "USD" not in data["quotes"]:
        return False, "Missing 'USD' key inside quotes."

    if "price" not in data["quotes"]["USD"]:
        return False, "Missing 'price' key inside USD quotes."

    if "percent_change_24h" not in data["quotes"]["USD"]:
        return False, "Missing 'percent_change_24h' key inside USD quotes."

    return True, "Valid response"


def demo_error_handling():
    """Demonstrate different error scenarios."""
    print("=== Error Handling Demo ===\n")

    # Test 1: Successful request
    print("--- Test 1: Valid URL ---")
    result = safe_api_request("https://jsonplaceholder.typicode.com/posts/1")
    if result["success"]:
        print(f"Success! Got post: {result['data']['title'][:30]}...")
    else:
        print(f"Failed: {result['error']}")

    # Test 2: 404 Error
    print("\n--- Test 2: Non-existent Resource (404) ---")
    result = safe_api_request("https://jsonplaceholder.typicode.com/posts/99999")
    if result["success"]:
        print(f"Success! Data: {result['data']}")
    else:
        print(f"Failed: {result['error']}")

    # Test 3: Invalid domain
    print("\n--- Test 3: Invalid Domain ---")
    result = safe_api_request("https://this-domain-does-not-exist-12345.com/api")
    if result["success"]:
        print("Success!")
    else:
        print(f"Failed: {result['error']}")

    # Test 4: Timeout simulation
    print("\n--- Test 4: Timeout Simulation ---")
    result = safe_api_request("https://httpstat.us/200?sleep=5000", timeout=1)
    if result["success"]:
        print("Success!")
    else:
        print(f"Failed: {result['error']}")


def fetch_crypto_safely():
    """Fetch crypto data with full error handling + validation."""
    print("\n=== Safe Crypto Price Checker ===\n")

    coin = input("Enter coin (btc-bitcoin, eth-ethereum): ").strip().lower()

    if not coin:
        print("❌ Error: Please enter a coin name.")
        return

    url = f"https://api.coinpaprika.com/v1/tickers/{coin}"
    result = safe_api_request(url)

    if result["success"]:
        data = result["data"]

        # Exercise 2 validation
        valid, message = validate_crypto_response(data)

        if not valid:
            print(f"❌ Invalid crypto response: {message}")
            return

        price = data["quotes"]["USD"]["price"]
        change_24h = data["quotes"]["USD"]["percent_change_24h"]

        print(f"\n✅ {data['name']} ({data['symbol']})")
        print(f"Price: ${price:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")

    else:
        print(f"\n❌ Error: {result['error']}")
        print("Tip: Try 'btc-bitcoin' or 'eth-ethereum'")


def validate_json_response():
    """Demonstrate JSON validation."""
    print("\n=== JSON Validation Demo ===\n")

    url = "https://jsonplaceholder.typicode.com/users/1"

    result = safe_api_request(url)

    if result["success"]:
        data = result["data"]

        required_fields = ["name", "email", "phone"]
        missing = [f for f in required_fields if f not in data]

        if missing:
            print(f"⚠ Warning: Missing fields: {missing}")
        else:
            print("✅ All required fields present!")
            print(f"Name: {data['name']}")
            print(f"Email: {data['email']}")
            print(f"Phone: {data['phone']}")
    else:
        print(f"❌ Error: {result['error']}")


def main():
    """Run all demos."""
    demo_error_handling()
    print("\n" + "=" * 40 + "\n")
    validate_json_response()
    print("\n" + "=" * 40 + "\n")
    fetch_crypto_safely()


if __name__ == "__main__":
    main()
