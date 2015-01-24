import random

## Objects ##

class Weapon(object):
# define weapon

	def name(self):
	# name of the weapon
		self.name

	def murder_weapon(self):
	# has this weapon committed a murder? boolean switches to True
		self.murder_weapon = False


class Gun(Weapon):
# define gun, starts with six bullets and cannot shoot after bullets run out


	def bullets(self):
	# starts with six bullets, decreases by one or two when shot
		self.bullets = 6

	def fired(self):
	# expels a bullet if there are any
		if self.bullets < 1:
		# no bullets left
			print "One plus two plus two plus one. One plus two plus one plus one."

		elif self.bullets == 1:
		# expel one bullet if there is only one bullet left
			self.bullets -= 1

		elif self.bullets >= 2:
		# expel one or two bullets if there are more than two bullets left
			self.bullets -= random.choice[1,2]

		else:
		# error for the gun
			print "Let us in, let us in! Let us out, let us out!"




class Visitor(object):
# define person object, person can hold one weapon

	def name(self):
		self.name

class Guest(Visitor):

	def hasweapon(self):
	# which weapon does this person have?
		self.hasweapon

class Mr_Body(Visitor):

	def hasweapons(self):
		self.hasweapons = True


class Room(object):
# define room

	def name(self):
		self.name


## Lists ## 
# guests: Wadsworth and six named characters
guests = ["Wadsworth", "Colonel Mustard", "Professor Plum", /
			"Miss Scarlett", "Mrs. White", "Mrs. Peacock", "Mr. Green"]
# bodies: list begins empty
bodies = []
# visitors
visitors = ["The Cook", "The Maid", "The Motorist", "The Policeman", /
			"The Singing Telegram Girl"]
# weapons
weapons = ["gun", "rope", "wrench", "lead pipe", "candlestick", "knife"]
# rooms
rooms = ["kitchen", "billard room", "ballroom", "hall", "conservatory", "dining room", /
		 "study", "lounge", "library"]


## Functions ##

# kill: removes person from possible suspects, adds to bodies list
# serious: when bodies > 4, print "Three murders? This is getting serious."
# guess: declares person + room + weapon
# end: choose one of the three random endings - may also need functions for endings?


## Printing random strings ##

# create a general function that given a not case-sensitive string prints a string.

# communism: "communism", print "No, Communism is just a red herring."
# threaten: "threaten", print "Miss Scarlett: Why would he wanna kill you in public? /
#	Wadsworth: I think she meant he threatened, in public, to kill her."
# meaning of no:  "no", print "No meaning yes?"
# know: "How do you know?", print "I know because I was there."
# short: "To make a long story short", print "Too late."
# open another door: "open another door", print "What's this? Another door! /
#	*gets sprayed by shower*"