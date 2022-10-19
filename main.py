# Testing file-------------------------
import pygame, sys, camera, particle, entities, time, core_func, tilemap

pygame.init()
FPS = 60
clock = pygame.time.Clock()

WINDOW_SIZE = (500, 500)

screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("PEngine main test")

staticRect = pygame.Rect(10, 10, 10, 10)


movement = [0, 0]

prev_time = time.time()

par = particle.Particle()

animT = [["idle", 3], ["run", 6], ["jump", 4], ["fall", 2], ["die", 7]]
animations = core_func.load_animation("adventurer", animT)
for a in animations:
  print(a)
adventurer = entities.Player([200, 100], 1, pygame.Surface([50, 50]), animations)

tileset = { "1" : "neon_tile", "2":"tile" }
config = core_func.read_json("config")

tilemap = tilemap.Tilemap(tileset, "map")
hit_list = tilemap.get_hit_list(config)
c = camera.Camera(adventurer.rect)


for i in tilemap.map:
  print(i)

run = True
while run:
    clock.tick(FPS)
    dt = time.time() - prev_time
    dt*= FPS
    prev_time = time.time()
    screen.fill((0, 0, 0))
    surf = pygame.transform.scale(screen, WINDOW_SIZE)
    screen.blit(surf, (0, 0))

    c.update(screen)

    
    adventurer.render(screen, c.offset)
    adventurer.update(dt, hit_list)
    print(adventurer.state)
    print(adventurer.movement)
    print(adventurer.collision_types["bottom"])

    adventurer.movement[1] = 1
    if adventurer.collision_types["bottom"]:
      adventurer.falling = False
    if adventurer.jump > 0:
      adventurer.movement[1] = -10
      adventurer.jump = 0
      adventurer.falling = True
      
    
      
    
  
    tilemap.render(screen, config, c.offset)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT: adventurer.movement[0] -= 1
            if event.key == pygame.K_RIGHT: adventurer.movement[0] += 1
            if event.key == pygame.K_UP:
                adventurer.jump += 1
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT: adventurer.movement[0] += 1
            if event.key == pygame.K_RIGHT: adventurer.movement[0] -= 1
