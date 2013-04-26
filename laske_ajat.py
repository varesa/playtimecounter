#!/usr/bin/env python

import time
import math

print("Counting time")

f = open('peliajat')
lines = [line.strip() for line in f.readlines()]
f.close()

state     = ""
totaltime = 0

linetime  = 0
oldtime   = 0

for line in lines:

	newtime = time.strptime(line[:19], "%Y-%m-%d %H:%M:%S")

	if "connecting" in line:
		print("connecting")
		state = "c"
	
	elif "lost con" in line:
		print("disconnect")
		if state is "c" and oldtime > 0:
			timespent = time.mktime(newtime) - time.mktime(oldtime)
			
			h = math.floor(timespent / 3600)
			m = math.floor((timespent - h*3600) / 60)
			s = timespent - h*3600 - m*60
			
			print("h: " + str(h) + ", m: " + str(m) + ", s: " + str(s))

			totaltime += timespent

		
		state = "d"
	oldtime = newtime


h = math.floor(totaltime / 3600)
m = math.floor((totaltime - h*3600) / 60)
s = totaltime - h*3600 - m*60

print("Total:\nh: " + str(h) + ", m: " + str(m) + ", s: " + str(s))
