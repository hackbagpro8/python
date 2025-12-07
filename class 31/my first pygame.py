import pygame
pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("pygame window")
screen.fill("teal")

done=False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    pygame.display.flip()