from ..utils import graph, printing
from math import isinf
from heapq import *

# Only calculate cost table for now
def bellman_ford(graph_path):
    g = graph.read_graph_adj_table(graph_path)
    
    cost = [ [float("inf")] * g.N for _ in range(g.N) ]

    for u in range(g.N):
        for v in range(g.N):
            cost[u][v] = g.get_cost(u, v)

    printing.print_table(cost, showindex=g.get_symbol(), headers=g.get_symbol())
    print()
    
    for i in range(g.N):
        for _ in range(g.M):
            for j in range(g.N):
                for n in range(g.N):
                    c = g.get_cost(j, n)
                    if cost[i][n] + c < cost[i][j]:
                        cost[i][j] = cost[i][n] + c

    printing.print_table(cost, showindex=g.get_symbol(), headers=g.get_symbol())

def dijkstra(graph_path, start):
    g = graph.read_graph_adj_table(graph_path)

    spt = set()
    spt_order = ''
    D = [float("inf")] * g.N
    p = [-1] * g.N
    q = [(0, -1, start)] # (D, p, node#)

    # Print header
    print(f'| step | N\' | ', end='')
    for i in range(0, g.N - 1):
        sym = g.get_symbol(i)
        print(f'D({sym}), p({sym})', end=' | ')
    print(f'D({g.get_symbol(g.N - 1)}), p({g.get_symbol(g.N - 1)})', end=' |\n')

    print('|' + '---|' * (g.N + 2))

    step = 0
    while q:
        D_n, p_n, n = heappop(q)

        if n not in spt:
            spt.add(n)
            spt_order += g.get_symbol(n)
            for i in range(g.N):
                c = g.get_cost(n, i)
                if i not in spt and not isinf(c):
                    if D[i] > D_n + c:
                        D[i] = D_n + c
                        p[i] = n
                    heappush(q, (D_n + c, n, i))

            print(f'| {step} | {spt_order} | ', end='')
            for i in range(0, g.N - 1):
                print(f'{D[i]}, {g.get_symbol(p[i])}', end=' | ')
            print(f'{D[g.N - 1]}, {g.get_symbol(p[g.N - 1])}', end=' |\n')

            step += 1
    