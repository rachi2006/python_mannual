from django.shortcuts import render
import requests

def home(request):

    weather_data = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")

        api_key = "4e814330ff2e49ccbd684f7a5a93defb"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            error = "City not found or API problem"
        else:
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }

    return render(request, "home.html", {"weather": weather_data, "error": error})