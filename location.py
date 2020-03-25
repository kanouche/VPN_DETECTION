import ipinfo
import pandas as pd
import csv

access_token = '67315bd63bab1c'
handler = ipinfo.getHandler(access_token)

df = pd.read_csv("vpn-netflow.csv")
ip = df.SrcIP

latitude = []
longitude = []

for value in ip:
	response = handler.getDetails(value)
	latitude.append(response.latitude)
	longitude.append(response.longitude)

myFile = open('output.csv', 'w')
with myFile:
   writer = csv.writer(myFile, delimiter=',')
   for i in range(0, len(latitude)):
   	if(latitude[i] is None or longitude[i] is None):
   		writer.writerow(("NA", "NA"))
   	else:
   		writer.writerow((latitude[i], longitude[i])) 