import pygame as pg
import sys, random, time

class Particle:
	def __init__(self, color=[[255, 255, 255], [0, 0, 0]], decrease_by=[0.2, 0.4], follow_mouse=False, pos=[0, 0], radius=[10, 10], rect=False, gravity=0, gray=False):
		self.particles = []

		self.color = color

		self.follow_mouse = follow_mouse # position
		self.pos = pos

		self.radius = radius # size
		self.decrease_by = decrease_by

		self.rect = rect # shape

		self.gravity = gravity

		self.gray = gray

	def emit(self):
		if self.particles:
			self.delete_particles()
			for particle in self.particles:
				particle[0][1] += particle[2][0]
				particle[0][0] += particle[2][1]

				particle[2] = [particle[2][0] + self.gravity, particle[2][1]]

				for p in particle[0]: p = int(p)
				particle[1] -= random.uniform(self.decrease_by[0], self.decrease_by[1])

				color = particle[3]

				if self.rect:
					pg.draw.rect(screen, color, (*particle[0], particle[1]*2, particle[1]*2))
				else:
					pg.draw.circle(screen, color, [int(particle[0][0]), int(particle[0][1])], int(particle[1]))

	def add_particles(self):
		pos_x = self.pos[0]
		pos_y = self.pos[1]
		if self.follow_mouse:
			pos_x = pg.mouse.get_pos()[0]
			pos_y = pg.mouse.get_pos()[1]

		radius = random.uniform(self.radius[0], self.radius[1])

		direction_x = random.uniform(-3,3)
		direction_y = random.uniform(-3,3)

		color = [0, 0, 0]
		if self.gray:
			scale = random.randint(self.color[0][0], self.color[1][0])
			color = [scale, scale, scale]
		else:
			color = [
			random.randint(self.color[0][0], self.color[1][0]),
			random.randint(self.color[0][1], self.color[1][1]),
			random.randint(self.color[0][2], self.color[1][2])
			]

		particle_circle = [[int(pos_x), int(pos_y)],radius,[direction_x,direction_y], color]
		self.particles.append(particle_circle)

	def delete_particles(self):
		particle_copy = [particle for particle in self.particles if particle[1] > 0]
		self.particles = particle_copy

pg.init()
screen = pg.display.set_mode((500,500))
clock = pg.time.Clock()

particle1 = Particle(((0, 0, 0), (255, 255, 255)), (0.2, 0.5), False, (250, 250), (5, 10), True, 0.2, False)
#particle2 = Particle(screen, 0, 250, 250, (0, 0, 255), 16, False, 1, 1, 1, 2)

PARTICLE_EVENT = pg.USEREVENT + 1
pg.time.set_timer(PARTICLE_EVENT,40)

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
		if event.type == PARTICLE_EVENT:
			particle1.add_particles()
			#particle2.add_particles()

	screen.fill((30,30,30))
	particle1.emit()
	pg.display.update()
	clock.tick(60)
