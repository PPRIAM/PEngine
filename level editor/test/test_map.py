import pygame, sys, gameobjects

pygame.init()

screen = pygame.display.set_mode((256, 256))
pygame.display.set_caption("Test level editor map")

map = gameobjects.read_json('C:/Users/RE COMPUTER/Documents/level editor/test/map')
config = gameobjects.read_json('C:/Users/RE COMPUTER/Documents/level editor/test/config')

neon_tile = pygame.image.load("neon_tile.png")
tile = pygame.image.load("tile.png")
tiles = [neon_tile, tile]

player_img = pygame.Surface([32, 32])
player_img.fill((255, 255, 255))

scroll = [0, 0]
dir = {'left':False, 'right':False, 'jump':False}

run = True
while run:
    screen.fill((10, 10, 10))
    gameobjects.render_map(map, screen, config, tiles)
    hit_list = gameobjects.get_hit_list(map, config)



    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir['left'] = True
            if event.key == pygame.K_RIGHT:
                dir['right'] = True
            if event.key == pygame.K_UP:
                if not dir['jump']:
                    dir['jump'] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dir['left'] = False
            if event.key == pygame.K_RIGHT:
                dir['right'] = False
