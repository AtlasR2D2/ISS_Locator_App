import requests
import time
from datetime import datetime
from email_script import send_email
from my_location import get_location


MY_LOCATION = get_location()
MY_LAT = MY_LOCATION["lat"]     # Your latitude
MY_LONG = MY_LOCATION["lng"]    # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

json_data = response.json()
iss_position = {key: float(value) for (key, value) in json_data["iss_position"].items()}

iss_latitude = iss_position["latitude"]
iss_longitude = iss_position["longitude"]

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
# Key Lookup between parameter dictionaries
key_lookup = {"latitude": "lat",
              "longitude": "lng"
              }

# Your position is within +5 or -5 degrees of the ISS position.
my_viewpoint = {key: [value-5, value+5] for (key, value) in parameters.items() if key in ["lat", "lng"]}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
visible_flag = False
if sunset <= time_now.hour <= sunrise:
    # Night time viewing window activated
    visible_flag = True
    for key, value in iss_position.items():
        if my_viewpoint[key_lookup[key]][0] <= value <= my_viewpoint[key_lookup[key]][1]:
            visible_flag = True
        else:
            visible_flag = False
    # Check if ISS within visible viewpoint
    if visible_flag:
        send_email(iss_position["latitude"], iss_position["longitude"])
