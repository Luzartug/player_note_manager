import pandas as pd
import yfinance as yf
#from yahoofinancials import YahooFinancials

def main():
    aapl_df = yf.download('AAPL', 
                      start='2023-01-12', 
                      end='2023-05-12', 
                      progress=False,
    )
    print(aapl_df.head())

if __name__ == "__main__":
    main()