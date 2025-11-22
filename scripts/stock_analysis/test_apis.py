import requests
from bs4 import BeautifulSoup

print("Testing financial APIs for BABA stock price...")

# Test Alpha Vantage
print("\n1. Alpha Vantage...")
try:
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=BABA&apikey=demo"
    r = requests.get(url, timeout=10)
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"Keys: {list(data.keys())}")
        if "Global Quote" in data and data["Global Quote"]:
            print(f"Price: {data['Global Quote'].get('05. price')}")
except Exception as e:
    print(f"Failed: {e}")

# Test Yahoo Finance
print("\n2. Yahoo Finance...")
try:
    url = "https://finance.yahoo.com/quote/BABA/"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    r = requests.get(url, headers=headers, timeout=10)
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        price_elem = soup.find('fin-streamer', {'data-symbol': 'BABA'})
        if price_elem:
            print(f"Price element found: {price_elem.text[:20]}")
except Exception as e:
    print(f"Failed: {e}")

# Test IEX Cloud
print("\n3. IEX Cloud...")
try:
    url = "https://cloud.iexapis.com/stable/stock/BABA/quote?token=pk_demo_token"
    r = requests.get(url, timeout=10)
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"Latest Price: {data.get('latestPrice')}")
except Exception as e:
    print(f"Failed: {e}")

print("\nDone testing.")
