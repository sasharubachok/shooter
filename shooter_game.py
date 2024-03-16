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
        bullet.append(bullet)
counter = 0
bullets = []


 
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

enemys = [] 
for i in range (5):
 enemy1 = Enemy (350, -100, 100, 50,random.randint(3,5),"ufo.png") 
 enemys.append(enemy1) 
font.init() 

font1 = font.Font(None, 40)

while game:
    window.blit(bg,( 0,0)) 
    window.blit(font1.render(f"Лічильник:  (counter)",True, (255,255,255), (0,0,0)), (0,0)) 
    window.blit(font1.render(f"Збиття:  (counter)",True, (255,255,255), (0,0,0)), (0,0)) 
    
    enemy1 = Enemy (350, -100, 150, 50,random.randint(3,5),"ufo.png")
    for i in enemys:
        i.reset() 
        i.move() 
    for b in bullets: 
        b.reset()   
        b.move()
    for e in event.get(): 
        if e.type == QUIT: 
            game = False  
        if e.type == KEYDOWN: 
            if e.key == K_SPACE: 
                rocket.fire() 
                
    enemy1.reset()      
    enemy1.move()      
    rocket.reset() 
    rocket.move()
    clock.tick(60) 
    display.update()