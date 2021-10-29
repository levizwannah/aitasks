from classes.Graphing import Graphing
class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.graph = Graphing().get_graph()
