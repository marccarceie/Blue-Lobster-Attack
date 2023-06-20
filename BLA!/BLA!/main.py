import pygame
import heart
import shartizard
import enemy
import bullet
import random
import time
import end
round=0
pygame.init()
name=input("What is your name?\n")
print(name+". That is a nice name.")
time.sleep(2)
def intro():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Blue Lobster OSv2 Mainframe\n\n")
    pygame.time.wait(1500)
    print("Welcome, Jacob!")
    pygame.time.wait(1500)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou turn around.")
    pygame.time.wait(1500)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Jacob: Hello",name,".")
    pygame.time.wait(1200)
    print("Jacob: I should have killed you when I had the chance. Now you're stronger. But I am still stronger than you. I challange you to a fight.")
    pygame.time.wait(2000)
    print(name,": I accept.")
    pygame.time.wait(1000)
intro()
pygame.mixer.music.load('music/Toccata & Fugue D Minor, BWV 565.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
pygame.display.set_caption('Blue Lobster Attack!')
def boundaries():
    color=(255,255,255)
    bound=pygame.draw.rect(screen, color, pygame.Rect(200-5, 250, 320, 300),  2)
screen=pygame.display.set_mode((800,600))
character = heart.Character('assets/heart_char.jpg',300,400,)
youdied = heart.Character('assets/youdied.jpg',0,0,800,600)
shartizard1=enemy.Enemy('assets/Jacob.png',250,50,200,200)
bullet1=bullet.Bullet(random.randint(200,500-64),200,32,54)
bullet2=bullet.Bullet(200,random.randint(200,500-64),32,54)
sprite_group = pygame.sprite.Group()
sprite_group.add(bullet1)
sprite_group.add(bullet2)
sprite_group.add(shartizard1)
sprite_group.add(character)
sprite_group.draw(screen)
run=True
start=time.time()
while run:

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False
    dt=pygame.time.delay(10)
    fin=time.time()
    if fin-start==15:
        end.end()
        sprite_group.add(bullet2)
    character.update()
    bullet1.update()
    bullet2.update()
    pygame.display.set_caption(str(round))
    screen.fill((0,0,0)) #comment this and see what hapen
    boundaries()
    a=random.randint(5,6)
    sprite_group.draw(screen)
    if pygame.sprite.collide_rect(bullet1,character):
        pygame.display.set_caption(str(round))
        character.kill()
        sprite_group.add(youdied)
        sprite_group.draw(screen)
    if bullet1.getY() > 600:
        bullet1.rect.y = 200
        bullet1.rect.x=random.randint(200,500-64)
        round+=1
    if pygame.sprite.collide_rect(bullet2,character):
        pygame.display.set_caption(str(round))
        character.kill()
        sprite_group.add(youdied)
        sprite_group.draw(screen)
    if bullet2.getY() > 600:
        bullet2.rect.y = 200
        bullet2.rect.x=random.randint(200,500-64)
        round+=1
    pygame.display.update()
quit()