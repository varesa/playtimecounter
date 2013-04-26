#!/usr/bin/env python

import time
import math

print("Counting time")

f = open('peliajat')
lines = [line.strip() for line in f.readlines()]
f.close()

totaltime = 0

oldtime   = 0

for line in lines:

	newtime = time.strptime(line[:19], "%Y-%m-%d %H:%M:%S")

	if "connecting" in line:
		print("connecting")
	
	elif "lost con" in line:
		print("disconnect")
		if oldtime > 0:
			timespent = time.mktime(newtime) - time.mktime(oldtime)
			
			h = math.floor(timespent / 3600)
			m = math.floor((timespent - h*3600) / 60)
			s = timespent - h*3600 - m*60
			
			print("h: " + str(h) + ", m: " + str(m) + ", s: " + str(s))

			totaltime += timespent

	oldtime = newtime


h = math.floor(totaltime / 3600)
m = math.floor((totaltime - h*3600) / 60)
s = totaltime - h*3600 - m*60

print("Total:\nh: " + str(h) + ", m: " + str(m) + ", s: " + str(s))
