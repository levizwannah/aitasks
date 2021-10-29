from classes.Node import Node
from classes.Problem import Problem

solution_path = []

heuristics = {
    "SportsComplex": 730,
    "Siwaka": 405,
    "Ph.1A": 380,
    "Ph.1B": 280,
    "Phase2": 210,
    "J1": 500,
    "Mada": 630,
    "STC": 213,
    "Phase3": 160,
    "ParkingLot": 0,
}

def greedy_best_first_search(problem: Problem):
    node = Node(problem, None, None)

    if(problem.goal_test(node.state)):
        return solution(node)

    frontier = []
    frontier_states = []
    frontier.append(node)
    frontier_states.append(node.state)

    explored = []

    while True:
        if(len(frontier) == 0):
            return []
        
        node = frontier.pop(0)
        frontier_states.pop(0)

        explored.append(node.state)

        actions = problem.get_actions(node.state)
        best_action = actions[0]
        for action in problem.get_actions(node.state):
            if(heuristics[action.dest] < heuristics[best_action.dest]):
                best_action = action

        child = Node(problem, node, best_action)
            
        if(child.state not in explored and child.state not in frontier_states):
            if(problem.goal_test(child.state)):
                return solution(child)
            frontier.append(child)
            frontier_states.append(child.state)
        
            


def solution(node: Node):
    solution_path.append(node.state)
    if(node.parent == None):
        return solution_path
    else:
        return solution(node.parent)

