import urllib.request as ur
import urllib.parse as uren
import sqlite3
import json
import time
import ssl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# If you are in China use this URL:
# serviceurl = "http://maps.google.cn/maps/api/geocode/json?"
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
scontext = None

#conn = sqlite3.connect('geodatademo.sqlite')
#cur = conn.cursor()

#cur.execute('''
#CREATE TABLE IF NOT EXISTS Locations (address TEXT, latitude TEXT, longitude)''')

latitude = []
longitude = []
final_name = []

fh = open("test.txt")
count = 0
for line in fh:
    if count > 200 : break
    address = line.strip()
    print (address)

    print ('Resolving', address)
    url = serviceurl + uren.urlencode({"sensor":"false", "address": address})
    print ('Retrieving', url)
    uh = ur.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data)) #,'characters',data[:20].replace('\n',' '))
    count = count + 1
    try: 
        js = json.loads(data.decode())
    except:
        print ("yes")
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print ('==== Failure To Retrieve ====')
        break

    lat = (js['results'])
    lat_1 = lat[0]
    lat_2 = lat_1['geometry']
    lat_3 = lat_2['location']
    name = lat_1['address_components']
    final = name[0]
    latitude.append(lat_3['lat'])
    longitude.append(lat_3['lng'])
    final_name.append(final['long_name'])

print(latitude)
print(longitude)
print(final_name)

fig = plt.figure()
themap = Basemap(projection='gall',
        llcrnrlon = -100,              # lower-left corner longitude
        llcrnrlat = 0,               # lower-left corner latitude
        urcrnrlon = 100,               # upper-right corner longitude
        urcrnrlat = 90,               # upper-right corner latitude
        resolution = 'l',
        area_thresh = 100000.0,
        )
    
themap.drawcoastlines()
themap.drawcountries()
themap.fillcontinents(color = 'gainsboro')
themap.drawmapboundary(fill_color='steelblue')
    
x, y = themap(longitude, latitude)
themap.plot(x, y, 
    'bo',                    # marker shape
    color='Indigo',         # marker colour
    markersize=8            # marker size
    )

for label, xpt, ypt in zip(final_name, x, y):
    plt.text(xpt, ypt, label)
plt.show()
