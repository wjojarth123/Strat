#imports
import pygame
# set vars
pygame.init()
fortlist=[]
print("made display")
screen = pygame.display.set_mode((800, 600))
def makeBasicLayout():
    screen.fill((0, 153, 51))
    rect=pygame.Rect(0,0,400,600)
    pygame.draw.rect(screen,(0,150,255),rect)
def checkFortCollision(fort):
        baserect=pygame.Rect(x-25,y-25,50,140)
        baserecthalf=pygame.Rect(x-25,y-25,50,50)
        baserect2=pygame.Rect(x-25,y-25,70,70)
def makeFort(x,y,c,t):
        wallrect=pygame.Rect(x-5,y+20,10,50)
        list=[]
        list.append(x,y,c,t)
        fortlist.append(list)
        if c==1:
            if t==1:
                pygame.draw.circle(screen,(102, 51, 0),(x,y),25)
            if t==2:
                pygame.draw.circle(screen,(102, 51, 0),(x,y),35)
        if c==2:
            if t==1:
                pygame.draw.circle(screen,(102, 51, 0),(x,y),25)
                pygame.draw.circle(screen,(102, 51, 0),(x,y+90),25)
                pygame.draw.rect(screen,(128, 128, 128),wallrect)
while True:
    print("in")
    for event in pygame.event.get():
        pass
    makeBasicLayout()
    makeFort(600,400,1,2)
    pygame.display.flip()
