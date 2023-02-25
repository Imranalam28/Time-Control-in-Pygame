import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
rect = pygame.Rect(0, 0, 20, 20)
running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
   
   rect.x += 1
   if rect.x > 780:
      rect.x = 0
   
   screen.blit(background, (0, 0))
   pygame.draw.rect(screen, (0, 0, 0), rect)
   pygame.display.update()
