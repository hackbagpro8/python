import pygame
pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("pygame window")
screen.fill("teal")

bg_surf=pygame.transform.scale(pygame.image.load("panda.jpg").convert(),(400,400))

next_surf=pygame.transform.scale(pygame.image.load("panda_1.jpg").convert(),(400,400))

done=False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        screen.blit(bg_surf,(0,0))
        screen.blit(next_surf,(200,200))


    pygame.display.flip()
    
