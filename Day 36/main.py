from creds import ALPHAVANTAGE_API_KEY
from datetime import date, timedelta
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

today = date.today()
yesterday = today - timedelta(days=2)
day_before_yesterday = yesterday - timedelta(days=2)
print(f"Today is: {today}\nYesterday was: {yesterday}\nDay before yesterday was: {day_before_yesterday}")

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK_NAME}' \
      f'&interval=5min&apikey={ALPHAVANTAGE_API_KEY}&outputsize=compact '

r = requests.get(url)
print(f"Sending request to:  {r.url}")
data = r.json()
get_yesterday_close_price = data['Time Series (Daily)'][f'{yesterday}']['4. close']
yesterday_close_price = '${:,.2f}'.format(float(get_yesterday_close_price))
get_previous_day_close_price = data['Time Series (Daily)'][f'{day_before_yesterday}']['4. close']
previous_day_close = '${:,.2f}'.format(float(get_previous_day_close_price))
print(
    f"[{yesterday}] Closing Price: {yesterday_close_price}\n[{day_before_yesterday}] Closing Price: {previous_day_close}")

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(get_previous_day_close_price) - float(get_yesterday_close_price)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percent_change = (difference / float(get_previous_day_close_price)) * 100

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percent_change > 5:
    print('Get News')
else:
    print('Not 5% change')
## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
