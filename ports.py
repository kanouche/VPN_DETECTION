import pandas as pd
import csv


df = pd.read_csv("vpn-netflow.csv",low_memory=False)
srcPorts = df.SrcPort
dstPorts = df.DstPort

src = []
dst = []

# 0: Well-known ports range from 0 through 1023. 
# 1: Registered ports are 1024 to 49151. 
# 2: Dynamic ports (also called private ports) are 49152 to 65535. 
# 3: Other ports..

for value in srcPorts:
	if(value >=0 and value <= 1023):
		src.append(0);
	elif(value >=1024 and value <= 49151):
		src.append(1);
	elif(value >= 49152 and value <= 65535):
		src.append(2);
	else:
		src.append(3);

for value in dstPorts:
	if(value >=0 and value <= 1023):
		dst.append(0);
	elif(value >=1024 and value <= 49151):
		dst.append(1);
	elif(value >= 49152 and value <= 65535):
		dst.append(2);
	else:
		dst.append(3);

myFile = open('output.csv', 'w')
with myFile:
   writer = csv.writer(myFile, delimiter=',')
   jçi=0
   for i in range(0, len(src)):
   	writer.writerow((src[i], dst[i])) 