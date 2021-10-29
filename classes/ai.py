from classes.Node import Node
from classes.Problem import Problem

def greedy_best_first_search(problem: Problem):
    node = Node(problem, None, None)

    if(problem.goal_test()):
        return solution(node)

    fonti

def solution(node: Node):
    pass