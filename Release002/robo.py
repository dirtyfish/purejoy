#!/usr/bin/env python
#AI assignment 4

#The program will search 70 alternative setups 
#
#give each alternative a score and chose best option.
#The goal is to drive one car to the goal.

import pygame, os, random, math, copy
from pygame.locals import *
from math import sin

main_dir = os.path.split(os.path.abspath(__file__))[0]


frameadd=1
black = (0,0,33) 
red = (255,0,0) #red
green = (0,255,0) 
blue = (0,123,123) 
screenw=1024
screenh=768
#fieldw=1024/2-48
fieldw=7*64
#fieldh=768/2
fieldh=6*64
fieldr=1024/2+63
fieldd=768/2
rotation=[-1,-1]

upcli="c:/windows/fonts/upcli.ttf"   ##seems to work for me
fontsize=44


print (fieldw/64,fieldh/64)
print (fieldw,fieldh)
#black=0x000000
#black=66

randomset = [0,1,1,1,2,3,4,5,6]
instructions= ['UP','LEFT','DOWN','RIGHT','TURN LEFT','TURN RIGHT']

imagenamel=['instruction_up_cropped_96.tga']
imagenamel.append('instruction_left_cropped_96.tga')
imagenamel.append('instruction_down_cropped_96.tga')
imagenamel.append('instruction_right_cropped_96.tga')
imagenamel.append('instruction_turnleft_cropped_96.tga')
imagenamel.append('instruction_turnright_cropped_96.tga')
imagenamel.append('sky.png')
imagenamel.append('floor.jpg')
imagenamel.append('instruction_turnright_cropped_96.tga')
imagenamel.append('rs_title_c_32.tga')

tilenamel=['white.jpg','bluegrey.jpg','pattern.jpg','start.jpg','goal.jpg','car.tga','car2.tga']
tilelist=[]
imagenamelist=[]
bitmaplist=[]
avgcolorlist=[]


def searchrange(levels):
 for x in range(1<<levels):
  #print " ",x," ",
  xx=x
  count=0
  result=[]
  for y in range(levels,0,-1):
    yy=xx>>y-1
    yy%=2
    count+=yy
    #print yy,
    result.append(yy)
  #print count,
  if count==levels/2:
    yield result

def splitlist(getlist,sortlist):
  result=[[],[]]
  for x in range(len(getlist)):
    result[sortlist[x]].append(getlist[x])
  return result


