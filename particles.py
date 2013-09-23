#!/usr/bin/env python
#########################################################
#             Created by Pawel Wisniewski               #
#                     23-09-2013                        #
#                    Version 0.1                        #
#         http://potyczkiinformatyczne.blogspot.pl      #
#########################################################

class Particle():
  """simple particle class"""
  def __init__(self,x,y,xVel,yVel,color,screenWidth,screenHeight):
    self.x          = x
    self.y          = y
    self.startX     = x
    self.startY     = y
    self.xVel       = xVel
    self.yVel       = yVel
    self.scrWidth   = screenWidth
    self.scrHeight  = screenHeight
    self.color      = color

  def update(self):
    self.x += self.xVel
    self.y += self.yVel
    if self.x > self.scrWidth or self.y > self.scrHeight or self.x < 0 or self.y < 0:
      self.x = self.startX
      self.y = self.startY
