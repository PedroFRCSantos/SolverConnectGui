
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
linNum1 = -1;
linNum2 = -1;

colNum1 = -1;
colNum2 = -1;

initPoints = [];

indexCount = 0;
newPoint = True;
 
pygame.display.set_caption("Solver Connect Gui")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    
    numPress = -1;
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            
            pos = pygame.mouse.get_pos()
            print pos;
            
            if step == 2:
                dimTab = estimateDim(linNum1, linNum2, colNum1, colNum2);
                indNewPoint = estimatePosIJ(dimTab, pos);
                
                if indNewPoint[0] >= 0:
                    if newPoint:
                        indexCount = indexCount + 1;
                        newPoint = False;
                    else:
                        newPoint = True;
                    initPoints[indNewPoint[0]][indNewPoint[1]] = indexCount;
                    
                if estimateIfIsToProcess(pos, [round(dimTab[0]/2)*100 + 100, 10, 100, 70]):
                    print "Is to process"
                    writeFileToMainProgram(initPoints, dimTab, indexCount);
                    print "call external program"
                    os.system("SolverConnect.exe DataIn.txt")
                    print "read output file"
                    processResult = readSolutionFromFile(dimTab);
                    step = 3;

            elif step == 0 or step == 1:
                numPress = estimateButton(pos)
                print numPress;
                print pressOK(pos);
                step = changeMode(pos, step)
                print estimateDim(linNum1, linNum2, colNum1, colNum2);
            
                if pressOK(pos):
                    step = 2;
                    dimTab = estimateDim(linNum1, linNum2, colNum1, colNum2);
                    size = [100*dimTab[0] + 200, 100*dimTab[1] + 200];
                    screen = pygame.display.set_mode(size)
                    initPoints = generate2DMatrix(dimTab);
            
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    if step == 0 or step == 1:
        
        if numPress >= 0:
            if step == 0:
                if linNum1 < 0:
                    linNum1 = numPress;
                elif linNum2 < 0:
                    linNum2 = numPress;
            if step == 1:
                if colNum1 < 0:
                    colNum1 = numPress;
                elif colNum2 < 0:
                    colNum2 = numPress;
        
        basicfont = pygame.font.SysFont(None, 50)
        
        if step == 0:
            pygame.draw.rect(screen, BLUE, [90, 10, 80, 50], 2)
        else:
            pygame.draw.rect(screen, BLACK, [90, 10, 80, 50], 2)
            
        if linNum1 >= 0:
            text = basicfont.render(str(linNum1), True, (0, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = 120;
            textrect.centery = 30;
            screen.blit(text, textrect)
            
        if linNum2 >= 0:
            text = basicfont.render(str(linNum2), True, (0, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = 140;
            textrect.centery = 30;
            screen.blit(text, textrect)
        
        if colNum1 >= 0:
            text = basicfont.render(str(colNum1), True, (0, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = 260;
            textrect.centery = 30;
            screen.blit(text, textrect)
            
        if colNum2 >= 0:
            text = basicfont.render(str(colNum2), True, (0, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = 280;
            textrect.centery = 30;
            screen.blit(text, textrect)
        
        text = basicfont.render('X', True, (0, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = 200;
        textrect.centery = 40;
        screen.blit(text, textrect)
        
        if step == 1:
            pygame.draw.rect(screen, BLUE, [230, 10, 80, 50], 2)
        else:
            pygame.draw.rect(screen, BLACK, [230, 10, 80, 50], 2)
        
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
    
    if step == 2 or step == 3:
        dimTab = estimateDim(linNum1, linNum2, colNum1, colNum2);
        
        for i in range(dimTab[1]):
            for j in range(dimTab[0]):
                pygame.draw.rect(screen, BLACK, [j*100 + 100, i*100 + 100, 100, 100], 2)
                if initPoints[i][j] > 0:
                    pygame.draw.circle(screen, estimateColor(initPoints[i][j]), [j*100 + 100 + 50, i*100 + 100 + 50], 40)
                    
        pygame.draw.rect(screen, BLACK, [round(dimTab[0]/2)*100 + 100, 10, 100, 70], 2)
        basicfont = pygame.font.SysFont(None, 80)
        text = basicfont.render('OK', True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = round(dimTab[0]/2)*100 + 150;
        textrect.centery = 50;
        screen.blit(text, textrect)
        
    if step == 3:
        #print "draw result"
        for i in range(dimTab[1]):
            for j in range(dimTab[0]):
                if processResult[1][i][j] > -1:
                    
                    colorUsed = estimateColor(int(processResult[0][i][j]));
                    
                    # check if horizontal
                    if processResult[1][i][j] == i:
                        jMin = min(processResult[2][i][j], j);
                        pygame.draw.rect(screen, colorUsed, [jMin*100 + 100 + 50, i*100 + 100 + 25, 100, 50], 0)
                    else:
                        iMin = min(processResult[1][i][j], i);
                        pygame.draw.rect(screen, colorUsed, [j*100 + 100 + 25, iMin*100 + 100 + 25, 50, 150], 0)
    
    # This MUST happen after all the other drawing commands.
    pygame.display.flip();
 
# Be IDLE friendly
pygame.quit()
