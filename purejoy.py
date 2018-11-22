import pygame
import numpy as np
import os
from urllib.request import urlopen

link = "https://espenvh.wixsite.com/gamedev"
print ("Parsing info online:")
print()
try:#getting info online
	f = urlopen(link)
	myfile = f.read()
	myfile =str(myfile)

	for x in range(1000,1999):
		searchstring="Release"+ (str(x)[1:])

		str1 = myfile
		str2 = searchstring
		str3 = "</span>"

		loc= (str1.find(str2))
		#if x==1900: print()
		str2= str1[loc:loc+111]
		if len(str2)>5:print (str2[:str2.find(str3)])

	for x in range(10000,11999):
		searchstring="Release"+ (str(x)[1:])

		str1 = myfile
		str2 = searchstring
		str3 = "</span>"

		loc= (str1.find(str2))
		#if x==1900: print()
		str2= str1[loc:loc+111]
		if len(str2)>5:print (str2[:str2.find(str3)])


	
except:
	print ("""no info found online
	       no info at all""")



main_dir = os.path.split(os.path.abspath(__file__))[0]
music_dir=main_dir+"\\release901"

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(main_dir) if isfile(join(main_dir, f))]

print()
print ("Console version 01.02(nov 22) running in consoledir: ")
print (main_dir,onlyfiles)


d = '.'
d=([os.path.join(d, o) for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))])

print (d)
maxrelease=""
for x in d:
	xstr=x[-3:]
	try:
		if int(xstr)>700:
			break
	except:
		print("What is git doing here?")
	maxrelease=xstr

maxrelease=".\\\\Release"+maxrelease
print ("Latest release:",(maxrelease))

import sys
sys.path.insert(0, maxrelease)
print (sys.path[0:3])





print ("Music:")
try:
	onlyfiles = [f for f in listdir(music_dir) if isfile(join(music_dir, f))]
	print (music_dir,[(x[-3:]) for x in onlyfiles])
except:
	print ("Oh no. No music packs downloaded.")




print()

print ("Searching for joysticks:")
pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

for joystick in joysticks:
  joystick.init() 
  #print (joystick.get_numbuttons())
  print (joystick.get_name())
  



buttontext= ["Select"],[""],[""],["Start"],["Digital Up"],["Digital Right"],["Digital Down"],["Digitial Left"],["L2"],["R2"],["R1"],["L1"],["Triangle"],["Circle"],["X"],["Square"],["PS"],[""],[""]
joystick = pygame.joystick.Joystick(0)
joystick.init() 
numaxes = joystick.get_numaxes() # return the number of axes on the controller
axis = [joystick.get_axis(i) for i in range(numaxes)] # get the analog value of the specified axis 
#print (numaxes)
sumaxis = np.array([joystick.get_axis(i) for i in range(numaxes)]) # get the analog value of the specified axis 
#print (axis)
#print (sumaxis)
#print (joystick.get_numbuttons())
#print (joystick.get_name())


joystick = pygame.joystick.Joystick(1)
joystick.init() 
numaxes = joystick.get_numaxes() # return the number of axes on the controller
axis = [joystick.get_axis(i) for i in range(numaxes)] # get the analog value of the specified axis 
#print (numaxes)
sumaxis = np.array([joystick.get_axis(i) for i in range(numaxes)]) # get the analog value of the specified axis 
#print (axis)
#print (sumaxis)
#print (joystick.get_numbuttons())
#print (joystick.get_name())


import game

print ()
game.run(main_dir)
print("Bye! Bye! Bye! Bye! Bye!")