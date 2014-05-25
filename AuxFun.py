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
    