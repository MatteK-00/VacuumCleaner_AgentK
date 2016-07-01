from . agents import *
from copy import copy


class AgentK3(Agent):
    
    def __init__(self):
        Agent.__init__(self) 

        self.counter = 0
        self.backTrack = False
        self.listMap = [(0,0,[],None)] # x,y,[lista mosse fatte da queste coordinate,(x,y) parent
        self.listFinished = []
        self.listVisited = []
        self.listAction = [['GoNorth',0,1,'GoSouth'],['GoEast',1,0,'GoWest'],['GoWest',-1,0,'GoEast'],['GoSouth',0,-1,'GoNorth']]

        def nextOp():
            action = 'NoOp'
            if self.listMap != []:
                current = self.listMap.pop(-1)
                print current
                nextX = None
                nextY = None
                newMove = []
                nextParent = None
                action = None

                if len(current[2]) != 4:
                    self.backTrack = False
                    for i in self.listAction:
                        if i[0] not in current[2]:
                            nextX = current[0] + i[1]
                            nextY = current[1] + i[2]

                            if (nextX,nextY) not in self.listVisited:
                                print 'sono qui 1'    
                                newMove.append(i[3])
                                nextParent = (current[0],current[1])
                                current[2].append(i[0])
                                action = i[0]
                                self.listVisited.append((nextX,nextY))
                                break
                elif current[3] == None:
                    return 'NoOp'
                else:
                    self.backTrack = True
                    for i in self.listAction:
                        nextX = current[0] + i[1]
                        nextY = current[1] + i[2]
                        if (nextX,nextY) == current[3]:
                            return i[0]
                        
                self.listMap.append(current)
                self.listMap.append((nextX,nextY,newMove,nextParent))   

            return action
                    
            
        def program((status, bump)):

            if status == 'Dirty':
                self.counter = 0
                return 'Suck'

            if bump == 'Bump':
                if self.listMap != []:
                    self.listMap.pop(-1)
                return nextOp()
                

            if status == 'Clean' and self.counter != 20:
                self.counter += 1
                return nextOp()

            return 'NoOp'


        self.program = program
