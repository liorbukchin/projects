import sys
import time
import requests
# Import the dictionary from the company_data_symbols.py file
from company_data_symbols import company_symbols



# Prompt the user for a company name
user_input = input("Enter the name of the company: ")

# Search for the trading symbol in the dictionary
trading_symbol = company_symbols.get(user_input)
if trading_symbol:
    #print(f"The trading symbol for {user_input} is {trading_symbol}.")
    # Save the trading symbol to a variable
    symbol_var = trading_symbol
else:
    print(f"Trading symbol for {user_input} not found.")
    # Set the symbol_var to None if symbol is not found
    symbol_var = None
    sys.exit()



#API KEY = the api key contains the key that we created in the alpha vantege website
API_KEY = '9AELFQSJQUK01YTN'
#symbol= stock name 
symbol = symbol_var
# var urlalphavantage -----> contain real time stock data
urlalphavantage = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"


while 1 < 3:
    try:
        # the response var gets the data of the stock using the urlalphavantage that contains the {API} and the {symbol}
        response = requests.get(urlalphavantage)

        #json convert the data to python readable format. - json (JavaScript Object Notation)
        data = response.json()
        # navigating through the JSON data using dictionary keys. ---> 'Global Quote']['05. price'] points to the key that holds the latest stock price
        #for example:there's a key named 'Global Quote'.this is like a folder with more information inside of it.this is where latest price is stored.
        latest_price = data['Global Quote']['05. price']
        print(f"The price of a {symbol} stock is: ${latest_price}")
        time.sleep(5)
    except Exception as e:
        # e= error, it contains the eror data
        print("Houston we got a problem :", e,type(e))
        time.sleep(5)