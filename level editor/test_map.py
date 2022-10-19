import pygame, sys, gameobjects

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test level editor map")

map = gameobjects.read_json('C:/Users/RE COMPUTER/Documents/level editor/test/map')
config = gameobjects.read_json('C:/Users/RE COMPUTER/Documents/level editor/test/config')

tile_1 = pygame.Surface((32, 32))
tile_1.fill((0, 255, 0))
tile_2 = pygame.Surface((32, 32))
tile_2.fill((50, 50, 50))
tiles = [tile_1, tile_2]

run = True
while run:
    screen.fill((0, 0, 0))
    gameobjects.render_map(map, screen, config, tiles)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
            
