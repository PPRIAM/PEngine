import core_func

class Entity:
  def __init__(self, origin, speed, image, isMovable=False):
    self.image = image.convert()
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
    self.jump = 0
    
    self.image = self.frames[self.frame_index]
    self.rect = self.image.get_rect(center = origin)
    self.health = health
    self.collision_types = {'top':False, 'bottom':False, 'left':False, 'right':False}
    self.falling = True
   
    
  def set_action(self, action):
    self.state = action
    self.frames = self.anim_type[self.state]
    

  
  def update(self, dt, platforms):
    if self.movement[0] < 0:
      self.direction = "left"
    if self.movement[0] > 0:
      self.direction = "right"
    self.animate(dt)
    self.set_action("idle")
    if self.movement[0] > 0:
      self.set_action("run")
    if self.movement[1] < 0:
      self.set_action("jump")
    if self.falling:
      self.set_action("fall")
    if self.health == 0:
      self.set_action("die")
    if self.direction == "left":
      if self.movement[0] == 0:
        self.set_action("idleleft")
      if self.movement[0] < 0:
        self.set_action("runleft")
      if self.movement[1] < 0 :
        self.set_action("jumpleft")
      if self.falling:
        self.set_action("fallleft")
      if self.health == 0:
        self.set_action("dieleft")
    if self.health > 0:
      self.move(dt, platforms)

  def move(self, dt, platforms):
    self.collision_types = {'top':False, 'bottom':False, 'left':False, 'right':False}
    self.rect.x += self.movement[0]*dt
    block_hit_list = core_func.collision_test(self.rect, platforms)
    for block in block_hit_list:
      if self.movement[0] > 0:
        self.rect.right = block.left
        self.collision_types['right'] = True
      if self.movement[0] < 0:
        self.rect.left = block.right
        self.collision_types['left'] = True
    self.rect.y += self.movement[1]*dt
    block_hit_list = core_func.collision_test(self.rect, platforms)
    for block in block_hit_list:
      if self.movement[1] < 0:
        self.rect.top = block.bottom
        self.collision_types['top'] = True
      if self.movement[1] > 0:
        self.rect.bottom = block.top
        self.collision_types['bottom'] = True
  
  def animate(self, dt):
    for k in self.states:
      if k in ["idle", "idleleft", "run", "runleft", "fall", "fallleft"]:
        if self.frame_index < len(self.frames)-1:
          self.frame_index += self.animation_speed*dt
        if self.frame_index >= len(self.frames)-1:
          self.frame_index = 0
      elif k in ["jump", "jumpleft", "die", "dieleft"]:
        if self.frame_index < len(self.frames)-1:
          self.frame_index += self.animation_speed*dt
      
    self.image = self.frames[int(self.frame_index)]

    
    

    