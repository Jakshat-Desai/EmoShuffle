#!/usr/bin/python2

import commands as sp

f=open('/music/current_emotions.txt','r')

content=(f.read()).split("\n")

f.close()

dominating_emotion="H"
num=0.0

g=open("/music/user_data.csv","a+")

for i in content:
	e=i[0]
	if e=="N":
		continue
	x=float(i[-5:])
	g.write(str(x)+",")
	if x>num:
		num=x
		dominating_emotion=e

dt=sp.getoutput("date")
day=dt[0:3]
time=dt[-17:-9]

g.write(time+","+day+"\n")
g.close()

if dominating_emotion=="S":
	dominating_emotion="Sad"
elif dominating_emotion=="H":
	dominating_emotion="Happy"
elif dominating_emotion=="F":
	dominating_emotion="Fear"
elif dominating_emotion=="A":
	dominating_emotion="Angry"

sp.getoutput("xpra start --start-child='find /music/soundimage/"+dominating_emotion+"/ -type f -exec vlc --one-instance --playlist-enqueue --playlist-autostart --fullscreen -Z '{}' +' --html=on --dpi=100 --bind-tcp=0.0.0.0:3333 --systemd-run=no")
