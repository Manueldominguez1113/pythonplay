import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Simple Game")
running = True

while running:
    pygame.display.update()
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()