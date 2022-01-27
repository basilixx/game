import pygame as py
import random
py.init()
window_h = 800
window_w = 1000
laps = 0
screen = py.display.set_mode((window_w, window_h))  # initialising screen

class Box:
    def __init__(self,r,g,b, x, y, w, h):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = (r,g,b)
        self.draw()
        
    def draw(self):
        py.draw.rect(screen, self.color, (self.x,self.y,self.w,self.h))

    def move(self, dir, vel = 2):
        if dir == "d":
            if self.y + self.h < window_h:
                self.y += vel

        if dir == "u":
            if self.y > 0:
                self.y -= vel
            else:
                self.y = window_h - self.h

        if dir == "r":
            if self.x + self.w < window_w:
                self.x += vel
            else:
                self.x = 0

        if dir == "l":
            if self.x > 0:
                self.x -= vel
            else:
                self.x = window_w - self.w

    def collision(self, box):
       if self.x < box.x + box.w and self.x + self.w > box.x and self.y < box.y + box.h and self.y + self.h > box.y:
        return True

class Enemy(Box):
    def __init__(self):
        self.color = (255,0,0)
        self.x = random.randrange(1, window_w)
        self.y = random.randrange(box1.h, window_h-50) 
        self.h = 10
        self.w = 10
        self.vel = 10
        self.alive = True
      
        
    def draw(self):
        py.draw.rect(screen, self.color, (self.x,self.y,self.w,self.h))

    def kill(self):
        self.x = 0
        self.y = 0
        self.h = 0
        self.w = 0
        self.alive = False

box1 = Box(100, 200,00,00, window_h - 40, 40, 40)

enemy = []
for i in range(20):
    enemy.append(Enemy())

run = True
while(run):
    for event in py.event.get():
        if event.type == py.QUIT:  # detecting QUIT event
            run = False

    keys = py.key.get_pressed() 
    if keys[py.K_UP]:
        box1.move("u") 
    if keys[py.K_DOWN]:
        box1.move("d")
    if keys[py.K_LEFT]:
        box1.move("l")
    if keys[py.K_RIGHT]:
        box1.move("r")

    screen.fill((30,30,30))
    box1.draw()

    for enemy_box in enemy:
        enemy_box.draw()
        
        enemy_box.move("r", 1)
        if enemy_box.collision(box1):
            run = False

    if box1.y == 0:
        laps += 1
        print("completed lap: ", laps)
    
    for enemy_box in enemy:
        if enemy_box.x == window_w - enemy_box.h:
            enemy_box.kill()

    for i in range(len(enemy)):
        if not enemy[i].alive:
            enemy[i] = Enemy()
            color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
            enemy[i].color = color

    py.display.update()

    py.display.flip()

py.quit()
    
