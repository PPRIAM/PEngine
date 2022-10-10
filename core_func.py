import pygame

def load_imgs(loc, len):
  imgs = []
  for i in range(len):
    img = pygame.image.load(loc+str(i)+'.png')
    imgs.append(img)
  return imgs