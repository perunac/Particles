#!/usr/bin/env python
#########################################################
#             Created by Pawel Wisniewski               #
#                     23-09-2013                        #
#                    Version 0.1                        #
#         http://potyczkiinformatyczne.blogspot.pl      #
#########################################################

#TODO
#get all screen boundyce

PARTICLESTYPES = ["PARTICLE","BOUNCYPARTICLE","BOUNCYPARTICLEDYING"]

class Particle():
  """simple particle class"""
  def __init__(self,x,y,xVel,yVel,color,screenWidth,screenHeight,startXcor,startYcor):
    self.x          = x
    self.y          = y
    self.startX     = x
    self.startY     = y
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
