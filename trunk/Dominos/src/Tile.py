#!/usr/bin/env python
'''
Created in Apr 6, 2009

@author: Abdallah Saeed

modified by Mohamed Elemam in Apr 8, 2009
	modification:
		changed functions' names and modified them to be much more readable
'''
import sys, pygame

class Tile(object):
	def __init__(self, number1, number2, screen, X, Y):
		
		self._number1 = number1
		self._number2 = number2
		
		self._X = X
		self._Y = Y
		
		self._screen = screen
		
		image1_place = "images/" + str(self._number1) + ".png"
		self._square1 = pygame.image.load(image1_place)
		
		image2_place = "images/" + str(self._number2) + ".png"
		self._square2 = pygame.image.load(image2_place)

	def show_horizontal(self):
		if self._number1 == 6 :
			self._square1 = pygame.image.load("images/6r.png")
		elif self._number2 == 6 :
			self._square2 = pygame.image.load("images/6r.png")
		
		self._screen.blit(self._square1, (self._X,self._Y))
		self._screen.blit(self._square2, ((self._X+34),self._Y))
		pygame.display.flip()


	def show_vertical(self):
		self._screen.blit(self._square1, (self._X, self._Y))
		self._screen.blit(self._square2, (self._X, (self._Y+34)))
		pygame.display.flip()
