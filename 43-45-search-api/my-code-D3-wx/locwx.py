import requests
from geopy import geocoders

g = geocoders.GoogleV3(api_key='AIzaSyCVKQVwckpcGEYmpZvazgztyFO0KxMs5Vs')
DARK_SKY_API_KEY = "f4407da6eafeb55869cdb6055591d6f5"

print(f"\n*********** Location Weather *****************\n")

#create an input address string
inputAddress = input("Enter a location: \n")

#do the geocode
location = g.geocode(inputAddress, timeout=1)

#some things you can get from the result
# print(location.latitude, location.longitude)
# pprint.pprint(location.address)

lat = str(location.latitude)
long = str(location.longitude)
address = location.address
# print("test coords: ", lat, long)

# request wx for given lat:long coords using darksky api
r = requests.get("https://api.darksky.net/forecast/"+DARK_SKY_API_KEY+"/"+lat+","+long+"?lang=en&units=si&exclude=daily,hourly,flags,offset")
dswx = r.json()

knot_c = dswx['currently']['windSpeed'] * 1.94
knots = str(round(knot_c, 1))

print("\nThe wind in", address, "is currently", knots + " kts, and the direction is coming from " + str(dswx['currently']['windBearing']) + " degrees.")
print("Set the altimeter to: ", round(dswx['currently']['pressure']), "HPa")
genwx = dswx['currently']['icon']
print("It's a", genwx, "today!")