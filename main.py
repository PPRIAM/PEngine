# Testing file-------------------------
import pygame, sys, camera, particle, entities, time, core_func

pygame.init()
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((360, 360))
pygame.display.set_caption("PEngine main test")

staticRect = pygame.Rect(10, 10, 10, 10)


movement = [0, 0]

prev_time = time.time()

par = particle.Particle()

animT = [["idle", 3], ["run", 6], ["jump", 0], ["fall", 0], ["die", 0]]
animations = core_func.load_animation("adventurer", animT)
for a in animations:
  print(a)
adventurer = entities.Player([250, 250], 1, pygame.Surface([50, 50]), animations)
c = camera.Camera(adventurer.rect)

run = True
while run:
    clock.tick(FPS)
    dt = time.time() - prev_time
    dt*= FPS
    prev_time = time.time()
    screen.fill((0, 0, 0))

    c.update(screen)
    #print(c.offset)
    #print(par.frame)
    #print(par.particles)

    # Draw the static rect
    
    pygame.draw.rect(screen, (255, 0, 0), (10-c.offset[0], 10-c.offset[1], 10, 10))

    # Draw the player rect
    
    adventurer.render(screen, c.offset)
    adventurer.update(dt)

    par.add([100, 100], c.offset)
    par.update(screen,dt)

  

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: adventurer.movement[1] -= 1
            if event.key == pygame.K_DOWN: adventurer.movement[1] += 1
            if event.key == pygame.K_LEFT: adventurer.movement[0] -= 1
            if event.key == pygame.K_RIGHT: adventurer.movement[0] += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: adventurer.movement[1] += 1
            if event.key == pygame.K_DOWN: adventurer.movement[1] -= 1
            if event.key == pygame.K_LEFT: adventurer.movement[0] += 1
            if event.key == pygame.K_RIGHT: adventurer.movement[0] -= 1
