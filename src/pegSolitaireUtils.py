import readGame
import new
import copy
#######################################################
# These are some Helper functions which you have to use 
# and edit.
# Must try to find out usage of them, they can reduce
# your work by great deal.
#
# Functions to change:
# 1. is_wall(self, pos):
# 2. is_validMove(self, oldPos, direction):
# 3. getNextPosition(self, oldPos, direction):
# 4. getNextState(self, oldPos, direction):
#######################################################
class game:
	def __init__(self, filePath):
		self.gameState = readGame.readGameState(filePath)
		self.nodesExpanded = 0
		self.trace = []	
	
	'''	
		Check if there is a corner state
	'''
	def is_corner(self, pos):
		'''
		########################################
		# You have to make changes from here
		# check for if the new positon is a corner or not
		# return true if the position is a corner
		'''
		if self.gameState[pos[0]][pos[1]] == -1:
			return True
		
		return False	
	
	'''	
		Returns the valid next game state
	'''
	
	def getNextPosition(self, oldPos, direction):
		'''
		#########################################
		# YOU HAVE TO MAKE CHANGES HERE
		# See DIRECTION dictionary in config.py and add
		# this to oldPos to get new position of the peg if moved
		# in given direction , you can remove next line
		'''
		
		if self.gameState[oldPos[0]][oldPos[1]] != 1:
			return None
		
		if(direction == 'N'):
			if(oldPos[0]-2 >= 0):						
				if self.gameState[oldPos[0] -1][oldPos[1]] == 1:
					if self.gameState[oldPos[0] -2][oldPos[1]] == 0:
						new = copy.deepcopy(self)
						new.gameState[oldPos[0]][oldPos[1]] = 0
						new.gameState[oldPos[0] -1][oldPos[1]] = 0
						new.gameState[oldPos[0] -2][oldPos[1]] = 1
						return new
			else:
				return None
			
		if(direction == 'S'):
			if(oldPos[0]+2<=6):					
				if self.gameState[oldPos[0] +1][oldPos[1]] == 1:
					if self.gameState[oldPos[0] +2][oldPos[1]] == 0:
						new = copy.deepcopy(self)
						new.gameState[oldPos[0]][oldPos[1]] = 0
						new.gameState[oldPos[0] +1][oldPos[1]] = 0
						new.gameState[oldPos[0] +2][oldPos[1]] = 1
						return new
			else:
				return None
			
		if(direction == 'E'):
			if(oldPos[1]+2<=6):						
				if self.gameState[oldPos[0]][oldPos[1]+1] == 1:
					if self.gameState[oldPos[0]][oldPos[1]+2] == 0:
						new = copy.deepcopy(self)
						new.gameState[oldPos[0]][oldPos[1]] = 0
						new.gameState[oldPos[0]][oldPos[1]+1] = 0
						new.gameState[oldPos[0]][oldPos[1]+2] = 1
						return new
			else:
				return None
			
		if(direction == 'W'):
			if(oldPos[1]-2>=0):						
				if self.gameState[oldPos[0]][oldPos[1]-1] == 1:
					if self.gameState[oldPos[0]][oldPos[1]-2] == 0:
						new = copy.deepcopy(self)
						if(oldPos[1]-2>=0):
							new.gameState[oldPos[0]][oldPos[1]] = 0
							new.gameState[oldPos[0]][oldPos[1]-1] = 0
							new.gameState[oldPos[0]][oldPos[1]-2] = 1
							return new
			else:
				return None
		
	
	'''	
		check if there is any valid moves
	'''	
		
	def is_validMove(self, oldPos, direction):
		#########################################
		# DONT change Things in here
		# In this we have got the next peg position and
		# below lines check for if the new move is a corner
		#print("is_validMove")
		new = self.getNextPosition(oldPos, direction)
		#if self.is_corner(new):
			#return None	
		if new is None:
			return None
		
		return new
		#########################################
		
		########################################
		# YOU HAVE TO MAKE CHANGES BELOW THIS
		# check for cases like:
		# if new move is already occupied
		# or new move is outside peg Board
		# Remove next line according to your convenience
		#return True
	
	'''	
		returns the next state of the game, if possible
	'''
	def getNextState(self, oldPos, direction):
		###############################################
		# DONT Change Things in here
		self.nodesExpanded += 1
		new=self.is_validMove(oldPos, direction)			
		if new is None:
				print ("Error, You are not checking for valid move")
				exit(0)
		###############################################
		
		###############################################
		# YOU HAVE TO MAKE CHANGES BELOW THIS
		# Update the gameState after moving peg
		# eg: remove crossed over pegs by replacing it's
		# position in gameState by 0
		# and updating new peg position as 1
		
		return new
