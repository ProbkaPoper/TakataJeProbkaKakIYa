import pygame
pygame.init()
screen = pygame.display.set_mode((2500,1310))
pygame.display.set_caption("4.3.1")
screen.fill('orange')
bg = pygame.image.load('img0-1-2-740x555.jpg')
a = pygame.image.load('ico.png')
pygame.display.set_icon(a)
pygame.transform.scale(bg,(2560,1440))
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg,(900,300))
    pygame.display.update()
