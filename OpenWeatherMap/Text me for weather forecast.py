import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key1 = "***"
api_key2 = "***"
account_sid = "***"
auth_token = "***"

weather_params = {
    "lat": 51.507351,
    "lon": -0.1277758,
    "appid": api_key1,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code =hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from="***",
        to="***"
    )
    print(message.status)
