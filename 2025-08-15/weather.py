import requests

class Weather:
    def __init__(self, token, lat, lon):
        self.lat = lat
        self.lon = lon
        self.my_token = token

    def get_weather(self):
        url = f'https://api.openweathermap.org/data/2.5/weather?appid={self.my_token}&units=metric&lang=ru'
        r = requests.get(url, params={'lat':self.lat,'lon':self.lon})
        # //lat = 56.8431  lon = 60.6454
        return(r.json())

    def format_weather(self):
        data = self.get_weather()
        city = data['name']
        temp = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        tek = f'{city}: {temp}°C, ощущается как {feels_like}°C'
        return tek


user_lat = float(input('Введи широту: '))
user_lon = float(input('Введи долготу: '))
token = 'dsds'

weather = Weather(token, user_lat, user_lon)
print(weather.format_weather())


