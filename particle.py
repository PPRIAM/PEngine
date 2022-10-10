# particles = [loc, velocity, img]
# img_list = []
# 
#
#
#

import core_func, random

class Particle:
  def __init__(self):
    self.p = core_func.load_imgs("static/p/p", 4)
    self.frame = 0
    self.start_img = 0
    self.particles = []

  def add(self, origin, offset):
    x, y = origin
    dir = [random.randint(-3, 3), -3]
    self.particles.append([[x-offset[0], y-offset[1]], dir, self.p[self.start_img]])

  def update(self, display):
    if self.frame < len(self.p)-1:
        self.frame += 0.5
    else:
      self.frame = 0
    for particle in self.particles:  
      particle[0][0] += particle[1][0]
      particle[0][1] += particle[1][1]
      particle[1][1] += 0.1
      particle[2] = self.p[int(self.frame)]

      display.blit(particle[2], particle[0])
      
      if particle[2] == self.p[3]:
        self.particles.remove(particle)
        

  
  