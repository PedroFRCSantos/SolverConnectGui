
# Import a library of functions called 'pygame'
import pygame
from AuxFun import *
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [370, 450]
screen = pygame.display.set_mode(size)

step = 0;
 
pygame.display.set_caption("Solver Connect Gui")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print pos;
            print estimateButton(pos);
            print pressOK(pos);
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    if step == 0 or step == 1 or step == 2:
        
        basicfont = pygame.font.SysFont(None, 50)
        
        num = 1;
        
        # print numbers
        for i in range(3):
            for j in range(3):
                text = basicfont.render(str(num), True, (255, 0, 0), (255, 255, 255))
                textrect = text.get_rect()
                textrect.centerx = 100 + j*70
                textrect.centery = 100 + i*70
                screen.blit(text, textrect)
                pygame.draw.rect(screen, BLACK, [textrect.centerx - 35, textrect.centery - 35, 70, 70], 2)
                num = num + 1;
        
        text = basicfont.render('0', True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = 100 + 1*70;
        textrect.centery = 100 + 3*70;
        screen.blit(text, textrect)
        pygame.draw.rect(screen, BLACK, [textrect.centerx - 35, textrect.centery - 35, 70, 70], 2)
        
        # ok button
        basicfont = pygame.font.SysFont(None, 90)
        pygame.draw.rect(screen, BLACK, [105, 370, 120, 70], 2)
        text = basicfont.render('OK', True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = 105 + 120/2.0;
        textrect.centery = 370 + 70/2.0;
        screen.blit(text, textrect)
    
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
