import os

def estimateButton(posClick):
    num = 1;
    
    valX = posClick[0];
    valY = posClick[1];
    
    for i in range(3):
        for j in range(3):
            centerx = 100 + j*70
            centery = 100 + i*70
            
            if abs(centerx - valX) < 35 and abs(centery - valY) < 35:
                return num;
            
            num = num + 1;
            
    centerx = 100 + 1*70
    centery = 100 + 3*70
    
    if abs(centerx - valX) < 35 and abs(centery - valY) < 35:
        return 0;
            
    return -1;

def pressOK(posClick):
    
    valX = posClick[0];
    valY = posClick[1];
    
    if abs(valX - 105 - 120/2.0) < 120/2.0 and abs(valY - 370 - 70/2.0) < 70/2.0:
        return True;
    
    return False;

def changeMode(posClick, actMode):
    
    valX = posClick[0];
    valY = posClick[1];
    
    if actMode == 0 or actMode == 1:
        if valX < 90 + 80 and valX > 90 and valY < 10 + 50 and valY > 10:
            return 0;
        if valX < 230 + 80 and valX > 230 and valY < 10 + 50 and valY > 10:
            return 1;
    
    return actMode;

def estimateDim(linNum1, linNum2, colNum1, colNum2):
    dimX = 5;
    dimY = 5;
    
    if linNum2 < 0 and linNum1 >= 0:
        dimY = linNum1;
        
    if linNum2 >= 0 and linNum1 >= 0:
        dimY = 10*linNum1 + linNum2;
        
    if colNum2 < 0 and colNum1 >= 0:
        dimX = colNum1;
        
    if colNum2 >= 0 and colNum1 >= 0:
        dimX = 10*colNum1 + colNum2;
    
    return [dimX, dimY];

def generate2DMatrix(dim):
    
    a = [];
    for i in xrange(dim[1]):
        a.append([])
        for j in xrange(dim[0]):
            a[i].append(0)
            
    return a;

def estimatePosIJ(dim, posClick):
    
    val = [-1, -1];
    
    for i in range(dim[1]):
        for j in range(dim[0]):
            if posClick[0] > j*100 + 100 and posClick[0] < j*100 + 100 + 100 and posClick[1] > i*100 + 100 and posClick[1] < i*100 + 100 + 100:
                val = [i, j];
            
    return val;

def estimateColor(valIn):
    
    val = valIn;
    
    Red = 0;
    Green = 0;
    Blue = 0;
    
    for i in range(1, 6):
        if i == val:
            Red = i*51;
            return [Red, Green, Blue];
        
    val = val - 5;
    for i in range(1, 6):
        if i == val:
            Red = 255;
            Green = i*51;
            return [Red, Green, Blue];
        
    val = val - 5;
    for i in range(1, 6):
        if i == val:
            Red = 255;
            Green = 255;
            Blue = i*255;
            return [Red, Green, Blue];
    
    color = [Red, Green, Blue];
    
    return color;

def estimateIfIsToProcess(posClick, rect):
    
    if posClick[0] < rect[0] + rect[2] and posClick[0] > rect[0] and posClick[1] < rect[1] + rect[3] and posClick[1] > rect[1]:
        return True;
    
    return False;

def writeFileToMainProgram(board, boardSize, numberLines):
    
    f = open('DataIn.txt','w')
    
    f.write(str(boardSize[1]) + os.linesep)
    f.write(str(boardSize[0]) + os.linesep)
    
    f.write(str(numberLines) + os.linesep)
    
    for val in range(1, numberLines+1):
        for i in range(boardSize[1]):
            for j in range(boardSize[0]):
                if board[i][j] == val:
                    f.write(str(i+1) + os.linesep)
                    f.write(str(j+1) + os.linesep)
                    f.write(str(board[i][j]) + os.linesep)
    
    f.close()
    
