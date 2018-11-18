class Laser:
    
    def __init__(self, x, y, direction):
        self.posx = x
        self.posy = y
        self.compass = direction
        
    def changeDir(self, newDir):
        self.compass = newDir
        
    def move(self, enterDir):
        if enterDir == 'N':
            self.posy = self.posy + 1
        elif enterDir == 'S':
            self.posy = self.posy - 1
        elif enterDir == 'W':
            self.posx = self.posx - 1
        elif enterDir == 'E':
            self.posx = self.posx + 1
        else:
            print('Incorrect Direction')