from . agents import *
from copy import copy


class AgentK(Agent):
    
    def __init__(self):
        Agent.__init__(self) 

        self.counter = 0
        self.listMap = [[0,0,False,False,False,False]] # x,y,North,Est,West,South
        self.ListAction = ['GoNorth','GoEast','GoWest','GoSouth']

        def nextOp(current):
            action = 'NoOp'
            if current != []:
                nextX = None
                nextY = None
                nextMove = None
                
                if current[2] == False:
                    current[2] = True
                    nextX = current[0]
                    nextY = current[1] + 1
                    nextMove = [False,False,False,True]
                    action = 'GoNorth'  
                elif current[3] == False:
                    current[3] = True
                    nextX = current[0] + 1
                    nextY = current[1]
                    nextMove = [False,False,True,False]
                    action = 'GoEast'
                elif current[4] == False:
                    current[4] = True
                    nextX = current[0] - 1
                    nextY = current[1]
                    nextMove = [False,True,False,False]
                    action = 'GoWest'
                elif current[5] == False:
                    current[5] = True
                    nextX = current[0]
                    nextY = current[1] - 1
                    nextMove = [True,False,False,False]
                    action = 'GoSouth'
                else:
                    action = 'NoOp'
                
                self.listMap.append(current)

                for i in range(0,len(self.listMap)):
                    if (self.listMap[i][0] == nextX and self.listMap[i][1] == nextY):
                        old = self.listMap.pop(i)
                        for j in range(2,5):
                            if old[j] == True:
                                nextMove[j-2] = True
                                break

                if action != 'NoOp':        
                    self.listMap.append([nextX,nextY] + nextMove)
                                    
            return action
            
        def program((status, bump)):
            stop = False

            if status == 'Dirty':
                self.counter = 0
                return 'Suck'

            if bump == 'Bump':
                self.listMap.pop(-1)
                if self.counter == 20:
                    stop = True
                    return 'NoOp'
            else:
                self.counter += 1
            return (nextOp(self.listMap.pop(-1)))

            if status == 'Clean' and stop == False:
                if self.counter == 20:
                    stop = True
                    return 'NoOp'
                else:
                    self.counter += 1
                    return (nextOp(self.listMap.pop(-1)))
            
            #return 'NoOp'


        self.program = program
