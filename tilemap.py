import core_func, pygame

class Tilemap:
  def __init__(self, tileset, map):
    self.tileset = tileset
    self.tiles = [self.tileset[k] for k in self.tileset]
    self.tiles_id = [int(k) for k in self.tileset]
    self.map = core_func.read_json(map)

  def render(self, display, data, offset):
    core_func.render_map(self.map, display, data, self.tiles, offset)

  def get_hit_list(self, data):
    tile_list = []
    y = 0
    for c in self.map:
      x = 0
      for l in c:
        if l in self.tiles_id:
          tile_list.append(pygame.Rect(x*data['screen']['Tilewidth'], y*data['screen']['Tileheight'], data['screen']['Tilewidth'], data['screen']['Tileheight']))
        x += 1
      y += 1
    return tile_list
    