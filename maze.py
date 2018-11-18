#!/usr/bin/env python3

import sys
from classArena import Arena
from classLaser import Laser

#Function to parse input file
#input is the path to the input text file
#output is arrays of grid size, position of player, and positions of mirrors
def parseInput(pathToInputFile):
    file = open(pathToInputFile, 'r')
    inputList = []
    for line in file: 
        inputList.append(line.split(' '))
    
    gridSize = [int(inputList[0][0]), int(inputList[0][1][0])]
    playerPos = [int(inputList[1][0]), int(inputList[1][1]), inputList[1][2][0]]
    mirrorForward = []
    mirrorBack = []
    
    if len(inputList) > 2:
        for i in range(2, len(inputList)):
            if inputList[i][2][0] == '/':
                mirrorForward.append([int(inputList[i][0]), int(inputList[i][1])])
            elif inputList[i][2][0] == '\\':
                mirrorBack.append([int(inputList[i][0]), int(inputList[i][1])])
    
    return (gridSize, playerPos, mirrorForward, mirrorBack)

#Function for writing output text file
#Input to function is number of traversed squares, end coordinate, and output file path
def writeOutput(numTraversedSquares, finalCoordinates, pathToOutput):
    outFile = open(pathToOutput, 'w') 
    outFile.write(str(numTraversedSquares) + '\n') 
    outFile.write(str(finalCoordinates[0]) + ' ' + str(finalCoordinates[1]))
    outFile.close()

#Algorithm process laser movement
#Input is Laser instance and arena instance (that specifies laser starting and arena layout)
def Solve(laser, arena):
    
    while not(arena.infiniteLoop(laser.posx, laser.posy, laser.compass) or arena.hitWall(laser.posx, laser.posy)):
        arena.addtoTraversed(laser.posx, laser.posy, laser.compass)
        #print(arena.traversed[-1])
        
        if arena.mirror(laser.posx, laser.posy) == 'F':
            laser.changeDir(arena.mirrorBounceForward(laser.compass))
            laser.move(laser.compass)
        elif arena.mirror(laser.posx, laser.posy) == 'B':
            laser.changeDir(arena.mirrorBounceBack(laser.compass))
            laser.move(laser.compass)
        else:
            laser.move(laser.compass)
            
    if arena.infiniteLoop(laser.posx, laser.posy, laser.compass):
        squares = -1
    else:
        squares = len(arena.traversed) - 1 #Do not count starting player square
        
    lastpos = arena.traversed[-1][0:2]
    
    return (squares, lastpos)

#Main function putting all functions together
def main():
    
    #Load input information
    arenaSize, playerPos, forwardSlash, backSlash = parseInput(sys.argv[1])
    
    #Initialize laser and arena objects
    lzr = Laser(playerPos[0], playerPos[1], playerPos[2])
    a = Arena(arenaSize[0], arenaSize[1], forwardSlash, backSlash)
    
    #Solve the challenge
    numSquares, coord = Solve(lzr, a)
    
    #Write output file
    writeOutput(numSquares, coord, sys.argv[2])


main()
