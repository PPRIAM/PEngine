# Entity - class
# Sprite(Player, Enemy) -> Image, Origin, Velocity, Movement, State, Animation type, Animation length...

#import core_func

class Entity:
  def __init__(self, origin, speed, image, isMovable=False):
    self.image = image
    self.rect = self.image.get_rect(center=origin)
    self.isMovable = isMovable
    self.movement = [0, 0]
    self.speed = speed

  def render(self, display, offset):
    display.blit(self.image, (self.rect.x-offset[0], self.rect.y-offset[1]))

  def update(self, sprite):
    if self.isMovable:
      if self.rect.colliderect(sprite.rect):
        self.movement = sprite.movement

class Player(Entity):
  def __init__(self, origin, speed, image, anim_type, health=1):
    Entity.__init__(self, origin, speed, image)
    self.states = [k for k in anim_type]
    self.state = self.states[0]
    self.anim_type = anim_type 
    self.frames = anim_type[self.state]
    self.animation_speed = 0.1
    self.frame_index = 0
    self.direction = "left"
    
    self.image = self.frames[self.frame_index]
    self.rect = self.image.get_rect(center = origin)
    self.health = health
   
    

  def update(self, dt):
    self.animate(dt)
    if self.movement[0] == 0 and self.movement[1] == 0:
      if self.direction == "left":
        self.state = self.states[1]
      else:
        self.state = self.states[0]
    if self.movement[0] == 1:
      self.rect.x += self.speed
      self.state = self.states[2]
      self.direction = "right"
    if self.movement[0] == -1:
      self.rect.x -= self.speed
      self.state = self.states[3]
      self.direction = "left"
    if self.movement[1] == 1:
      self.rect.y += self.speed
      if self.direction == "left":
        self.state = self.states[3]
      else:
        self.state = self.states[2]
     
    if self.movement[1] == -1:
      self.rect.y -= 1
      if self.direction == "left":
        self.state = self.states[3]
      else:
        self.state = self.states[2]
    

  def animate(self, dt):
    if self.frame_index < len(self.frames)-1:
      self.frame_index += self.animation_speed*dt
    if self.frame_index >= len(self.frames)-1:
      self.frame_index = 0
      
    self.image = self.frames[int(self.frame_index)]

    for state in range(len(self.states)-1):
      if self.state == self.states[state]:
        self.frames = self.anim_type[self.state]
    '''
    if self.state == self.states[0]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[1]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[2]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[3]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[4]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[4]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[5]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[6]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[7]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[8]:
      self.frames = self.anim_type[self.state]
    if self.state == self.states[9]:
      self.frames = self.anim_type[self.state]
    '''

    