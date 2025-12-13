import pygame
pygame.init()

x=100
y=100

screen = pygame.display.set_mode((400,500))
done=False

while not done:
    screen.fill('red')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y=y-5
        if pressed[pygame.K_DOWN]:
            y=y+5
        if pressed[pygame.K_LEFT]:
            x=x-5
        if pressed[pygame.K_RIGHT]:
            x=x+5
    pygame.draw.rect(screen,"cyan",((x,y),(50,60)))
    pygame.display.update()
