# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import pdb


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # Return type is a list of actions to be performed to reach the goal

    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    visited = set()
    stack = util.Stack()
    stack.push((problem.getStartState(), ""))
    parentNode = {}
    goalNode = None

    while not stack.isEmpty():
        top = stack.pop()
        # print "Here:", top

        if problem.isGoalState(top[0]):
            # print(top[0],problem.isGoalState(top[0]))
            goalNode = top
            break
        
        visited.add(top[0])
        for neighbor in problem.getSuccessors(top[0]):
            if neighbor[0] not in visited:
                stack.push((neighbor[0], neighbor[1]))
                parentNode[neighbor[0]] = top

    actions = []

    # for x in parentNode:
    #     print(x, parentNode[x])
    while goalNode[0] is not problem.getStartState():
        # print(goalNode,  problem.getStartState())
        actions.append(goalNode[1])
        goalNode = parentNode[goalNode[0]]

    # print(actions)
    return actions[::-1]

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    next = util.Queue()
    visited = []

    start = problem.getStartState()
    actions = []

    next.push((start, actions))

    while not next.isEmpty():
        curr, actions = next.pop()

        if problem.isGoalState(curr):
            # print(actions)
            return actions
        
        if curr not in visited:
            visited.append(curr)
            
            # pdb.set_trace()
            succs = problem.getSuccessors(curr)

            for state_, action_, cost_ in succs:
                actions_ = actions + [action_]
                next.push((state_, actions_))

    return actions_

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #A variant of Dijkstra's
    next = util.PriorityQueue()

    visited = []
    actions = []

    start = problem.getStartState()
    startState = (start, actions, 0) #Cost = 0 for start

    next.push((startState), 0) #PQ item = (node, cost)

    while not next.isEmpty():
        curr, actions, cost = next.pop()

        if problem.isGoalState(curr):
            return actions
        
        if curr not in visited:
            visited.append(curr)

            succx = problem.getSuccessors(curr)

            for state_, action, cost_ in succx:

                actions_ = actions + [action]
                updatedCost = cost + cost_

                #Priority Queue will only update the cost of an already existing state IF the new cost is lesser
                
                next.update((state_, actions_, updatedCost), updatedCost)

    return actions

    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    next = util.PriorityQueue()

    visited = []
    actions = []

    start = problem.getStartState()
    startState = (start, actions, 0)

    next.push((startState), startState[-1]) #PQ item = (node, cost)

    while not next.isEmpty():
        curr, actions, cost = next.pop()

        if problem.isGoalState(curr):
            return actions
        
        if curr not in visited:
            visited.append(curr)

            succx = problem.getSuccessors(curr)

            for state_, action, cost_ in succx:

                actions_ = actions + [action]
                updatedCost = cost + cost_ 

                #Priority Queue will only update the cost of an already existing state IF the new cost is lesser
                
                next.update((state_, actions_, updatedCost), updatedCost + heuristic(state_, problem))

    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
