from pygame import *
class Enemy(sprite.Sprite):
    def __init__(self, image_path, x, y,width=64,height=64):
       sprite.Sprite.__init__(self) 

       self.image = image.load(image_path)
       self.image = transform.scale(self.image, (width,height))

       self.rect = self.image.get_rect()

       self.start_x = x
       self.start_y = y
       self.rect.x = x
       self.rect.y = y