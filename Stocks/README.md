# Stocks-API
This Python script retrieves the daily stock price data for a specific company and sends news articles related to the company if there is a significant change in the stock price. It uses Alpha Vantage to fetch stock price data and News API to get news articles. If the stock price change is greater than a certain threshold, it sends news articles via Twilio to your specified phone number.

<img src = "https://github.com/RiyaChhikara/API-Projects-/assets/115228191/d09d9051-5c27-4cbb-b55f-cf0d4225986e" width="500"/>

## Prerequisites
Before using this script, you need to have the following:

- Alpha Vantage API Key: Sign up for an Alpha Vantage API key and replace STOCK_API_KEY with your own key.

- News API Key: Obtain a News API key and replace NEWS_API_KEY with your key.

- Twilio Account SID and Auth Token: You should have a Twilio account and obtain your Account SID and Auth Token. Replace TWILIO_SID and TWILIO_AUTH_TOKEN with your Twilio credentials.

- Twilio Phone Numbers: Make sure you have access to Twilio phone numbers. Replace the from and to numbers with the appropriate phone numbers.

## Usage
Open a terminal and navigate to the directory containing the Python script.
Run the script using the following command:
- python stock_price_and_news_alert.py
  
The script will fetch the daily stock price data for the specified stock and calculate the percentage change between yesterday's and the day before yesterday's closing price.
If the percentage change is greater than the threshold, it will retrieve news articles related to the company from the News API.
It will send the top three news articles via Twilio to your specified phone number.

## Customization
You can change the STOCK_NAME and COMPANY_NAME variables to target a different stock and company.
You can modify the diff_percent threshold to change when the script sends news articles based on the percentage change in stock price.
You can adjust the number of news articles to retrieve and send by modifying the articles[:3] line.
Replace the from and to phone numbers in the Twilio message sending section with the appropriate phone numbers.

## Acknowledgments
This script was created by Riya as a learning project.
If you encounter any issues or have suggestions for improvement, please feel free to file an issue or create a pull request on the GitHub repository.

