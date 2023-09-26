import pygame
import time
import random

WIDTH, HEIGHT = 800 , 700

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Demo Game")
BG = pygame.transform.scale(pygame.image.load("bg.jpg"),(WIDTH,HEIGHT))
PLAYER_WIDTH, PLAYER_HEIGHT = 30,50

def draw(player):
    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN,"red",player)
    pygame.display.update()
    
def main():
    run = True
    
    player = pygame.Rect(200,HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(player)
            
    pygame.quit()
    
if __name__ == "__main__":
    main()