import pyowm
city = str(input("Enter city: "))
owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')
observation = owm.weather_at_place(city)
w = observation.get_weather()
print ("in the " ,city,"weather is ", w, w.get_humidity() )