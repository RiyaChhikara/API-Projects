# Weather_API-
## Description
This Python script checks the weather forecast for a specific location and sends a text message alert using the Twilio API if it's going to rain within the next 12 hours.
![Text by Twilio](https://github.com/RiyaChhikara/API-Projects-/assets/115228191/66ae3036-d7aa-4375-97fe-6e4aae0703dd)

## Prerequisites
Before using this script, you need to have the following:

OpenWeatherMap API Key: You'll need to sign up for an OpenWeatherMap API key and replace api_key1 with your own key.
![OneWeatherMap API](https://github.com/RiyaChhikara/API-Projects-/assets/115228191/a0741af1-c8ae-4b25-9b8d-e7b1d3a9a4fc)

Twilio Account SID and Auth Token: You should have a Twilio account and obtain your Account SID and Auth Token. Replace account_sid and auth_token with your Twilio credentials.
![Twilio](https://github.com/RiyaChhikara/API-Projects-/assets/115228191/0402e572-0893-42e1-83d9-73526c801dba)

Twilio Phone Numbers: Make sure you have access to Twilio phone numbers. Replace the from and to numbers with the appropriate phone numbers.

## Installation
Make sure you have Python installed on your system.

Install the required libraries using pip:
pip install requests twilio

## Configuration
You need to set the following variables in the script:

api_key1: Replace this with your OpenWeatherMap API key.
account_sid: Replace this with your Twilio Account SID.
auth_token: Replace this with your Twilio Auth Token.
from: Replace this with your Twilio phone number (sender's number).
to: Replace this with your recipient's phone number.

## Usage
Open a terminal and navigate to the directory containing the Python script.
Run the script using the following command:
python weather_alert.py

The script will check the weather forecast for the location defined in latitude and longitude.
If rain is predicted within the next 12 hours, it will send a text message using the Twilio API to the specified recipient.

## Customization
You can customize the location for which you want to check the weather by changing the values of lat and lon in the weather_params dictionary.
You can adjust the number of hours to check for rain by changing the slice of hourly data in the weather_data dictionary. The current configuration checks for the next 12 hours.
You can modify the rain condition by changing the condition_code comparison. The script currently considers any condition code less than 700 as indicating rain.

## Acknowledgments
This script was created by Riya as a learning project.
If you encounter any issues or have suggestions for improvement, please feel free to file an issue or create a pull request on the GitHub repository.
