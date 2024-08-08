import requests


class Weather :
    """Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates

    Package use example:

    # Create a weather object using a city name
    # Get your own apikey from https://api.openweathermap.org
    
    >>> weather1 = Weather(apikey="xxxxxxxxxxxxxxxxxxxx", city="Madrid")

    # Using lattitude and longitude coordinates
    >>> weather2 = Weather(apikey="xxxxxxxxxxxxxxxxxxxx", lat=41.2, lon=-4.6)

    # Get complete weather data for the next 12 hours:
    >>> weather1.next_12h()

    # Simplified data for the next 12 hours:
    >>> weather2.next_12h_simplified()
    
    Sample url to get sky condition icons:
    https://openweathermap.org/img/wn/10d@2x.png
    
    """
    def __init__(self, apikey, city=None, lat=None, lon=None) :
        if city :
            self.url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=imperial"
            r = requests.get(self.url)
            self.data = r.json()
        elif lat and lon :
            self.url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=imperial"
            r = requests.get(self.url)
            self.data = r.json()
        else :
            raise TypeError("Provide either city or lat and lon!")  

        if self.data["cod"] != "200" :
            raise ValueError(self.data["message"])         

    def next_12hr(self) :
        """Returns 3-hour data for the next 12 hours as a dict.
        """
        return self.data['list'][:4]
    
    def next_12h_simplified(self) :
        """Returns date, temperature, and sky condition every 3 hours
        for the next 12 hours as a tuple of tuples.
        """
        simple_data = []
        for dicty in self.data['list'][:4] :
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description'], dicty['weather'][0]['icon']))
        return simple_data