from creds import *
from datetime import date, timedelta
from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

articles = []
percent_change = 0


def get_articles(change, list_of_articles):
    # Date Information
    today = date.today()
    yesterday = today - timedelta(days=1)
    day_before_yesterday = yesterday - timedelta(days=1)
    print(f"Today is: {today}\nYesterday was: {yesterday}\nDay before yesterday was: {day_before_yesterday}")

    # Using the NEWS API
    url = ('https://newsapi.org/v2/everything?'
           f'q={COMPANY_NAME}&'
           f'from={yesterday}&'
           'sortBy=popularity&'
           f'apiKey={NEWS_API_KEY}')
    response = requests.get(url)
    data = response.json()['articles']
    for key in data[:3]:
        list_of_articles.append(key)

    # Using ALPHAVANTAGE API
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK_NAME}' \
          f'&interval=5min&apikey={ALPHAVANTAGE_API_KEY}&outputsize=compact '
    response = requests.get(url)
    data = response.json()

    # Getting Each Day's Closing price
    get_yesterday_close_price = data['Time Series (Daily)'][f'{yesterday}']['4. close']
    yesterday_close_price = '${:,.2f}'.format(float(get_yesterday_close_price))
    get_previous_day_close_price = data['Time Series (Daily)'][f'{day_before_yesterday}']['4. close']
    previous_day_close = '${:,.2f}'.format(float(get_previous_day_close_price))

    difference = float(get_previous_day_close_price) - float(get_yesterday_close_price)
    change = round((difference / float(get_previous_day_close_price)) * 100, 2)


get_articles(percent_change, articles)


def send_message(change):
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    for index, keys in enumerate(articles):
        if percent_change < -5:
            print(f'The percent change is {percent_change}. Sending message.')
            message = client.messages.create(
                body=f"{STOCK_NAME}: 🔺{percent_change}%\nHeadline: {articles[index]['title']}."
                     f"\nBrief: {articles[0]['description']}",
                from_=f'{TWILIO_PHONE_NUMBER}',
                to=f'{MY_PHONE_NUMBER}'
            )
        elif percent_change > 5:
            print(f'The percent change is {percent_change}. Sending message.')
            message = client.messages.create(
                body=f"{STOCK_NAME}: 🔻{percent_change}%\nHeadline: {articles[index]['title']}."
                     f"\nBrief: {articles[0]['description']}",
                from_=f'{TWILIO_PHONE_NUMBER}',
                to=f'{MY_PHONE_NUMBER}'
            )
        else:
            print(f'There has not been any major change.')
            message = client.messages.create(
                body=f"{STOCK_NAME}: 😬No major changes.",
                from_=f'{TWILIO_PHONE_NUMBER}',
                to=f'{MY_PHONE_NUMBER}'
            )
        print(f'The status of the sent message: {message.status}')


send_message(percent_change)

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
