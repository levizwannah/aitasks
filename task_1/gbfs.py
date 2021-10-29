from classes.Graphing import Graphing
from classes.Problem import Problem
from classes.ai import greedy_best_first_search, solution

problem = Problem("SportsComplex", "ParkingLot")
solution = greedy_best_first_search(problem)

# problem.graphing.color(solution)
problem.graphing.draw_graph(solution, "Greedy-BFS.png")
# graph = Graphing().get_graph()
# print(graph)

# prob = Problem("SportsComplex", "ParkingLot")

# for a in prob.get_actions("Siwaka"):
#     print(a.dest)
# print(a.dest for a in prob.get_actions("Siwaka"))


