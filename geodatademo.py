#Import all the required libraries
import urllib.request as ur
import urllib.parse as uren
import sqlite3
import json
import time
import ssl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
scontext = None

# Define the Lists required for storing the data.
latitude = []
longitude = []
final_name = []

# Read the file which contains the locations. The number of locations should not exceed 200 or else the program quits.
fh = open("test.txt")
count = 0

for line in fh:
    if count > 200 : break
    address = line.strip()
    print (address)

#Create the URL to send request to the API.
    print ('Resolving', address)
    url = serviceurl + uren.urlencode({"sensor":"false", "address": address})
    print ('Retrieving', url)
    
#Read the received data from the API. Convert the data to JSON format. In case the conversion fails, exit with error message.     
    uh = ur.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data)) #,'characters',data[:20].replace('\n',' '))
    count = count + 1
    try: 
        js = json.loads(data.decode())
    except:
        print ("Error")
        break

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print ('==== Failure To Retrieve ====')
        break

#Perform data mining on the data to retrieve only the latitude, longitude and name. Append the data to the respective lists.
    lat = (js['results'])
    lat_1 = lat[0]
    lat_2 = lat_1['geometry']
    lat_3 = lat_2['location']
    name = lat_1['address_components']
    final = name[0]
    latitude.append(lat_3['lat'])
    longitude.append(lat_3['lng'])
    final_name.append(final['long_name'])

# At this point we will have the necessary 3 Lists ready. These work as inputs to the next step.
print(latitude)
print(longitude)
print(final_name)

fig = plt.figure()

# we define the basic parameters for the map.
themap = Basemap(projection='gall',
        llcrnrlon = -100,              # lower-left corner longitude
        llcrnrlat = 0,               # lower-left corner latitude
        urcrnrlon = 100,               # upper-right corner longitude
        urcrnrlat = 90,               # upper-right corner latitude
        resolution = 'l',
        area_thresh = 100000.0,
        )
    
#draw the country boundaries and coastlines with land having grey color and water bodies having steel blue color
themap.drawcoastlines()
themap.drawcountries()
themap.fillcontinents(color = 'gainsboro')
themap.drawmapboundary(fill_color='steelblue')

#Plot the data points    
x, y = themap(longitude, latitude)
themap.plot(x, y, 
    'bo',                    # marker shape
    color='Indigo',         # marker colour
    markersize=8            # marker size
    )

#Plot the data point labels
for label, xpt, ypt in zip(final_name, x, y):
    plt.text(xpt, ypt, label)

plt.show()
