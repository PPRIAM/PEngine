import pygame, sys, gameobjects

data = gameobjects.read_json('C:/Users/RE COMPUTER/Documents/level editor/config')

pygame.init()
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((256, 480), pygame.RESIZABLE)
pygame.display.set_caption('Level Editor')



data['tilemap'] =  gameobjects.create_grid(data)
data['id'] = [0, 1, 2]

menu = pygame.Surface((480, 480-256))
menu.fill((50, 50, 50))
neon_tile = pygame.image.load("neon_tile.png")
tile = pygame.image.load("tile.png")

tiles = [neon_tile, tile]

selected = data['id'][1]

overing = [0, 0]

grid_surf = pygame.Surface((data['screen']['width'], data['screen']['height']))
grid_surf.fill((50, 50, 50))

print(data)

run = True
while run:
    screen.fill((50, 50, 50))
    screen.blit(grid_surf, (0, 0))
    screen.blit(menu, (0, data['screen']['height']))
    for i in range(len(tiles)):
        menu.blit(tiles[i], (i*data['screen']['width'], 0))



    mousePos = pygame.mouse.get_pos()
    gameobjects.render_grid(data['tilemap'], grid_surf, data, tiles)
    if grid_surf.get_rect().collidepoint(mousePos):
        overing = [mousePos[0]//data['screen']['Tilewidth'], mousePos[1]//data['screen']['Tileheight']]

    # Debug
    gameobjects.debug(['Mouse', mousePos], menu,y = data['screen']['Tileheight'], background=(0, 0, 0))
    gameobjects.debug(['Mouse Over', str(overing[0])+','+str(overing[1])], menu, y=data['screen']['Tileheight']+16, background=(0, 0, 0))
    gameobjects.debug(['Selected', selected], menu,y = data['screen']['Tileheight']+32, background=(0, 0, 0))
    gameobjects.debug(['...', data['tilemap'][overing[1]][overing[0]]], menu, y = data['screen']['Tileheight']+48, background=(0, 0, 0))

    pygame.display.flip()

    gameobjects.write_json(data, 'C:/Users/RE COMPUTER/Documents/level editor/config', 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if selected > 0:
                    selected -= 1
            if event.key == pygame.K_RIGHT:
                if selected < len(data['id'])-1:
                    selected += 1
            if event.key == pygame.K_s:
                gameobjects.write_json(data['tilemap'], 'C:/Users/RE COMPUTER/Documents/level editor/map')


        if event.type == pygame.MOUSEBUTTONDOWN:
            if grid_surf.get_rect().collidepoint(mousePos):

                data['tilemap'][overing[1]][overing[0]] = selected
