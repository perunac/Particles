#!/usr/bin/env python
#########################################################
#             Created by Pawel Wisniewski               #
#                     23-09-2013                        #
#                    Version 0.1                        #
#         http://potyczkiinformatyczne.blogspot.pl      #
#########################################################
import pygame,sys,particles,random
from pygame.locals import *
from collections import deque

#definitions of global constans
SCRWIDTH  = 800
SCRHEIGHT = 600
MAXPARTICLES = 800
FPS = 40
NEWPARTICLES = 2
MAXXVEL = 4
MAXYVEL = 4

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

ALLCOLORS = [RED, GREEN, GRAY, BLUE, YELLOW, ORANGE, PURPLE, CYAN, NAVYBLUE]


def main():
  pygame.init()
  SCREEN = pygame.display.set_mode((SCRWIDTH,SCRHEIGHT))
  CLOCK = pygame.time.Clock()
  particles = deque([],MAXPARTICLES)
  mouseDown = False
  mousePos = (None,None)

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
      elif event.type == MOUSEBUTTONDOWN:
        mouseDown = True
        mousePos = event.pos
      elif event.type == MOUSEBUTTONUP:
        mouseDown = False
      elif event.type == MOUSEMOTION:
        mousePos = event.pos

    #add new particles if mouse button is hold
    if mouseDown:
      generateParticles(particles,mousePos)
    #draw particles
    for part in particles:
      part.update()
      pygame.draw.circle(SCREEN,part.color,(part.x,part.y),2)

    pygame.display.flip()
    CLOCK.tick(FPS)
  pygame.quit()
  sys.exit()


def pause():
  """stops main program for a while"""
  pass



def generateParticles(list,pos):
  """generates new particles and maintaining there is not to much of then"""
  for i in range(NEWPARTICLES):
    list.append(particles.Particle(pos[0],pos[1],random.randint(-MAXXVEL,MAXXVEL),random.randint(-MAXYVEL,MAXYVEL),ALLCOLORS[random.randint(0,len(ALLCOLORS)-1)],SCRWIDTH,SCRHEIGHT))



if __name__ == '__main__':
  main()
