x="xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
y="h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"

dumpx = x.decode('base64').encode('hex')
dumpy = y.decode('base64').encode('hex')

flag_dump = hex(int(dumpx,16) ^ int(dumpy,16)).rstrip("L").lstrip("0x")

print flag_dump.decode('hex')
