from . agents import *
from copy import copy


class AgentK(Agent):
    
    def __init__(self):
        Agent.__init__(self) 

        self.counter = 0
        self.backTrack = False
        self.listMap = [(0,0,[])] # x,y,[lista mosse fatte da queste coordinate
        self.listFinished = []
        self.listAction = [['GoNorth',0,1,'GoSouth'],['GoEast',1,0,'GoWest'],['GoWest',-1,0,'GoEast'],['GoSouth',0,-1,'GoNorth']]

        def nextOp():
            action = 'NoOp'
            if self.listMap != []:
                current = self.listMap.pop(-1)
                print current
                nextX = None
                nextY = None
                newMove = []

                for i in self.listAction:
                    if i[0] not in current[2]:
                        nextX = current[0] + i[1]
                        nextY = current[1] + i[2]
                        current[2].append(i[0])

                        if (nextX,nextY) in self.listFinished:
                            print 'sono qui'    
                        newMove.append(i[3])
                        action = i[0]

                        self.listMap.append(current)

                        for j in range(0,len(self.listMap)):
                            if (self.listMap[j][0] == nextX and self.listMap[j][1] == nextY):
                                self.listMap[j][3].append(i[3])
                                newMove = self.listMap[j][3]

                        self.listMap.append((nextX,nextY,newMove))
                        return action

                self.backTrack = True
                return action
                    
            
        def program((status, bump)):
            stop = False

            if status == 'Dirty':
                self.counter = 0
                return 'Suck'

            if bump == 'Bump':
                fail = self.listAction.pop(-1)
                self.listFinished.append((fail[0],fail[1]))
                return nextOp()
                

            if status == 'Clean' and stop == False:
                if self.counter == 100:
                    stop = True
                    return 'NoOp'
                else:
                    self.counter += 1
                    return nextOp()
            
            #return 'NoOp'


        self.program = program
