from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
  
  
def index(request):
    if request.method == 'POST':
        city = request.POST['city']  
        # source contain JSON data from API
  
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a0bbee999e9fca2dd5234784dfe5f8b6&units=metric').read()
  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
  
        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": (str(list_of_data['main']['temp'])),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "feels_like": str(list_of_data['main']['feels_like']),
          "min_temp": str(list_of_data['main']['temp_min']),
          "max_temp": str(list_of_data['main']['temp_max']),
            "city_name": str(list_of_data['name']),
        }
        print(data)
    else:
        data ={}
    return render(request, "main/index.html", data)