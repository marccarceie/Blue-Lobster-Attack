from pygame import *
from bullet import *

class Character(sprite.Sprite): #in the parentheses it is indicated that the class inherits from the Sprite class
    #creating the constructor
    bullets = sprite.Group()


    def __init__(self, image_path, x, y,width=64,height=64):
       sprite.Sprite.__init__(self) #mandatory calling of the constructor of the parent class
       # each sprite should store the image property—its image
       self.image = image.load(image_path)
       self.image = transform.scale(self.image, (width,height)) # resize the image
 
       # each sprite should store the rect property—the rectangle into which it is inscribed
       self.rect = self.image.get_rect() #we get a rectangle from the image
       #we set its location
       self.start_x = x
       self.start_y = y
       self.rect.x = x
       self.rect.y = y
    def shoot(self):
       self.bullets.add(Bullet(self.rect.x,self.rect.y))

   #method defining the sprite’s movement
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 200:
           self.rect.x -= 3
        if keys[K_RIGHT] and self.rect.x < 500-64:
           self.rect.x += 3
        if keys[K_DOWN] and self.rect.y < 540-64:
           self.rect.y += 3
        if keys[K_UP] and self.rect.y > 200+64:
           self.rect.y -= 3
        if keys[K_UP]:
           if keys[K_UP]:
              if keys[K_DOWN]:
                 if keys[K_DOWN]:
                    if keys[K_LEFT]:
                       if keys[K_RIGHT]:
                          if keys[K_LEFT]:
                             if keys[K_RIGHT]:
                                if keys[K_b]:
                                   if keys[K_a]:
                                      self.rect.x+=500
                                      print("Cheat code activated: invincibility")
         
        self.bullets.update()
        for bullet in self.bullets:
           if bullet.getY() > 805:
              bullet.kill()

    def reset_position(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
    