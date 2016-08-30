import math

R=6371

lat1=math.radians(39.9)
lng1=math.radians(116.4)
lat2=math.radians(25.1)
lng2=math.radians(102.4)

# lat1=30
# lng1=60
# lat2=60
# lng2=90

ret=math.cos(lat1)*math.cos(lat2)*math.cos(lng2-lng1)+math.sin(lat1)*math.sin(lat2)
print(ret)
phi=math.acos(ret)
print(phi*R)
