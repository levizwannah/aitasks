from networkx.classes import graph
from classes.Graphing import Graphing
from classes.Action import Action
class Problem:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.graph = Graphing().get_graph()
        self.final_state = final_state

    def goal_test(self, state):
        return state == self.final_state

    def get_actions(self, state):
        actions = []
        for node in self.graph.adj[state]:
            actions.append(Action(node))
        return actions
