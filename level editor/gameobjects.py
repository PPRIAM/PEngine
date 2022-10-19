import math, random, pygame, json

pygame.init()

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
class XVector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def info(self):
		print(self.x, self.y)

	def add(self, v):
		self.x = self.x + v.x
		self.y = self.y + v.y

	def adds(self, v):
		self.x = self.x + v.x
		self.y = self.y + v.y
		return XVector(self.x, self.y)

	def sub(self, v):
		self.x = self.x - v.x
		self.y = self.y - v.y

	def subs(self, v):
		self.x = self.x - v.x
		self.y = self.y - v.y
		return XVector(self.x, self.y)

	def mult(self, n):
		self.x = self.x * n
		self.y = self.y * n

	def mults(self, n):
		self.x = self.x * n
		self.y = self.y * n
		return XVector(self.x, self.y)

	def div(self, n):
	 	self.x /= n
	 	self.y /= n

	def divs(self, n):
	 	self.x /= n
	 	self.y /= n
	 	return XVector(self.x, self.y)

	def mag(self):
	 	return math.sqrt(self.x**2+self.y**2)

	def normalize(self):
	 	m = self.mag()
	 	if m != 0:
	 		self.div(m)

	def limit(self, max):
	    if self.mag() > max:
	    	self.normalize()
	    	self.mult(max)
	def get(self):
	    return XVector(self.x, self.y)
