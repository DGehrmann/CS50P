import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r = r.json()
    except requests.RequestException:
        pass

    price_float = r["bpi"]["USD"]["rate_float"]

    amount = price_float * float(sys.argv[1])

    print(f"${amount:,.4f}")