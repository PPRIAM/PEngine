# Testing file-------------------------
import pygame, sys, camera

pygame.init()
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("PEngine main test")

staticRect = pygame.Rect(10, 10, 10, 10)

playerRect = pygame.Rect(50, 50, 10, 10)

movement = [0, 0]
c = camera.Camera(playerRect)

run = True
while run:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    c.update(screen)
    print(c.offset)

    # Draw the static rect
    
    pygame.draw.rect(screen, (255, 0, 0), (10-c.offset[0], 10-c.offset[1], 10, 10))

    # Draw the player rect
    
    pygame.draw.rect(screen, (255, 255, 0), (playerRect.x-c.offset[0], playerRect.y-c.offset[1], 10, 10))

    # Move the player rect
    if movement[0] == -1:
        playerRect.x -= 1
    if movement[0] == 1:
        playerRect.x += 1
    if movement[1] == -1:
        playerRect.y -= 1
    if movement[1] == 1:
        playerRect.y += 1

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: movement[1] -= 1
            if event.key == pygame.K_DOWN: movement[1] += 1
            if event.key == pygame.K_LEFT: movement[0] -= 1
            if event.key == pygame.K_RIGHT: movement[0] += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: movement[1] += 1
            if event.key == pygame.K_DOWN: movement[1] -= 1
            if event.key == pygame.K_LEFT: movement[0] += 1
            if event.key == pygame.K_RIGHT: movement[0] -= 1
