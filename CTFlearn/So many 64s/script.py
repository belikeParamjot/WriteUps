from base64 import *
	
f = open("flag.txt","r")
message = f.read()
f.close()
count=0
try:
	while 1:
		message = b64decode(message)
		count+=1
except:
	print message
	print count

