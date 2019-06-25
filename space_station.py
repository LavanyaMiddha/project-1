import urllib.request, urllib.parse, urllib.error
import json
import time, calendar, datetime
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


#http://api.open-notify.org/astros.json
url=input("Enter URL")
data=urllib.request.urlopen(url).read()
info=json.loads(data)
people=info['people']
names=[]
for x in people:
    names.append(x['name'])
print("Name of the people on the ship are:")
for y in names:
    print(y)
print()

#http://api.open-notify.org/iss-now.json
url=input("Enter URL")
data=urllib.request.urlopen(url).read()
info=json.loads(data)
pos=info['iss_position']
for x in pos:
    lat=pos['latitude']
    lon=pos['longitude']
print(lat)
print(lon)

#https://matplotlib.org/basemap/users/examples.html

m=Basemap(llcrnrlon=-160, llcrnrlat=-75,urcrnrlon=160,urcrnrlat=80)
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
m.drawcoastlines(linewidth=0.1, color="white")
m.plot(lat,lon,linestyle='none',marker='o',markersize=16,alpha=0.6,c='orange',markeredgecolor='black',markeredgewidth=1)
plt.title('Location of ISS ')
