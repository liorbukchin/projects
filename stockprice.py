import requests
#API KEY = the api key contains the key that we created in the alpha vantege website
API_KEY = '9AELFQSJQUK01YTN'
#symbol= stock name 
symbol = 'TSLA'

# var urlalphavantage -----> contain real time stock data
urlalphavantage = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"

try:
    # the response var gets the data of the stock using the urlalphavantage that contains the {API} and the {symbol}
    print(urlalphavantage)
    response = requests.get(urlalphavantage)

    #json convert the data to python readable format. - json (JavaScript Object Notation)
    data = response.json()
    # navigating through the JSON data using dictionary keys. ---> 'Global Quote']['05. price'] points to the key that holds the latest stock price
    #for example:there's a key named 'Global Quote'.this is like a folder with more information inside of it.this is where latest price is stored.
    latest_price = data['Global Quote']['05. price']

    print(f"The price of a {symbol} stock is: ${latest_price}")


except Exception as e:
    # e= error, it contains the eror data 
    print("Houston we got a problem:", e)

