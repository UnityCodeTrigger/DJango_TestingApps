import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):

    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    cities = City.objects.all()
    weatherData = []

    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid=6839fe55987ea2bb41a9ecf1cffaf36f'
        weatherRequest = requests.get(url).json()
        city_weather = {
            "CityName" : city.name,
            "Temp" : weatherRequest["main"]["temp"],
            "Hum" : weatherRequest["main"]["humidity"],
            "Desc" : weatherRequest["weather"][0]["description"],
            "Icon" : weatherRequest["weather"][0]["icon"],
        }
        weatherData.append(city_weather)

    context =  {"weatherData" : weatherData, "form" : form}
    return render(request, 'weather/weather.html', context)