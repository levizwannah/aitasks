from classes.Problem import Problem
class Node:

    def __init__(self, problem: Problem, parent, action):
        self.parent = parent
        self.problem = problem
        self.action = action
        if(not parent):
            self.state = problem.initial_state
    