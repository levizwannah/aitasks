from classes.Graphing import Graphing
from classes.Problem import Problem
from classes.ai import greedy_best_first_search

print( greedy_best_first_search(Problem("SportsComplex", "ParkingLot")))

# graph = Graphing().get_graph()
# print(graph)

# prob = Problem("SportsComplex", "ParkingLot")

# for a in prob.get_actions("Siwaka"):
#     print(a.dest)
# print(a.dest for a in prob.get_actions("Siwaka"))


