from . agents import *
from copy import copy


# 'GoNorth' # sinistra
# 'GoEast', # giu'
# 'GoWest # su
# 'GoSouth' #destra


class AgentKSmart(Agent):
    
    def __init__(self):
        Agent.__init__(self) 

        self.counter = 0
        self.backTrack = False
        self.listMap = [[1,1,[],None,False]] # x,y,[lista mosse fatte da queste coordinate,(x,y) parent, ho pulito io
        self.listFinished = []
        self.listVisited = []
        self.listAction = [['GoNorth',0,-1,'GoSouth'],['GoEast',1,0,'GoWest'],['GoWest',-1,0,'GoEast'],['GoSouth',0,1,'GoNorth']]

        def nextOp():
            action = 'NoOp'
            if self.listMap != []:
                current = self.listMap.pop(-1)
                print current
                nextX = None
                nextY = None
                newMove = []
                nextParent = None
                

                if len(current[2]) != 4:
                    for i in self.listAction:
                        if i[0] not in current[2]:
                            nextX = current[0] + i[1]
                            nextY = current[1] + i[2]

                            if (nextX,nextY) not in self.listVisited:
                                newMove.append(i[3])
                                nextParent = (i[3])
                                current[2].append(i[0])
                                action = i[0]
                                self.listVisited.append((nextX,nextY))
                                self.backTrack = False
                                                        
                                self.listMap.append(current)
                                self.listMap.append([nextX,nextY,newMove,nextParent])
                                break

                            else:
                                for j in self.listMap:
                                    if j[0] == nextX and j[1] == nextY:
                                        j[2].append(i[3])
                                        self.backTrack = True

                    
                if self.backTrack == True:
                    preparaBack()
                    return current[3]

            return action

        def preparaBack():
            for i in self.listMap:
                for j in self.listAction:
                    if j[0] not in i[2]:
                        X = i[0]+j[1]
                        Y = i[1]+j[2]
                        for k in self.listMap:
                            if k[0] == X and k[1] == Y:
                                k[2].append(j[3])
                                i[2].append(j[0])
                        
                        
                    
            
        def program((status, bump)):

            if status == 'Dirty':
                try:
                    #self.listMap[-1][4] = True    #testare se migliora controllando che abbia mangiato io o meno in quella casella!
                    self.counter = 0
                    self
                    return 'Suck'
                except IndexError:
                    print '--------------------------------------------'
                    self.counter = 0
                    return 'Suck'

            if bump == 'Bump':
                self.backTrack = True
                mossa = self.listAction.pop(0)
                self.listAction.append(mossa)
                if self.listMap != []:
                    self.listMap.pop(-1)
                return nextOp()
                

            if status == 'Clean' and self.counter != 30:
                #print self.listMap[-1]
                #if self.listMap[-1][4] == False:
                #    mossa = self.listAction.pop(0)
                #    self.listAction.append(mossa) 
                self.counter += 1
                return nextOp()

            return 'NoOp'


        self.program = program
