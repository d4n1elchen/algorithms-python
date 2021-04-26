def parse_line_str(line):
    return map(str, line.split())

def parse_line_int(line):
    return map(int, line.split())

class Graph:

    def __init__(self, N, M, directed = False):
        self.adj = [ [float("inf")] * N for _ in range(N) ]
        self.E = []
        self.N = N
        self.M = M
        self.directed = directed

        for i in range(N):
            self.adj[i][i] = 0

    def __repr__(self):
        from tabulate import tabulate
        return tabulate(self.adj, showindex="always", headers=list(range(0, self.N)), tablefmt="pipe")
    
    def add_edge(self, u, v, cost):
        self.E.append((u, v, cost))
        self.set_cost(u, v, cost)
    
    def get_cost(self, u, v):
        return self.adj[u][v]
    
    def set_cost(self, u, v, cost):
        if not self.directed:
            self.adj[u][v] = self.adj[v][u] = cost
        else:
            self.adj[u][v]


"""
Input format:
<N_nodes> <M_edges> <directed?>
<from> <to> <cost>
... M lines
"""
def read_graph_adj_table(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        N, M, directed = parse_line_int(lines.pop(0))

        g = Graph(N, M, directed)

        for line in lines:
            u, v, cost = parse_line_int(line)
            g.add_edge(u, v, cost)

        return g
