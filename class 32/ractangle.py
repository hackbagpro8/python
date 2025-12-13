import pygame
pygame.init()

screen = pygame.display.set_mode((400,500))
screen.fill('beige')

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,"cyan",pygame.rect.Rect((100,160),(50,60)))
    pygame.display.update()
