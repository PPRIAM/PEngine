import pygame, json

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def read_json(filename):
	with open(filename+'.json') as f:
		content = json.loads(f.read())
	return content

def write_json(data, filename, tab=0):
	with open(filename+'.json', 'w') as f:
		f.write(json.dumps(data, indent=tab))

def debug(debug, screen, antialias = True, x=0, y=0, color=(255, 255, 255), background= None):
	font = pygame.font.SysFont('calibri', 16, True)
	screen.blit(font.render(str(debug[0])+':'+str(debug[1]), antialias, color, background), (x, y))

def create_grid(data):
	list = []
	for c in range(data['screen']['height']//data['screen']['Tileheight']):
		list.append([])
		for l in range(data['screen']['width']//data['screen']['Tilewidth']):
			list[c].append(0)
	return list

def get_hit_list(map, data):
        tile_list = []
        y = 0
        for c in map:
                x = 0
                for l in c:
                        if l in [1, 2]:
                                tile_list.append(pygame.Rect(x*data['screen']['Tilewidth'], y*data['screen']['Tileheight'], data['screen']['Tilewidth'], data['screen']['Tileheight']))
                        x += 1
                y += 1
        return tile_list

def render_map(map, screen, data, tiles, offset):
	tilemap = map
	y = 0
	for c in tilemap:
		x = 0
		for l in c:
			if l == 1:
				screen.blit(pygame.image.load(tiles[0]+".png").convert(), (x*data['screen']['Tilewidth']-offset[0], y*data['screen']['Tileheight']-offset[1]))
			if l == 2:
				screen.blit(pygame.image.load(tiles[1]+".png").convert(), (x*data['screen']['Tilewidth']-offset[0], y*data['screen']['Tileheight']-offset[1]))
			x += 1
		y += 1

def render_grid(grid, screen, data, tiles):
	tilemap = grid
	y = 0
	for c in tilemap:
		x = 0
		for l in c:
			pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x*data['screen']['Tilewidth'], y*data['screen']['Tileheight'], data['screen']['Tilewidth'], data['screen']['Tileheight']), 1)

			if l == 1:
				screen.blit(tiles[0], (x*data['screen']['Tilewidth'], y*data['screen']['Tileheight']))
			if l == 2:
				screen.blit(tiles[1], (x*data['screen']['Tilewidth'], y*data['screen']['Tileheight']))
			if l == 3:
				screen.blit(tiles[2], (x*data['screen']['Tilewidth'], y*data['screen']['Tileheight']))
			x += 1
		y += 1

def load_img(loc, name):
  return pygame.image.load(loc+name+".png")

def load_particle(loc, len):
  imgs = []
  for i in range(len):
    img = pygame.image.load(loc+str(i)+'.png')
    imgs.append(img)
  return imgs

def load_imgs(loc, name, len):
  imgs = []
  for i in range(len):
    img = pygame.image.load(loc+"/"+name+str(i)+'.png')
    imgs.append(img)
  return imgs

def flip(image, left=False, right=False):
  image_copy = image.copy()
  image_copy = pygame.transform.flip(image_copy, left, right)
  return image_copy

def flips(image_list, lefts=False, rights=False):
  images = []
  for i in image_list:
    images.append(flip(i, lefts, rights))
  return images
def load_animation(sprite_name, anim_type):
  anim = {}
  for n in range(len(anim_type)):
    anim[anim_type[n][0]] = load_imgs("static/animations/"+sprite_name+"/"+anim_type[n][0], sprite_name+"-"+anim_type[n][0]+"-", anim_type[n][1])
    anim[anim_type[n][0]+"left"] = flips(load_imgs("static/animations/"+sprite_name+"/"+anim_type[n][0], sprite_name+"-"+anim_type[n][0]+"-", anim_type[n][1]), True)
  return anim

aT = [["die", 7], ["fall", 2], ["idle", 3], ["jump", 4], ["run", 6]]
anim = load_animation('adventurer', aT)
print(k for k in anim)
