p1x = 100
p1y = 100
import pygame
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((700,700))
window.fill((255, 255, 255))
#maze
pygame.draw.line(window, (0, 0, 0), [100, 300], [500, 300], 1)
pygame.draw.line(window, (0, 0, 0), [500, 300], [500, 600], 1)
pygame.draw.line(window, (0, 0, 0), [500, 600], [650, 600], 1)
pygame.draw.line(window, (0, 0, 0), [650, 600], [650, 100], 1)
pygame.draw.line(window, (0, 0, 0), [30, 300], [30, 600], 1)

#maze
rect1 = pygame.Rect(100,100,10,10)
rect2 = pygame.Rect(200,200,10,10)
pygame.draw.rect(window, (255, 0, 0),rect1)
pygame.draw.rect(window, (0, 255, 0),rect2)

pygame.display.update()

#run until quit
run =True
delayy = 15
while run:
    delayy = 20
    pygame.draw.rect(window, (255, 255, 255), rect1)
    pygame.draw.rect(window, (255, 255, 255), rect2)
    #for event in pygame.event.get():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    k1 = 1
    k2 = 1
    k3 = 1
    k4 = 1
    kk1 =1
    kk2 =1
    kk3 =1
    kk4 = 1
    kkk1 =1
    kkk2 =1
    kkk3 =1
    kkk4 = 1
    close_x = 1 #how close are they two, and how should the police move is decided by this
    close_y = 1 #how close are they two, and how should the police move is decided by this
    for i in range(11):
        if pygame.Surface.get_at(window,(rect1.centerx-5+i,rect1.centery-6)) != (255,255,255) or pygame.Surface.get_at(window,(rect1.centerx-5+i,rect1.centery-7)) != (255,255,255) :
            k1=0
        if (rect1.centery-8)<0 :
            k1=0
    for i in range(11):
        if pygame.Surface.get_at(window,(rect1.centerx-5+i,rect1.centery+6)) != (255,255,255) or pygame.Surface.get_at(window,(rect1.centerx-5+i,rect1.centery+7)) != (255,255,255) :
            k2=0
        if (rect1.centery+10)>700 :
            k2=0
    for i in range(11):
        if pygame.Surface.get_at(window,(rect1.centerx+6,rect1.centery-5+i)) != (255,255,255) or pygame.Surface.get_at(window,(rect1.centerx+7,rect1.centery-5+i)) != (255,255,255) :
            k3=0
        if (rect1.centerx+10)>700 :
            k3=0
    for i in range(11):
        if pygame.Surface.get_at(window,(rect1.centerx-6,rect1.centery-5+i)) != (255,255,255) or pygame.Surface.get_at(window,(rect1.centerx-7,rect1.centery-5+i)) != (255,255,255) :
            k4=0
        if (rect1.centerx-8)<0:
            k4=0
    for i in range(11):
        if pygame.Surface.get_at(window,(rect2.centerx-5+i,rect2.centery-6)) != (255,255,255) or pygame.Surface.get_at(window,(rect2.centerx-5+i,rect2.centery-7)) != (255,255,255) :
            kk1=0
        if (rect2.centery-8)<0 :
            kkk1=0
    for i in range(11):
        if pygame.Surface.get_at(window,(rect2.centerx-5+i,rect2.centery+6)) != (255,255,255) or pygame.Surface.get_at(window,(rect2.centerx-5+i,rect2.centery+7)) != (255,255,255) :
            kk2=0
        if (rect2.centery+8)>700 :
            kkk2=0
    for i in range(11):
        if pygame.Surface.get_at(window,(rect2.centerx+6,rect2.centery-5+i)) != (255,255,255)  or pygame.Surface.get_at(window,(rect2.centerx+7,rect2.centery-5+i)) != (255,255,255):
            kk3=0
        if (rect2.centerx+8)>700 :
            kkk3=0
    for i in range(11):
        if pygame.Surface.get_at(window,(rect2.centerx-6,rect2.centery-5+i)) != (255,255,255) or  pygame.Surface.get_at(window,(rect2.centerx-7,rect2.centery-5+i)) != (255,255,255):
            kk4=0
        if (rect2.centerx-8)<0:
            kkk4=0
    if (rect1.centerx-rect2.centerx)> 0 :
        close_x = 1
    else :
        close_x = -1
    if (rect1.centery-rect2.centery)> 0 :
        close_y = 1
    else :
        close_y = -1
    if (kk1==0 or kkk1 == 0) and close_y<0:
        close_y=0
    if (kk2==0 or kkk2 ==0) and close_y>0:
        close_y=0
    if (kk3==0 or kkk3==0) and close_x>0:
        close_x=0
    if (kk4==0 or kkk4 ==0) and close_x<0:
        close_x=0


    pygame.Rect.move_ip(rect2,close_x,close_y)



    if pygame.key.get_pressed()[pygame.K_UP] and k1!=0 :
        pygame.Rect.move_ip(rect1, 0, -2)
        delayy = 20
    if pygame.key.get_pressed()[pygame.K_DOWN] and k2!=0:
        pygame.Rect.move_ip(rect1, 0, 2)
        delayy = 20
    if pygame.key.get_pressed()[pygame.K_RIGHT] and k3!=0:
        pygame.Rect.move_ip(rect1, 2, 0)
        delayy =20
    if pygame.key.get_pressed()[pygame.K_LEFT] and k4!=0:
        pygame.Rect.move_ip(rect1, -2, 0)
        delayy = 20
    pygame.draw.rect(window, (255, 0, 0), rect1)
    pygame.draw.rect(window, (0, 255, 0), rect2)
    pygame.display.update()
    if abs(rect1.centerx-rect2.centerx)<10 and abs(rect1.centery-rect2.centery)<10:
        print("game over")
        delayy = 1000
        run = False
    pygame.time.delay(delayy)
#run until quit
