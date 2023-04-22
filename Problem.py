class Problem:
    def __init__(self,initialState, goalState):
        self.initial_state = initialState
        self.goal_state = goalState
        self.operators = ["move up", "move down", "move left", "move right"]

    def actions(self, currentState):
        possibleActions = []
        possibleActions.append(self.moveUp(currentState))
    
    def goal_test(self,state):
        if state == self.goal_state:
            return True
        else:
            return False
    
    def moveUp(self,state):
        copyState = state
        indexValue = copyState.index(0)
        if indexValue not in copyState[0:3]:
            tempVal = copyState[indexValue - 1]
            copyState[indexValue - 1] = copyState[indexValue]
            copyState[indexValue] = tempVal
            return copyState
        
        else:
            return None
