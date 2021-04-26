from ..utils import graph, printing
from math import isinf

# Only calculate cost table for now
def bellman_ford(graph_path):
    g = graph.read_graph_adj_table(graph_path)
    
    cost = [ [float("inf")] * g.N for _ in range(g.N) ]

    for u in range(g.N):
        for v in range(g.N):
            cost[u][v] = g.get_cost(u, v)

    printing.print_table(cost)
    print()
    
    for i in range(g.N):
        for _ in range(g.M):
            for j in range(g.N):
                for n in range(g.N):
                    c = g.get_cost(j, n)
                    if cost[i][n] + c < cost[i][j]:
                        cost[i][j] = cost[i][n] + c

    printing.print_table(cost)