def main():
    carpos=[[4,4],[4,4]]
    goalpos=[[11,15],[11,15]]
    lookx=0
    looky=0
    lookx2=0
    looky2=0
    decks=[[],[]]
    frameadd=1
    room=0
    pygame.init()
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((screenw, screenh), HWSURFACE|DOUBLEBUF)

    if 1:
        for imagename in imagenamel:
    
          fullimagename= os.path.join(main_dir, 'IMAGES',imagename)
          bitmap = pygame.image.load(fullimagename)      
          imagenamelist.append(fullimagename)
          bitmaplist.append(bitmap)

        for imagename in tilenamel:
    
          fullimagename= os.path.join(main_dir, 'IMAGES',imagename)
          bitmap = pygame.image.load(fullimagename)      
          imagenamelist.append(fullimagename)
          tilelist.append(bitmap)

    #print imagenamelist
    #print bitmaplist[7].get_size()
    bitmaplist[7].blit(tilelist[3], (64*3, 64*3), (0, 0, 64,64))
    for x in range(9):
      bitmaplist[7].blit(tilelist[x%2], (64*(x%3), 64*(x/3)), (0, 0, 64,64))
    for x in range(9):
      bitmaplist[7].blit(tilelist[x%2], (64*(x%3+8), 64*(x/3+8)), (0, 0, 64,64))
    for x in range(9):
      bitmaplist[7].blit(tilelist[x%2], (64*(x%3+2), 64*(x/3+5)), (0, 0, 64,64))
    for x in range(9):
      bitmaplist[7].blit(tilelist[x%2], (64*(x%3+11), 64*(x/3+15)), (0, 0, 64,64))

    bitmaplist[7].blit(tilelist[4], (64*10, 64*14), (0, 0, 64,64))
    bitmaplist.append(pygame.transform.scale(bitmaplist[7],(448,384)))
    #print len(bitmaplist)
    #print bitmaplist[10].get_size()

  
    #get the image and screen in the same format
    if screen.get_bitsize() == 8:
        screen.set_palette(bitmap.get_palette())
    else:
        bitmap = bitmap.convert()

    #prep some variables
    anim = 0.0



   
    stopevent = QUIT
    #print stopevent
    frame=0

    if 1:

    # set up music'background.mid'
            #pickUpSound = pygame.mixer.Sound('pickup.wav')
            pygame.mixer.music.load('Power tools.mp3')
            pygame.mixer.music.play(0, 0)
            #pygame.mixer.music.play(0, 0.5)
            
    
 #mainloop ##################################################################################
    while 1:
        frame+=frameadd
        screen.fill(black)
       



        if room<2:
            posx=0
            for bitmap in bitmaplist:
                
                adposx=posx+frame*2
                adposx%=screenh+96
                adposx-=96
                screen.blit(bitmap, (screenw/2-48, adposx), (0, 0, 96,96))
                posx+=96

            for bitmap in tilelist:
                
                adposx=posx+frame*2
                adposx%=screenh+96
                adposx-=96
                screen.blit(bitmap, (screenw/2-48, adposx), (0, 0, 96,96))
                posx+=64


        #pygame.draw.rect(screen, blue, [0,0,fieldw,fieldh], 2)
        #pygame.draw.rect(screen, blue, [0,0,64,64], 2)
        #pygame.draw.rect(screen, blue, [0,0,32,32], 2)
        if room==0:
            pygame.draw.rect(screen, blue, [0,fieldd,fieldw,fieldh], frame%2*5+1)
            pygame.draw.rect(screen, blue, [fieldr,0,fieldw,fieldh], frame%2+1)
            pygame.draw.rect(screen, blue, [fieldr,fieldd,fieldw,fieldh], frame%2+1) 

            screen.blit(bitmaplist[7], (0, fieldd), (frame, 0, fieldw,fieldh)) 
            screen.blit(bitmaplist[7], (0, 0), (0, frame, fieldw,fieldh)) 
            screen.blit(bitmaplist[7], (fieldr, 0), (frame, frame, fieldw,fieldh)) 
            screen.blit(bitmaplist[7], (fieldr, fieldd), (frame, 100.0*math.sin(frame/100.0), fieldw,fieldh)) 

            screen.blit(bitmaplist[0], (0, fieldd), (-frame, 0, fieldw,fieldh)) 
            screen.blit(bitmaplist[4], (fieldr, fieldd), (-frame, -frame*0.5, fieldw,fieldh)) 
            screen.blit(bitmaplist[2], (0, 0), (-frame, -100.0*math.sin(frame/100.0), fieldw,fieldh))
            if frame>40:
                pygame.mixer.music.play(0, 0)
                room=1

        if room==1:
            pygame.draw.rect(screen, blue, [0,fieldd,fieldw,fieldh], frame%2*5+1)
            pygame.draw.rect(screen, blue, [fieldr,0,fieldw,fieldh], frame%2+1)
            pygame.draw.rect(screen, blue, [fieldr,fieldd,fieldw,fieldh], frame%2+1) 
            if frame>80:
                room=2
                frame=200
                #pygame.mixer.music.load('Power tools.mp3')
                pygame.mixer.music.play(0,0)

        if room==2:
            screen.fill((100,133,100))
            #bitmaplist[8].set_colorkey((255,255,255),0)
            #bitmaplist[8].set_alpha(255)
            #screen.blit(bitmaplist[9], (200, 0), (0, 0, 999,999)) 

            font=pygame.font.Font(upcli,fontsize*2)
           

            text= font.render("ROBOT SCHOOL", True, blue)
            screen.blit(text, [320,150+50*math.sin((frame*2-2)*0.05)])


            font=pygame.font.Font(upcli,fontsize)
            
            text= font.render("AI ASSIGNMENT 04", True, blue)
            screen.blit(text, [420,150+50*math.sin((frame-2)*0.05)])

            font=pygame.font.Font(upcli,fontsize)
            
            text= font.render("PRESS SPACE", True, blue)
            screen.blit(text, [466,350+50*math.sin((frame*2/3-2)*0.05)])

            text= font.render("PRESS I FOR INSTRUCTION", True, blue)
            screen.blit(text, [400,450+50*math.sin((frame*2/4-2)*0.05)])

            text= font.render("PRESS F FOR FULLSCREEN", True, blue)
            screen.blit(text, [400,550+50*math.sin((frame*3/5-2)*0.05)])

            




            for e in pygame.event.get():
              if e.type == KEYDOWN:
                if e.key == ord(' '):
                  room=3
                  frame=500
                  pygame.mixer.music.fadeout(2999)
                if e.key == ord('i'):
                  room=4
                if e.key == ord('f'):
                  screen = pygame.display.set_mode((screenw, screenh), HWSURFACE|DOUBLEBUF|FULLSCREEN)
                if e.key == ord('w'):
                  screen = pygame.display.set_mode((screenw, screenh), HWSURFACE|DOUBLEBUF)
                                    
              if e.type == stopevent:
                return

        if room==4:
            screen.fill((100,133,100))
            #bitmaplist[8].set_colorkey((255,255,255),0)
            #bitmaplist[8].set_alpha(255)
            #screen.blit(bitmaplist[9], (200, 0), (0, 0, 999,999)) 

            font=pygame.font.Font(upcli,fontsize*2)
           

            text= font.render("INSTRUCTIONS", True, blue)
            screen.blit(text, [320,150+50*math.sin((frame*2-2)*0.05)])


            font=pygame.font.Font(upcli,fontsize)
            
            #text= font.render("AI ASSIGNMENT 04", True, blue)
            #screen.blit(text, [420,150+50*math.sin((frame-2)*0.05)])

            font=pygame.font.Font(upcli,fontsize)
            
            text= font.render("PRESS SPACE", True, blue)
            screen.blit(text, [466,350+50*math.sin((frame*2/3-2)*0.05)])

            text= font.render("YOU WILL CONTROL TWO ROBOTS", True, blue)
            screen.blit(text, [400,450+50*math.sin((frame*2/4-2)*0.05)])

            text= font.render("A - LEFT, D - RIGHT, C-CHEAT", True, blue)
            screen.blit(text, [400,550+50*math.sin((frame*2/4-2)*0.05)])

            




            for e in pygame.event.get():
              if e.type == KEYDOWN:
                if e.key == ord(' '):
                  room=3
                  frame=500
                  pygame.mixer.music.fadeout(2999)
                if e.key == ord('2'):
                  room=3
                  frame=500
                  #pygame.mixer.music.load('Power tools.mp3')
                  pygame.mixer.music.play(0, 0.5)
              if e.type == stopevent:
                return

        if room==3:
            screen.fill((00,133,100))
            if frame<600:
            
              font=pygame.font.Font(upcli,fontsize*2)
              text= font.render("START", True, black)
              text=pygame.transform.rotate(text,10);
              screen.blit(text, [420,150+50*math.sin((frame*2-2)*0.05)])

            else:
                room=5
                frame=0

            
            
            #pygame.mixer.music.stop()
            #pygame.mixer.pause()

            for e in pygame.event.get():
              
              if e.type == stopevent:
                return


        if room==5:
            if frame==0:
                selcarddir=0
                cardlist=[]
                carddir=[]
                cards=8
                cardsleft=cards
                totdir=0
                for x in range(cards):
                    cardlist.append(randomset[random.randint(1,8)])
                    carddir.append(0)




                #print "cardlist:",cardlist

            screen.fill((55,133,33))
            screen.blit(bitmaplist[7], (0, fieldd), (lookx, looky, fieldw,fieldh)) 
            screen.blit(bitmaplist[10], (0, 0), (0, 0, fieldw,fieldh)) 
            screen.blit(bitmaplist[10], (fieldr, 0), (0, 0, fieldw,fieldh)) 
            screen.blit(bitmaplist[7], (fieldr, fieldd), (lookx2, looky2, fieldw,fieldh)) 

            screen.blit(tilelist[5],(3*64,fieldd+3*64))
            screen.blit(tilelist[6],(fieldr+3*64,fieldd+3*64))

            #screen.blit(bitmaplist[0], (0, fieldd), (-frame, 0, fieldw,fieldh)) 
            #screen.blit(bitmaplist[4], (fieldr, fieldd), (-frame, -frame*0.5, fieldw,fieldh)) 
            #screen.blit(bitmaplist[2], (0, 0), (-frame, -100.0*math.sin(frame/100.0), fieldw,fieldh))

            posx=0
            adposy=0
            
            nrcard=cards
            for card in cardlist:

                nrcard-=1
                bitmap=bitmaplist[card-1]
                adposx=posx+frame*1-200
                #adposx%=screenh+96
                adposx-=96

                if adposx==673 and frameadd==2:
                    adposx=672
                    frameadd=1
                if adposx==672:#decide direction
                    frameadd=1
                    if totdir==cardsleft:
                        selcarddir=-1
                    if totdir==-cardsleft:
                        selcarddir=1

                    #if selcarddir==0:
                      #selcarddir=nrcard%2*2-1

                    carddir[nrcard]=selcarddir
                    cardsleft-=1
                    totdir+=selcarddir
                    if cardsleft==0:
                        room=6
                        frame=0
                        


                if adposx>672:#card changes direction
                   
                    adposy=adposx-672
                    adposx=672
                
                try:
                  if carddir[nrcard]==0:
                    carddir[nrcard]=nrcard%2*2-1
                    totdir+=nrcard%2*2-1
                except:
                  print (nrcard," is out of range -",carddir)

                screen.blit(bitmap, (screenw/2-48+adposy*(carddir[nrcard]), adposx), (0, 0, 96,96))
                #font=pygame.font.Font(upcli,fontsize*2/3)
                #text= font.render(str(card), True, (255,255,255))
                #text= font.render(str(totdir), True, (255,255,255))
                #screen.blit(text, [screenw/2-48+adposy*(carddir[nrcard])+5, adposx+5])
                #if frame>=48:
                 #   frame=48

                posx+=96
                for e in pygame.event.get():
                  if e.type == KEYDOWN:
                    if e.key == ord('a'):
                        selcarddir=-1
                        frameadd=2
                    if e.key == ord('d'):
                        selcarddir=1
                        frameadd=2
                    if e.key == ord('s'):
                        frameadd=2
                    if e.key == ord('w'):
                        screen = pygame.display.set_mode((screenw, screenh), HWSURFACE|DOUBLEBUF)
                    if e.key == ord('f'):
                        screen = pygame.display.set_mode((screenw, screenh), HWSURFACE|DOUBLEBUF|FULLSCREEN)

                    if e.key == ord('c'):
                        count=0
                        bestscore=-99999
                        savemyx=[]
                        for x in searchrange(8):
                          count+=1
                          #print count,x, splitlist(cardlist,x),
                          vcards=splitlist(cardlist,x)
                          vrotation=copy.deepcopy(rotation)
                          vcarpos=copy.deepcopy(carpos)
                          vcards[0].reverse()
                          vcards[1].reverse()

                          score=0
                          vcar=0
                          for xx in vcards:
                            for y in xx:
                              if y==5:
                                vrotation[vcar]+=1
                              else:
                                if y==6:
                                  vrotation[vcar]-=1
                                else:
                                  if y<5:
                                    if (y+vrotation[vcar])%4==1:
                                      vcarpos[vcar][1]-=1
                                      score-=1
                                    if (y+vrotation[vcar])%4==2:
                                      vcarpos[vcar][0]-=1
                                      score-=1
                                    if (y+vrotation[vcar])%4==3:
                                      vcarpos[vcar][1]+=1
                                      score+=1
                                    if (y+vrotation[vcar])%4==0:
                                      vcarpos[vcar][0]+=1
                                      score+=1
                            vcar+=1

                          #for vrot in vrotation:
                           # if vrot==0 or vrotation==3:
                            #  score+=200
                              #print"good rotation"

                          score*=10
                          score+=random.randint(1,9)
                          score-=100*abs(vcarpos[0][0]-goalpos[0][0])+abs(vcarpos[0][1]-goalpos[0][1])
                          score-=100*abs(vcarpos[1][0]-goalpos[1][0])+abs(vcarpos[1][1]-goalpos[1][1])
                          score+=10000*(vcarpos[0][0]==goalpos[0][0] and carpos[0][1]==goalpos[0][1])
                          score+=10000*(vcarpos[1][0]==goalpos[1][0] and carpos[1][1]==goalpos[1][1])

                          if score>bestscore:
                            bestscore=score
                            #print "---------------x",vcards,score,x, vcarpos, vrotation
                            #print "-------------car1", abs(vcarpos[0][0]-goalpos[0][0])+abs(vcarpos[0][1]-goalpos[0][1])
                            #print "-------------car2", abs(vcarpos[1][0]-goalpos[1][0])+abs(vcarpos[1][1]-goalpos[1][1])
                            savemyx=copy.deepcopy(x)
                          #else:
                            #print "---------x",vcards,score






                          #print vrotation

                        
                        if 1:
                          carddir=[]
                          for y in savemyx:
                            carddir.append(y*2-1)
                          #print "sending:",savemyx,carddir
                          

                          carddir.reverse()



                          




                        room=6
                        frame=0
                  if e.type == stopevent:
                      return
                  
                  
            

        if room==6:

            if frame==0:
                if carpos[0]==goalpos[0] or carpos[1]==goalpos[1]:
                    #print"you are done"
                    room=7
                
                frameadd=1
                rotationcountdown=[0,0]
                decks=[[],[]]
                carddir.reverse()
                for x in range(cards):
                  if carddir[x]==1:
                    decks[1].append(cardlist[x])
                  else:
                    decks[0].append(cardlist[x])
                decks[1].reverse()
                decks[0].reverse()

                #print decks


            #print carddir
                
            
            #print "cardlist:",cardlist
            cardfromframe=frame/64
            if cardfromframe>cards/2-1:
                room=5
                frame=-1#when you are going down one room.. or reset wont work

            
            else:
              if frame%64==0:
                  one=1
                  leftcar=tilelist[5]
                  rightcar=tilelist[6]
                  deltax=0
                  deltay=0
                  deltax2=0
                  deltay2=0
                  rotdeg=[rotation[0]*90%360,rotation[1]*90%360]
                  
                  #print "YEL:",rotdeg[0], carpos[0],lookx,looky
                  #print "PUR:",rotdeg[1], carpos[1],lookx2,looky2
                  if carpos[0]==goalpos[0] or carpos[1]==goalpos[1]:
                    #print"you are done"
                    room=7


                  #delta=0
                  if (decks[0][int(cardfromframe)]==5):
                    rotation[0]+=1
                    rotationcountdown[0]+=90
                    tilelist[5]=pygame.transform.rotate(tilelist[5],90)
                  else:
                    if decks[0][cardfromframe]==6:
                      rotation[0]-=1
                      rotationcountdown[0]-=90
                      tilelist[5]=pygame.transform.rotate(tilelist[5],-90)
                    else:

                      if (decks[0][cardfromframe]+rotation[0])%4==1:
                        if carpos[0][1]>1:
                          deltay=-one
                          carpos[0][1]-=1
                      if (decks[0][cardfromframe]+rotation[0])%4==3:
                        deltay=one
                        carpos[0][1]+=1
                      if (decks[0][cardfromframe]+rotation[0])%4==2:
                        if carpos[0][0]>1:
                          deltax=-one
                          carpos[0][0]-=1
                      if (decks[0][cardfromframe]+rotation[0])%4==0:
                        deltax=one
                        carpos[0][0]+=1

                  #if decks[0][cardfromframe]==5:
                   # bitmaplist[7]=pygame.transform.rotate(bitmaplist[7],10)
                  #if decks[0][cardfromframe]==6:
                   # bitmaplist[7]=pygame.transform.rotate(bitmaplist[7],-10)




                  if decks[1][cardfromframe]==5:
                    rotation[1]+=1
                    rotationcountdown[1]+=90
                    tilelist[6]=pygame.transform.rotate(tilelist[6],90)
                    
                  else:
                    if decks[1][cardfromframe]==6:
                      rotation[1]-=1
                      rotationcountdown[1]-=90
                      tilelist[6]=pygame.transform.rotate(tilelist[6],-90)
                      
                    else:
                      if (decks[1][cardfromframe]+rotation[1])%4==1:
                        if carpos[1][1]>1:
                          deltay2=-one
                          carpos[1][1]-=1
                      if (decks[1][cardfromframe]+rotation[1])%4==3:
                        deltay2=one
                        carpos[1][1]+=1
                      if (decks[1][cardfromframe]+rotation[1])%4==2:
                        if carpos[1][0]>1:
                          deltax2=-one
                          carpos[1][0]-=1
                      if (decks[1][cardfromframe]+rotation[1])%4==0:
                        deltax2=one
                        carpos[1][0]+=1
              



            lookx+=deltax
            looky+=deltay
            lookx2+=deltax2
            looky2+=deltay2
            screen.fill((55,133,33))
            screen.blit(bitmaplist[10], (0, 0), (0, 0, fieldw,fieldh)) 
            screen.blit(bitmaplist[10], (fieldr, 0), (0, 0, fieldw,fieldh)) 
            screen.blit(bitmaplist[7], (0, fieldd), (lookx, looky, fieldw,fieldh)) 
            
            screen.blit(bitmaplist[7], (fieldr, fieldd), (lookx2, looky2, fieldw,fieldh)) 

            if rotationcountdown[0]>0:
              rotationcountdown[0]-=2

              leftcar=pygame.transform.rotate(tilelist[5],-1*rotationcountdown[0])


            if rotationcountdown[0]<0:
              rotationcountdown[0]+=2

              leftcar=pygame.transform.rotate(tilelist[5],-1*rotationcountdown[0])

            leftcarrect=leftcar.get_rect()
            leftcarrect.center=(3*64+32,fieldd+3*64+32)
            screen.blit(leftcar,leftcarrect)

            if rotationcountdown[1]>0:
              rotationcountdown[1]-=2
              rightcar=pygame.transform.rotate(tilelist[6],-1*rotationcountdown[1])


            if rotationcountdown[1]<0:
              rotationcountdown[1]+=2
              rightcar=pygame.transform.rotate(tilelist[6],-1*rotationcountdown[1])


            rightcarrect=rightcar.get_rect()
            rightcarrect.center=(fieldr+3*64+32,fieldd+3*64+32)
            screen.blit(rightcar,(rightcarrect))


            decknr=-1

            for deck in decks:
                
                mcard=0
                for card in deck:
                    mcard+=1

                    bitmap=bitmaplist[card-1]
                    if mcard==cardfromframe+1:
                      stretch = pygame.transform.scale(bitmap, (64, 64))
                      screen.blit(stretch, (screenw/2-32+decknr*48, 300+(mcard*96)), (0, 0, 64,64))
                    else:
                      stretch = pygame.transform.scale(bitmap, (48, 48))  
                      screen.blit(stretch, (screenw/2-24+decknr*48, 300+(mcard*96)), (0, 0, 48,48))
                    
                    font=pygame.font.Font(upcli,fontsize*2/3)
                    text= font.render(str(nrcard), True, (255,255,255))
                #text= font.render(str(totdir), True, (255,255,255))
                    #screen.blit(text, [screenw/2-48+adposy*(carddir[nrcard])+5, adposx+5])
                decknr+=2

           




            for e in pygame.event.get():
             
                  
              
              if e.type == stopevent:
                return

        if room==7:
            screen.fill((99,133,99))
            font=pygame.font.Font(upcli,fontsize*2)
           

            text= font.render("VICTORY! :)", True, blue)
            screen.blit(text, [320,150+50*math.sin((frame*2-2)*0.05)])
            for e in pygame.event.get():
             
                  
              
              if e.type == stopevent:
                return



        
        pygame.display.flip()
        mainClock.tick(40)

if __name__ == '__main__': main()
pygame.quit()