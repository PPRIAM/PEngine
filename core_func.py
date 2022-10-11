import pygame

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
