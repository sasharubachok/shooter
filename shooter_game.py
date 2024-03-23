#Створи власний Шутер!

from pygame import *
import random 
window = display.set_mode((700,500)) 
bg = image.load("galaxy.jpg") 
bg = transform.scale(bg, (700,500)) 

game = True 
clock = time.Clock()  

mixer.init() 
space = mixer.Sound("space.ogg")

space.play()

class Hero(sprite.Sprite): 
    def __init__(self, x, y, width, height , speed, img_name="rocket.png"):  
        super().__init__()
        self.image = image.load(img_name) 
        self.image = transform.scale(self. image, (width, height))
        self.speed = speed 
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        
    def reset(self): 
        window.blit(self.image,(self.rect.x,self.rect.y)) 

class Bullet(Hero): 
    def move(self): 
        self.rect.y -= self.speed 
        if (self.rect.y < 0): 
             self.kill()

class Player(Hero): 
    def move (self): 
        keys = key.get_pressed() 
        if keys [K_a] and self.rect.x > 5: 
            self.rect.x -= self.speed 

        if keys [K_d] and self.rect.x < 650: 
            self.rect.x += self.speed 

     
    def fire(self): 
        bullet = Bullet(self.rect.x, self.rect.y, 10,10,10, 'bullet.png') 
        bullets.add(bullet)
counter = 0
killed = 0

bullets = sprite.Group()


 
class Enemy (Hero): 
    def move(self): 
        self.rect.y += self.speed 
        global counter  
        if self.rect.y > 560:
            counter += 1 
            self.rect.x = random.randint(50, 565) 
            self.speed = random.randint(1,4)
            self.rect.y = -100

rocket = Player(350,400,50,85,5)

enemys = sprite.Group() 
for i in range (5):
    enemy1 = Enemy (350, -100, 100, 50,random.randint(3,5),"ufo.png") 
    enemys.add(enemy1) 
font.init() 
lifes = 3
font1 = font.Font(None, 40)
finish = False
while game:
    
    for e in event.get(): 
        if e.type == QUIT: 
            game = False  
        if e.type == KEYDOWN: 
            if e.key == K_SPACE: 
                rocket.fire() 
                
    window.blit(bg,( 0,0)) 
    if finish != True:
        window.blit(font1.render(f"Лічильник:  {counter}",True, (255,255,255), (0,0,0)), (0,0)) 
        window.blit(font1.render(f"Життя:  {lifes}",True, (255,255,255), (0,0,0)), (0,100)) 
        window.blit(font1.render(f"Збиття:  {killed}",True, (255,255,255), (0,0,0)), (0,50)) 
        
        enemy1 = Enemy (350, -100, 150, 50,random.randint(3,5),"ufo.png")
        for i in enemys:
            i.reset() 
            i.move() 
        for b in bullets: 
            b.reset()   
            b.move()
    
        list_collaides = sprite.spritecollide(rocket,enemys,False) 
        for colide in list_collaides:
            if colide: 
                lifes -= 1
            for i in enemys: 
                i.rect.y = -100
                i.rect.x = random.randint(50, 565) 

            list_colides =   sprite.groupcollide(bullets, enemys , True, False) 
            for collide in list_colides: 
                if collide:
                    killed += 1
                    enemy1 = Enemy (random.randint(50, 565), -100, 100, 300, random.randint(1,4), "ufo.png")
                    enemys.add(enemy1)
        enemy1.reset()      
        enemy1.move()      
        rocket.reset() 
        rocket.move()
    clock.tick(60) 
    display.update() 
