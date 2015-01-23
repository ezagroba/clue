## Objects ##

# define weapon
class Weapon(object):

	def murder_weapon(self):
		# has this weapon committed a murder? boolean switches to True
		False

	def name(self):
		# name of the weapon
		""

# define gun, starts with six bullets and cannot shoot after bullets run out
class Gun(Weapon):

	def bullets(self):
		# starts with six bullets, decreases by one or two when shot
		6

	def fired(self):
		# expels a bullet if there are any
		if self.bullets < 1:
			print "One plus two plus two plus one. One plus two plus one plus one."
		elif self.bullets >= 1:
			self.bullets -= 1
		else:
			print "Let us in, let us in! Let us out, let us out!"


# define person object, person can hold weapon
# define room


## Inherit from Person ##

# guest
# Mr. Body
# Wadsworth
# victim

## Lists ## 
# possible suspects: list begins with Mr. Body and six named characters
# bodies: list begins empty
# weapons
weapons = ["gun", "rope", "wrench", "lead pipe", "candlestick", "knife"]
# rooms
rooms = ["kitchen", "billard room", "ballroom", "hall", "conservatory", "dining room", "study", "lounge", "library"]


## Functions ##

# kill: removes person from possible suspects, adds to bodies list
# serious: when bodies > 4, print "Three murders? This is getting serious."
# guess: declares person + room + weapon
# end: choose one of the three random endings - may also need functions for endings?


## Printing random strings ##

# create a general function that given a not case-sensitive string prints a string.

# communism: "communism", print "No, Communism is just a red herring."
# threaten: "threaten", print "Miss Scarlett: Why would he wanna kill you in public? Wadsworth: I think she meant he threatened, in public, to kill her."
# meaning of no:  "no", print "No meaning yes?"
# know: "How do you know?", print "I know because I was there."
# short: "To make a long story short", print "Too late."
# open another door: "open another door", print "What's this? Another door! *gets sprayed by shower*"

