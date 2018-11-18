class Arena:
    
    def __init__(self, arenaSizeX, arenaSizeY, forwardSlash, backSlash):
        self.traversed = []
        self.arenaX = arenaSizeX
        self.arenaY = arenaSizeY
        self.mirrorForward = forwardSlash
        self.mirrorBack = backSlash
        
    def addtoTraversed(self, x, y, direction):
        self.traversed.append([x, y, direction])
        
    def infiniteLoop(self, x, y, direction):
        check = [x, y, direction] in self.traversed
        return check
    
    def hitWall(self, x, y):
        checkx = (x < 0) or (x >= self.arenaX)
        checky = (y < 0) or (y >= self.arenaY)
        check = checkx or checky
        return check
    
    def mirror(self, x, y):
        mirrorType = None
        if [x, y] in self.mirrorForward:
            mirrorType = 'F'
        elif [x, y] in self.mirrorBack:
            mirrorType = 'B'
            
        return mirrorType
    
    def mirrorBounceForward(self, direction):
        if direction == 'N':
            newDir = 'E'
        elif direction == 'E':
            newDir = 'N'
        elif direction == 'S':
            newDir = 'W'
        elif direction == 'W':
            newDir = 'S'
        
        return newDir
    
    def mirrorBounceBack(self, direction):
        if direction == 'N':
            newDir = 'W'
        elif direction == 'W':
            newDir = 'N'
        elif direction == 'S':
            newDir = 'E'
        elif direction == 'E':
            newDir = 'S'
        
        return newDir
            