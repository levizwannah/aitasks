from classes.Graphing import Graphing
from classes.Problem import Problem
from classes.ai import greedy_best_first_search, solution

problem = Problem("SportsComplex", "ParkingLot")
solution = greedy_best_first_search(problem)
problem.graphing.draw_graph(solution, "Greedy-BFS.png")