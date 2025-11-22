# -*- coding: utf-8 -*-
"""Test script to check if yfinance can be imported and used."""

try:
    import yfinance as yf
    print("yfinance imported successfully")

    # Try to get a simple ticker info
    print("Creating ticker object...")
    ticker = yf.Ticker("BABA")
    print("Getting info...")
    info = ticker.info
    print(f"Got info for BABA: {list(info.keys())[:5]}...")  # Print first 5 keys
    print("Success!")

except Exception as e:
    print(f"Exception occurred: {str(e)}")
    import traceback
    print("Full traceback:")
    traceback.print_exc()
