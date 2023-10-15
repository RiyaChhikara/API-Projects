import requests
from twilio.rest import Client

STOCK_NAME = "RELIANCE.BSE"
COMPANY_NAME = "Reliance Industries"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "Your stocks API Key"
NEWS_API_KEY = "Your News API Key"
TWILIO_SID = "Your Twilio SID"
TWILIO_AUTH_TOKEN = "Your Twilio Auth Token"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT,stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data["4. close"]

day_before_yesterday_data =data_list[1]
day_before_yesterdays_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterdays_closing_price) - float(day_before_yesterdays_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterdays_closing_price)) * 100)

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article ['title']} \nBrief: " \
                          f"{article ['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_="twilio number",
            to="Your real number"
        )
