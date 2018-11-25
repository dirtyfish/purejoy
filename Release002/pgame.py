
import pygame, os, random, math, copy
from pygame.locals import *
import numpy as np


def main():
	run("..")

def run(main_dir):
	print ("GameRelease002 Running!")

	screenw=1024
	screenh=768
	#fieldw=1024/2-48
	fieldw=7*64
	#fieldh=768/2
	fieldh=6*64
	fieldr=1024/2+63
	fieldd=768/2
	rotation=[-1,-1]
	stopevent = QUIT

	upcli="c:/windows/fonts/upcli.ttf" 
	pygame.init()
	mainClock = pygame.time.Clock()

	screen = pygame.display.set_mode((screenw, screenh), 1)
	frame=0
	fontsize=25
	black = (0,0,33) 
	blue=(0,0,200)
	try:
		pygame.mixer.music.load(main_dir+'\\release901\\8 - hate.mp3')
		pygame.mixer.music.play(0, 0)
	except:
		print("Music does not load.")


	while 1:
		frame+=1
		screen.fill(black)
		if 1:
			screen.fill((100,133,100))
			font=pygame.font.Font(upcli,fontsize*2)
			pos=0
			for x in "RobOTSCHOLl":


			  pos+=30;
			  text= font.render(x, True, blue)
			  screen.blit(text, [320+pos,150+50*math.sin((pos+frame*2-2)*0.05)])
			
			screen.blit(text, [420,150+50*math.sin((frame-2)*0.05)])
			font=pygame.font.Font(upcli,fontsize)
			text= font.render("PRESS SPACE", True, blue)
			screen.blit(text, [466,350+50*math.sin((frame*2/3-2)*0.05)])
			text= font.render("PRESS I FOR INSTRUCTION", True, blue)
			screen.blit(text, [400,450+50*math.sin((frame*2/4-2)*0.05)])
			text= font.render("PRESS F FOR FULLSCREEN", True, blue)
			screen.blit(text, [400,550+50*math.sin((frame*3/5-2)*0.05)])
		for e in pygame.event.get():

			
				if e.type == stopevent:
					return
		pygame.display.flip()
		mainClock.tick(40)

if __name__ == '__main__': main()
pygame.quit()





	#pygame.mixer.music.load('Power tools.mp3')
    #pygame.mixer.music.play(0, 0)
    
    
    
    
