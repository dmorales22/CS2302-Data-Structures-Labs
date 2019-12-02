#Modified DSF implementation and Kruskal pseudo code provided to us. 
from queue import Queue
from graph_am import GraphAM
from graph_al import GraphAL

class DisjointSetForest:
    def __init__(self, vertices):
        self.forest = [i for i in range(vertices)]

    def find_loop(self, p, q):
        return self._find(p) == self._find(q)

    def union(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)

        if p_root == q_root:
            return
        self.forest[p_root] = q_root

    def _find(self, p):
        while p != self.forest[p]:
            p = self.forest[p]
        return p

    def __str__(self):
        return str(self.forest)

def kruskal_am(graph): #This is kruskal's algorithm. It was works for adjaceny matrix graphs.
    edges = set()
    T = set()

    for i in range(len(graph.am)): #Adds all edges to a set. 
        for j in range(len(graph.am[i])):
            if graph.am[i][j] != 0 and (j, i) not in edges:
                edges.add((i, j))

    sorted_edges = sorted(edges, key = lambda edge:graph.am[edge[0]][edge[1]]) #Sorts edges.
    dsf = DisjointSetForest(graph.vertices)
    
    for i in sorted_edges: #uses a DSF to find the minimum spanning tree.
        u, v = i
        if dsf.find_loop(u, v):
            continue
        dsf.union(u, v)
        T.add(i)

    return T 
