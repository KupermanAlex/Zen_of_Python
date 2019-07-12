import pygame
pygame.init()
gameDisplay=pygame.display.set_mode((500,300))
pygame.display.set_caption("My first game")
clock=pygame.time.Clock()
crashed=False
PI = 3.14
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           crashed = True
     
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
#quit()