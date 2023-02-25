import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
rect = pygame.Rect(0, 0, 20, 20)
running = True
while running:
    time_elapsed = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if time_elapsed / 5000 > 1:
        rect.x += 5
    else: rect.x += 1
    if rect.x > 780:
        rect.x = 0
    
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), rect)
    font = pygame.font.SysFont('Arial', 18)
    text = font.render('Time Elapsed: {} ms'.format(time_elapsed), True, (0, 0, 0))
    screen.blit(text, (0, 40))
    pygame.display.update()
