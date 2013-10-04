#!/usr/bin/env python
#########################################################
#             Created by Pawel Wisniewski               #
#                     23-09-2013                        #
#                    Version 0.1                        #
#         http://potyczkiinformatyczne.blogspot.pl      #
#########################################################

#TODO
#get all screen boundyce
import random

PARTICLESTYPES = ["PARTICLE","BOUNCYPARTICLE","BOUNCYPARTICLEDYING","SHAKEINGPARTICLE"]

class Particle():
  """simple particle class"""
  def __init__(self,x,y,xVel,yVel,color,screenWidth,screenHeight,startXcor,startYcor):
    self.x          = x               #current x position
    self.y          = y               #current y position
    self.startX     = x               #starting x position
    self.startY     = y               #starting y position
    self.xVel       = xVel            #x velocity
    self.yVel       = yVel            #y velocity
    self.scrWidth   = screenWidth     #particles screen width
    self.scrHeight  = screenHeight    #particles screen height
    self.color      = color           #particle color
    self.topleftX   = startXcor       #top left corner of particle screen x coordinat
    self.topleftY   = startYcor       #top left corner of particle screen y coordinat

  def update(self):
    self.x += self.xVel
    self.y += self.yVel
    if self.x > self.scrWidth or self.y > self.scrHeight or self.x < self.topleftX or self.y < self.topleftY:
      self.x = self.startX
      self.y = self.startY
    return 1

class BouncyParticle(object):
  """this particle bounce from walls"""
  def __init__(self,x,y,xVel,yVel,color,screenWidth,screenHeight,startXcor,startYcor):
    self.x          = x
    self.y          = y
    self.xVel       = xVel
    self.yVel       = yVel
    self.scrWidth   = screenWidth
    self.scrHeight  = screenHeight
    self.color      = color
    self.topleftX   = startXcor
    self.topleftY   = startYcor

  def update(self):
    self.x += self.xVel
    self.y += self.yVel
    if self.x > self.scrWidth or self.x < self.topleftX:
      self.xVel = -self.xVel
    elif self.y > self.scrHeight or self.y < self.topleftY:
      self.yVel = -self.yVel
    return 1

class BouncyParticleDying(BouncyParticle):
  """this particle lives specyfic amount of time"""
  """ttl is time to live, if its -1 particle is infinite"""
  def __init__(self,x,y,xVel,yVel,color,screenWidth,screenHeight,startXcor,startYcor,ttl):
    BouncyParticle.__init__(self,x,y,xVel,yVel,color,screenWidth,screenHeight,startXcor,startYcor)
    self.ttl = ttl

  def update(self):
    self.x += self.xVel
    self.y += self.yVel
    if self.x > self.scrWidth or self.x < self.topleftX:
      self.xVel = -self.xVel
    elif self.y > self.scrHeight or self.y < self.topleftY:
      self.yVel = -self.yVel
    if self.ttl > 0:
      self.ttl -= 1
    elif self.ttl == 0:
      return 0
    return 1
class ShakeingParticle(Particle):
  """
  this particle shakes in time
  """
  def __init__(self,x,y,xVel,yVel,color,screenWidth,screenHeight,startXcor,startYcor,ttl):
    Particle.__init__(self,x,y,xVel,yVel,color,screenWidth,screenHeight,startXcor,startYcor)
    self.ttl = ttl

  def update(self):
    if self.ttl != 0:
      self.x += self.xVel
      self.y += self.yVel
      if self.x > self.scrWidth or self.y > self.scrHeight or self.x < self.topleftX or self.y < self.topleftY:
        self.x = self.startX
        self.y = self.startY
      if self.xVel < self.yVel:
        self.y += random.randint(-2,2)
      else:
        self.x += random.randint(-2,2)
      self.ttl -= 1
      return 1
    else:
      return 0

