#!/usr/bin/env python
#########################################################
#             Created by Pawel Wisniewski               #
#                     23-09-2013                        #
#                    Version 0.1                        #
#         http://potyczkiinformatyczne.blogspot.pl      #
#########################################################
import pygame,sys,particles,random,copy
from pygame.locals import *
from collections import deque


#definitions of global constans
SCRWIDTH  = 800
SCRHEIGHT = 600
MAXPARTICLES = 800
FPS = 40
MAXXVEL = 4
MAXYVEL = 4
PARTICLESTOPLEFTX = 0
PARTICLESTOPLEFTY = 0
PARTICLESSCRWIDTH = 800
PARTICLESSCRHEIGHT = 500
TTL = FPS * 3  #to give particles about 3 sec span

#texts center positions
PARTTYPETXTCENTER = (150, PARTICLESSCRHEIGHT + 30)


#colors
#name        R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

ALLCOLORS = [RED, GREEN, GRAY, BLUE, YELLOW, ORANGE, PURPLE, CYAN, NAVYBLUE, BLACK]


def main():
  pygame.init()
  SCREEN = pygame.display.set_mode((SCRWIDTH,SCRHEIGHT))
  CLOCK = pygame.time.Clock()
  particleslist = deque([],MAXPARTICLES)
  currentTypeNr = 0
  NEWPARTICLES = 2

  mouseDown = False
  inPartSurf = False
  mousePos = (None,None)
  particlesSurf = pygame.Rect(PARTICLESTOPLEFTX,PARTICLESTOPLEFTY,PARTICLESSCRWIDTH,PARTICLESSCRHEIGHT)


  #texts
  fontObj = pygame.font.Font('freesansbold.ttf',24)
  partTypeText = fontObj.render(particles.PARTICLESTYPES[currentTypeNr],True,BLACK)
  partTypeTextRect = partTypeText.get_rect()
  partTypeTextRect.center = PARTTYPETXTCENTER
  running = True
  while running:
    SCREEN.fill(WHITE)
    #events handling
    for event in pygame.event.get():
      if event.type == QUIT:
        running = False
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pause()
        elif event.key == K_SPACE:
          currentTypeNr = incrementPartTypeNr(currentTypeNr)
          (partTypeText,partTypeTextRect) = updatePartTypeText(partTypeText, partTypeTextRect, currentTypeNr, fontObj)
        elif event.key == K_c:
          particleslist = deque([],MAXPARTICLES)
        elif event.key == K_UP:
          if NEWPARTICLES < 60:
            NEWPARTICLES += 1
        elif event.key == K_DOWN:
          if NEWPARTICLES > 0:
            NEWPARTICLES -= 1
      elif event.type == MOUSEBUTTONDOWN:
        mouseDown = True
        mousePos = event.pos
      elif event.type == MOUSEBUTTONUP:
        mouseDown = False
      elif event.type == MOUSEMOTION:
        if particlesSurf.collidepoint(event.pos[0],event.pos[1]):
          inPartSurf = True
        else:
          inPartSurf = False
        mousePos = event.pos

    #add new particles if mouse button is hold
    if mouseDown and inPartSurf:
      generateParticles(particleslist,mousePos, currentTypeNr, NEWPARTICLES)
    #draw particles
    particlesToRemove = []
    for part in particleslist:
      if part.update():
        pygame.draw.circle(SCREEN,part.color,(part.x,part.y),2)
      else:
        particlesToRemove.append(part)
    for part in particlesToRemove:
      particleslist.remove(part)

    #draw text
    SCREEN.blit(partTypeText,partTypeTextRect)

    pygame.display.flip()
    CLOCK.tick(FPS)
  pygame.quit()
  sys.exit()


def pause():
  """stops main program for a while"""
  pass



def generateParticles(list, pos, type, newParticles):
  """generates new particles and maintaining there is not to much of then"""
  for i in range(newParticles):
    if particles.PARTICLESTYPES[type] == "PARTICLE":
      print "adding normal particle"
      list.append(particles.Particle(pos[0],pos[1],random.randint(-MAXXVEL,MAXXVEL),random.randint(-MAXYVEL,MAXYVEL),ALLCOLORS[random.randint(0,len(ALLCOLORS)-1)],PARTICLESSCRWIDTH,PARTICLESSCRHEIGHT,PARTICLESTOPLEFTX,PARTICLESTOPLEFTY))
    elif particles.PARTICLESTYPES[type] == "BOUNCYPARTICLE":
      print "adding bouncyparticle"
      list.append(particles.BouncyParticle(pos[0],pos[1],random.randint(-MAXXVEL,MAXXVEL),random.randint(-MAXYVEL,MAXYVEL),ALLCOLORS[random.randint(0,len(ALLCOLORS)-1)],PARTICLESSCRWIDTH,PARTICLESSCRHEIGHT,PARTICLESTOPLEFTX,PARTICLESTOPLEFTY))
    elif particles.PARTICLESTYPES[type] == "BOUNCYPARTICLEDYING":
      print "adding bouncyparticledying"
      list.append(particles.BouncyParticleDying(pos[0],pos[1],random.randint(-MAXXVEL,MAXXVEL),random.randint(-MAXYVEL,MAXYVEL),ALLCOLORS[random.randint(0,len(ALLCOLORS)-1)],PARTICLESSCRWIDTH,PARTICLESSCRHEIGHT,PARTICLESTOPLEFTX,PARTICLESTOPLEFTY,TTL))
    elif particles.PARTICLESTYPES[type] == "SHAKEINGPARTICLE":
      print "adding shakeingparticle"
      list.append(particles.ShakeingParticle(pos[0],pos[1],random.randint(-MAXXVEL,MAXXVEL),random.randint(-MAXYVEL,MAXYVEL),ALLCOLORS[random.randint(0,len(ALLCOLORS)-1)],PARTICLESSCRWIDTH,PARTICLESSCRHEIGHT,PARTICLESTOPLEFTX,PARTICLESTOPLEFTY,TTL))



def incrementPartTypeNr(val):
  if val >= len(particles.PARTICLESTYPES) - 1:
    val = 0
  else:
    val += 1
  return val

def updatePartTypeText(partTypeText, partTypeTextRect, currentTypeNr, fontObj):
  """
  updates particle type text
  returns pair of textSurf and rect
  """
  partTypeText = fontObj.render(particles.PARTICLESTYPES[currentTypeNr],True,BLACK)
  partTypeTextRect = partTypeText.get_rect()
  partTypeTextRect.center = PARTTYPETXTCENTER
  return (partTypeText,partTypeTextRect)



if __name__ == '__main__':
  main()
