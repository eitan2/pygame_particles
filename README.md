# pygame_particles
Python program that contains a class of Particles with customizeable properties such as - shape, color, affected by gravity, lifetime and lots more

to use it just import:
	from Particles import ParticleMaster

and then create the master:
	master = ParticleMaster()

add an update method in the mainloop:
	master.update_effects()
  
then every time you want to add an effect:
	master.add_effect(screen, color, decrease_by, follow_mouse, pos, radius, rect, gravity, gray, speed, litetime, spawn_speed)
  
	explanation:
    	screen, is the pygame screen. example - screen = pygame.display.set_mode((500,500)) # will create a 500px by 500px window named screen
		color, is the range the colors can be randomized in. example - [[0, 0, 0], [255, 255, 255]] # will allow any color. or black to white
		decrease by, is the range of the amount the size of each particle will be randomized to be decreased by at each frame it's also the way particles are being destroyed - when they're too small so be sure it's bigger than 0, example - [0.2, 0.4] # each particle will choose a number between those and will decrease by it at each frame
		follow_mouse, is a boolean that is responsable for will the particles will follow the mouse or not. example - True # the particles will be at the mouse position at all time
		pos, is the starting position for the particles. it's irelevant if follow_mouse is on. example - [250, 250]
		radius, is the range the radius or half the size of each particle will be randomized in, it's got to be a positive number. remember that it will effect the lifetime of each particle. example - [10, 15] # each particle will choose a starting size between 10 and 15
		rect, will determine whether or not the particles will be shaped as squares, if not they will be circles. example - True # the particles will be shaped as squares
		gravity, the amount of gravity that will be applyed, can be 0 for no gravity and negative for upwards gravity. example - 0.05 # a realatively small downwards gravity will be apllyed
		gray, will determine whether or not the color range should be gray which means the r, g, b scales will be equal one to each other. example - False # the color can be colorful
		speed, the maximum speed that can be applyed to each particle, wiil effect the distance each particle travels. example - 3 # the speed of each particle can be up to 3
		
		lifeetime, the lifetime of the particle group as a whole (not of each particle) in seconds. example - 10 # the particles will be generating for 10 seconds
		spawn_speed, the frames that the programm will wait until generating a new particle. example - 1 # a new particle will be generated each frame
		
		full example - master.add_effect(screen, [[0, 0, 0], [255, 255, 255]], [0.2, 0.4], True, [250, 250], [10, 15], True, 0.05, False, 3, 10, 1)

the whole script:
