import pegSolitaireUtils

'''
ItrDeepSearch function is used here to call IDS function to perform iterative deepening search.
It takes the initial state object and checks for goal state solution.
'''	
def ItrDeepSearch(pegSolitaireObject):
	'''
	#################################################
	# Must use functions:
	# getNextState(self,oldPos, direction)
	# 
	# we are using this function to count,
	# number of nodes expanded, If you'll not
	# use this grading will automatically turned to 0
	#################################################
	#
	# using other utility functions from pegSolitaireUtility.py
	# is not necessary but they can reduce your work if you 
	# use them.
	# In this function you'll start from initial gameState
	# and will keep searching and expanding tree until you 
	# reach goal using Iterative Deepning Search.
	# you must save the trace of the execution in pegSolitaireObject.trace
	# SEE example in the PDF to see what to save
	#
	#################################################
	'''
	
	trace_list = []
	for h in range(33):
		flag=IDS(pegSolitaireObject, h, trace_list)
		if flag:
			trace_list.reverse()
			pegSolitaireObject.trace= trace_list	
			return True

'''
IDS function performs depth controlled search on any given state and keeps appending the moves made in trace_list.
'''
def IDS(pegSolitaireObject, h, trace_list):
	
	if isGameState(pegSolitaireObject):
		return True
	
	if h==0:
		return False
	
	for i in range(7):
		for j in range(7):
			if pegSolitaireUtils.game.is_validMove(pegSolitaireObject, [i,j], "N") is not None:
				new=pegSolitaireUtils.game.getNextState(pegSolitaireObject, [i,j], "N"); 
				if new is not None:					
					if(IDS(new, h-1, trace_list)):
						trace_list.append([i-2,j])
						trace_list.append([i,j])						
						return True	
					
			if pegSolitaireUtils.game.is_validMove(pegSolitaireObject, [i,j], "S") is not None:
				new=pegSolitaireUtils.game.getNextState(pegSolitaireObject, [i,j], "S");
				if new is not None:					
					if(IDS(new, h-1, trace_list)):
						trace_list.append([i+2,j])
						trace_list.append([i,j])						
						return True
					
			if pegSolitaireUtils.game.is_validMove(pegSolitaireObject, [i,j], "E") is not None:
				new=pegSolitaireUtils.game.getNextState(pegSolitaireObject, [i,j], "E");
				if new is not None:					
					if(IDS(new, h-1, trace_list)):
						trace_list.append([i,j+2])
						trace_list.append([i,j])
						return True
			
			if pegSolitaireUtils.game.is_validMove(pegSolitaireObject, [i,j], "W") is not None:
				new=pegSolitaireUtils.game.getNextState(pegSolitaireObject, [i,j], "W"); 
				if new is not None:					
					if(IDS(new, h-1, trace_list)):
						trace_list.append([i,j-2])
						trace_list.append([i,j])					
						return True
				
	pegSolitaireObject.trace = ['GOAL NOT FOUND']


'''
isGameState function checks whether a received game state is a Goal State. If the solution is found, it returns true.
'''
def isGameState(pegSolitaireObject):
	goalState = [[-1, -1, 0, 0, 0, -1, -1], [-1, -1, 0, 0, 0, -1, -1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, -1, 0, 0, 0, -1, -1], [-1, -1, 0, 0, 0, -1, -1]]
	if(pegSolitaireObject.gameState==goalState):
		return True

'''
#Algorithm reference: https://www.youtube.com/watch?v=VIGqdGksDJ0
aStarOne function takes the game state and uses Manhattan distance heuristics to traverse. 
It stores fVal for every game state visited and makes a move which has a lower fVal.
G value of every game state is stored in dictionary using string equivalent of game state as key and g as value.
Finally it constructs the trace of the solution and sets it to path trace for printing. 
'''
def aStarOne(pegSolitaireObject):
	
	list_open=[]
	list_closed=[]
	
	list_open.append(pegSolitaireObject)
	fVal=dict()
	gVal=dict()
	parent_state=dict()
	gVal[getKey(pegSolitaireObject)]=0
	
	fVal[getKey(pegSolitaireObject)] = gVal[getKey(pegSolitaireObject)]+getManhattanValue(pegSolitaireObject)
	
	while list_open:			
		
		state = getOptimalNode(list_open,fVal)
		
		if isGameState(state):			 
			pegSolitaireObject.trace = define_path(parent_state,state)			
			return
		
		list_open.remove(state)
		list_closed.append(state)
		
		for successor in getSuccessors(state):
			if list_closed.count(successor[0]) != 0:
				continue
			
			newGVal = gVal[getKey(state)] + 1			
			if list_open.count(successor[0])==0 or newGVal<gVal[getKey(successor[0])]:
				gVal[getKey(successor[0])]=newGVal
				fVal[getKey(successor[0])] = gVal[getKey(successor[0])] + getManhattanValue(successor[0])
				parent_state[getKey(successor[0])] = ( getKey(state) , successor[1] , successor[2])				
				
				if list_open.count(successor[0]) == 0:
					list_open.append(successor[0])
				
	pegSolitaireObject.trace = ['GOAL NOT FOUND']

'''
define_path receives the dictionary of every node traversed in both the heuristics search and gets the path traversed for goal solution.
'''
def define_path(parent_state,state):

	trace = list()
	gameStateKey = getKey(state)
	
	while parent_state.has_key(gameStateKey):
		trace.append(parent_state[gameStateKey][1])
		trace.append(parent_state[gameStateKey][2])		
		gameStateKey=parent_state[gameStateKey][0]
		
	trace.reverse()
	
	return trace

'''
getOptimalNode finds the best move among the fringe list according to smallest f value.
'''
def getOptimalNode(list_open,fVal):
	minState=list_open[0]
	
	for state in list_open:
		if fVal[getKey(state)]< fVal[getKey(minState)]:
			minState=state
			
	return minState
			
'''
getKey takes any game state and returns the string equivalent of it.
'''
def getKey(inputState):
	
	gameString = ""
	
	for i in range(7):
		gameString = gameString + "".join(str(inputState.gameState[i]))
		
	return gameString
		
'''
getSuccessors finds all the possible moves from any game state.
'''
def getSuccessors(pegSolitaireObject):
	
	successors=[]
	for i in range(7):
		for j in range(7):
			if pegSolitaireUtils.game.is_validMove(pegSolitaireObject, [i,j], "N") is not None:
				new=pegSolitaireUtils.game.getNextState(pegSolitaireObject, [i,j], "N") 
				if new is not None:
					nextState=(new,[i-2,j],[i,j])
					successors.append(nextState)
					
			if pegSolitaireUtils.game.is_validMove(pegSolitaireObject, [i,j], "S") is not None:
				new=pegSolitaireUtils.game.getNextState(pegSolitaireObject, [i,j], "S")
				if new is not None:
					nextState=(new,[i+2,j],[i,j])
					successors.append(nextState)
			
			if pegSolitaireUtils.game.is_validMove(pegSolitaireObject, [i,j], "E") is not None:
				new=pegSolitaireUtils.game.getNextState(pegSolitaireObject, [i,j], "E")
				if new is not None: 
					nextState=(new,[i,j+2],[i,j])
					successors.append(nextState)
					
			if pegSolitaireUtils.game.is_validMove(pegSolitaireObject, [i,j], "W") is not None:
				new=pegSolitaireUtils.game.getNextState(pegSolitaireObject, [i,j], "W") 
				if new is not None:
					nextState=(new,[i,j-2],[i,j])
					successors.append(nextState)
	return successors
				
'''
getManhattanValue returns the manhattan distance of any peg from the goal location i.e. (3,3)
and thus it serves as a heuristic for aStarOne search.
'''
def getManhattanValue(pegSolitaireObject):
	
	cost=0;
	for i in range(7):
		for j in range(7):
			if pegSolitaireObject.gameState[i][j]==1:
				cost=cost+abs(i-3)+abs(j-3)
	return cost

'''
aStarTwo takes the initial game state and finds for goal state using Move State Cost Heuristics.
Move State Cost heuristic is calculated by finding the total number of valid moves on any given state
and thus giving us an indication as how far is it from goal state.
'''
def aStarTwo(pegSolitaireObject):
	'''	
		#################################################
        # Must use functions:
        # getNextState(self,oldPos, direction)
        # 
        # we are using this function to count,
        # number of nodes expanded, If you'll not
        # use this grading will automatically turned to 0
        #################################################
        #
        # using other utility functions from pegSolitaireUtility.py
        # is not necessary but they can reduce your work if you 
        # use them.
        # In this function you'll start from initial gameState
        # and will keep searching and expanding tree until you 
        # reach goal using A-Star searching with second Heuristic
        # you used.
        # you must save the trace of the execution in pegSolitaireObject.trace
        # SEE example in the PDF to see what to return
        #
   	    ####################################################
    '''
	list_open=[]
	list_closed=[]
	
	list_open.append(pegSolitaireObject)
	fVal=dict()
	gVal=dict()
	parent_state=dict()
	gVal[getKey(pegSolitaireObject)]=0
	
	fVal[getKey(pegSolitaireObject)] = gVal[getKey(pegSolitaireObject)]+getMoveStateCost(pegSolitaireObject)
	
	while list_open:			
		
		state = getOptimalNode(list_open,fVal)
		
		if isGameState(state):
			pegSolitaireObject.trace = define_path(parent_state,state)
			return
		
		list_open.remove(state)
		list_closed.append(state)
		
		for successor in getSuccessors(state):
			if list_closed.count(successor[0]) != 0:
				continue
			
			newGVal = gVal[getKey(state)] + 1			
			if list_open.count(successor[0])==0 or newGVal<gVal[getKey(successor[0])]:
				gVal[getKey(successor[0])]=newGVal
				fVal[getKey(successor[0])] = gVal[getKey(successor[0])] + getMoveStateCost(successor[0])
				parent_state[getKey(successor[0])] = ( getKey(state) , successor[1] , successor[2])
				
				if list_open.count(successor[0]) == 0:
					list_open.append(successor[0])
		
	pegSolitaireObject.trace = ['GOAL NOT FOUND']			       

'''
getMoveStateCost is a heuristic for aStarTwo and it calculates the total number of valid moves possible for any game state.
The idea is if less number of moves are left on the board, it is more probable that the game is nearer to the goal state.
'''
def getMoveStateCost(pegSolitaireObject):
	
	cost=0;
	for i in range(7):
		for j in range(7):
			if pegSolitaireObject.gameState[i][j]==1:
				if i-2>=0 and pegSolitaireObject.gameState[i-1][j]==1 and pegSolitaireObject.gameState[i-2][j]==0:
					cost=cost+1
				if i+2<=6 and pegSolitaireObject.gameState[i+1][j]==1 and pegSolitaireObject.gameState[i+2][j]==0:
					cost=cost+1
				if j-2>=0 and pegSolitaireObject.gameState[i][j-1]==1 and pegSolitaireObject.gameState[i][j-2]==0:
					cost=cost+1
				if j+2<=6 and pegSolitaireObject.gameState[i][j+1]==1 and pegSolitaireObject.gameState[i][j+2]==0:
					cost=cost+1

	return cost 

