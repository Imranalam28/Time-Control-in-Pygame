import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
rect = pygame.Rect(0, 0, 20, 20)
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    time = clock.get_time()
    fps = clock.get_fps()
    clock.tick_busy_loop(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    rect.x += 1
    if rect.x > 780:
        rect.x = 0
    
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), rect)
    font = pygame.font.SysFont('Arial', 18)
    text = font.render('Time taken: {} ms'.format(time), True, (0, 0, 0))
    text2 = font.render('FPS: {}'.format(fps), True, (0, 0, 0))
    screen.blit(text, (0, 20))
    screen.blit(text2, (0, 0))
    pygame.display.update()
