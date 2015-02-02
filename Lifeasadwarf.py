from sys import exit
from random import randint


class Scene(object):

	def enter(self):
		print "This scene is not configured yet.  Subclass it and implement enter()"
		exit(1)
		

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
	
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		current_scene.enter()		
	
class Loss(Scene):
	
	quips = [
		"Woops you lose."
		
	]
	
	def enter(self):
		print Loss.quips[randint(0, len(self.quips)-1)]
		exit(1)

class Well(Scene):

	def enter(self):
		
		print "You are a dwarf from Argentina.  You live in Nathan's" 
		print "lovely fortress.  Your assigned duties for today are"
		print "hauling water from the local well.  As you bring up" 
		print "the bucket, you slip and fall into the well!"
		print "\n"
		print "You're now stuck in a well.  You have to get out or"
		print "starve.  Do you want to: 1. yell for help, 2. try to" 
		print "climb out, or 3. look for an exit."
		
		action = raw_input("> ")
		
		if action == "1":
			print "You decide to put your vocal cords to the test"
			print "and obnoxiously sing Darude Sandstorm. After"
			print "the third repition, no one has come. You start"
			print "yelling more desperately, but no one heres you."
			return 'Loss'
			
		elif action == "2":
			print "All those years at the gym will surely pay off."
			print "You latch onto the wall and begin to hoist yourself"
			print "out.  The start is very slippery and you end up having"
			print "to restart twice.  On your third attempt you make it to"
			print "the top.  You poke your head out only to be smacked by"
			print "your buddy who's come looking for you.  You fall back"
			print "down the well."
			return 'Loss'
		
		elif action == "3":
			print "You decide to take a look around while you're stuck down"
			print "here.  After a brief glance, you don't see anything."
			print "You keep looking and you see a small glow from a crevice"
			print "in the wall under the water.  You swim towards the light."
			return 'Cavern'
		
		else: 
			print "Please enter a number."
			return 'Well'

class Cavern(Scene):

	def enter(self):
		print "The light leads you to an underground cavern.  Looking up,"
		print "you can just barely see the roof.  The natural light seems"
		print "to be coming from some mushrooms scattered around.  Do you"
		print "want to: 1. explore the cavern, 2. go back the way you came"
		print "3 sit and wait."
			
		action = raw_input ("> ")
			
		if action == "1":
			print "Time to keep using the look command. A quick glance reveals"
			print "an entrance to a tunnel across the cavern.  Rather than sitting"
			print "around all day, you decide to go to the tunnel. On the way you" 
			print "pass some skeletons."
			return 'Tunnel'

		elif action == "2":
			print "This cave is scary.  You go back to the well."
			return 'Well'
		
		elif action == "3":
			print "You're really tired.  Like, really, really tired.  You sit down."
			print "A couple of years later some lost dwarves find your skeleton."
			return 'Loss'
			
		else: 
			print "Please enter a number."
			return 'Cavern'
			
			
class Tunnel(Scene):
	
	def enter(self):
		print "You enter a tunnel.  There are three ways to go.  Do you go 1. Left,"
		print "2. Right, or 3. Back?"
		
		correct_way = "%d" % (randint(1,2))
		
		action = raw_input("> ")
			
		if action == "3": 
			print "This tunnel is 2sketchy4you.  You go back to the cavern"
			return 'Cavern'
			
		elif action == correct_way:
			print "You start walking.  After maybe 10 minutes the tunnel curves."
			print "When you get around the bend, you see sunlight."
			print "\n"
			print "Congratulations, you win!"
			quit(1)
				
		else:
			print "You get bored of thinking and start walking.  After maybe 10"
			print "minutes the tunnel curvese.  When you get around the bend,"
			print "you see sunlight!  There's also a bear... Uh oh."
			return 'Loss'
			

class Map(object):
	
	scenes = {
		'Well': Well(),
		'Cavern':Cavern(),
		'Tunnel':Tunnel(),
		'Loss':Loss(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('Well')
a_game = Engine(a_map)
a_game.play()