import pygame
pygame.init()
display_widht = 600
display_heigh = 800
WHITE = (255,255,255)
BLACK =(0,0,0)
GRAY = (125,125,125)
GREEN= (0,200,64)
YELLOW= (225,225,0)
PINK = (230,50,230)
done = False
x= 100
y= 100
vol =10
PI =3.14

screen = pygame.display.set_mode((display_widht,display_heigh))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()

while not done:
    pygame.time.delay(50)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vol * 6 :
        x=x-vol
    if keys[pygame.K_RIGHT] and x < display_widht - vol * 6:
        x=x+vol
    if keys[pygame.K_UP] and y > vol * 6 :
        y=y-vol
    if keys[pygame.K_DOWN] and y < display_heigh - vol * 6 :
        y=y+vol

    screen.fill(BLACK)

    pygame.draw.circle(screen,PINK,(x,y),60)
    
   
    pygame.display.update()
	#clock.tick(60)

