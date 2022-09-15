import  pygame

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))

runing = True

while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

    pygame.display.update()