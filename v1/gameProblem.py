## v2.2
## Javier Huertas (2017-18)
## Alejandro Cervantes (2017-18)
## To be used with python2.7
## Open source. Distributed as-is

'''
    Class gameProblem, implements simpleai.search.SearchProblem
'''


from simpleai.search import SearchProblem
# from simpleai.search import breadth_first,depth_first,astar,greedy
import simpleai.search

class GameProblem(SearchProblem):

    #
    # --------------------  INITIALIZATION, DO NOT INITIALIZE HERE  -------------------------
    #
    
    MAP=None
    POSITIONS=None
    INITIAL_STATE=None
    GOAL=None
    CONFIG=None
    AGENT_START=None


    #
    # --------------------  SOLUTION CODE (STUDENT)  -------------------------
    #
    
    
    def actions(self, state):
        
        '''Returns a LIST of the actions that may be executed in this state
        '''
        # acciones = ['North','East','South','West'] # Basic actions

        actionList = ['North','East','South','West']

        if state[0] + 1 >= self.CONFIG['map_size'][0]:
            actionList.remove('East')
        if state[0] - 1 < 0:
            actionList.remove('West')
        if state[1] + 1 >= self.CONFIG['map_size'][1]:
            actionList.remove('North')
        if state[1] - 1 < 0:
            actionList.remove('South')

        print("ACTIONS: " )
        print(actionList)
   
        return actionList
    

    def result(self, state, action):
        '''Returns the state reached from this state when the given action is executed
        '''
        print("INITIAL STATE: ")
        print(state)

        newState=None

        if action == 'North':
            newState = (state[0], state[1] + 1)
        elif action == 'East':
            newState = (state[0] + 1, state[1])
        elif action == 'South':
            newState = (state[0], state[1] - 1)
        elif action == 'West':
            newState = (state[0] - 1, state[1])

        print("NEW STATE: ")
        print(newState)

        return newState
    
    def is_goal(self, state):
        '''Returns true if state is the final state
        '''
        return self.GOAL == state

    def cost(self, state, action, state2):
        '''Returns the cost of applying `action` from `state` to `state2`.
           The returned value is a number (integer or floating point).
           By default this function returns `1`.
        '''
        return 1

    def heuristic(self, state):
        '''Returns the heuristic for `state`
        '''
        return 0


    def setup (self):
        initial_state = self.AGENT_START
        final_state = self.POSITIONS['goal'][0]
        algorithm = simpleai.search.breadth_first
            
        return initial_state,final_state,algorithm


        
    
    # --------------- DO NOT MODIFY FROM THIS LINE  -----------------
    def getAttribute (self, position, attributeName):
        '''Returns an attribute value for a given position of the map
           position is a tuple (x,y)
           attributeName is a string
           
           Returns:
               None if the attribute does not exist
               Value of the attribute otherwise
        '''
        tileAttributes=self.MAP[position[0]][position[1]][2]
        if attributeName in tileAttributes.keys():
            return tileAttributes[attributeName]
        else:
            return None
        
    # THIS INITIALIZATION FUNCTION HAS TO BE CALLED BEFORE THE SEARCH
    def initializeProblem(self,map,positions,conf,aiBaseName):
        
        # Loads the problem attributes: self.AGENT_START, self.POSITIONS,etc.
        if self.mapInitialization(map,positions,conf,aiBaseName):
    
            initial_state,final_state,algorithm = self.setup()
            
            self.INITIAL_STATE=initial_state
            self.GOAL=final_state
            self.ALGORITHM=algorithm
            super(GameProblem,self).__init__(self.INITIAL_STATE)
            
            return True
        else:
            return False
        
    # END initializeProblem 


    def mapInitialization(self,map,positions,conf,aiBaseName):
        # Creates lists of positions from the configured map
        # The initial position for the agent is obtained from the first and only aiBaseName tile
        self.MAP=map
        self.POSITIONS=positions
        self.CONFIG=conf

        if 'agentInit' in conf.keys():
            self.AGENT_START = tuple(conf['agentInit'])
        else:                    
            if aiBaseName in self.POSITIONS.keys():
                if len(self.POSITIONS[aiBaseName]) == 1:
                    self.AGENT_START = self.POSITIONS[aiBaseName][0]
                else:
                    print ('-- INITIALIZATION ERROR: There must be exactly one agent location with the label "{0}", found several at {1}'.format(aiAgentName,mapaPosiciones[aiAgentName]))
                    return False
            else:
                print ('-- INITIALIZATION ERROR: There must be exactly one agent location with the label "{0}"'.format(aiBaseName))
                return False
        
        return True
    

