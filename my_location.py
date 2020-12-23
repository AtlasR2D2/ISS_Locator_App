import requests



def get_location():
    try:
        url = 'http://ipinfo.io/json'
        response = requests.get(url=url)
        response.raise_for_status()
        json_data = response.json()
        loc_data = json_data["loc"].split(",")
        lat = float(loc_data[0])
        lng = float(loc_data[1])
    except:
        return "Couldn't retrieve IP Address"
    else:
        return {"lat": lat, "lng": lng}

