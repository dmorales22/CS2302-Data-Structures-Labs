#Using the implementation of topological sort provided to us.
from queue import Queue
from graph_am import GraphAM
from graph_al import GraphAL

def compute_indegree_every_vertex_am(graph):  #This method computes the indegree of every vertice in the graph (AM). 
    if graph is None: 
        return []

    in_degree = [0] * graph.vertices

    for i in range(len(graph.am)): #Goes through the graph (2D array) and counts indegrees.
        for j in range(len(graph.am[i])): 
            if graph.am[i][j] != 0:
                in_degree[j] += 1

    return in_degree

def compute_indegree_every_vertex_al(graph): #This method computes the indegree of every vertice in the graph (AL).
    if graph is None: 
        return []

    in_degree = [0] * graph.vertices

    for i in range(len(graph.al)): #Goes through the graph (adjacency list) and counts indegrees. 
        for j in range(len(graph.al[i])): 
                in_degree[j] += 1

    return in_degree

def topological_sort_am(graph): #Topological sort for a adjacency matrix graph.
    all_in_degrees = compute_indegree_every_vertex_am(graph) #Getting the all_in_degrees.
    sort_result = []
    q = Queue() 

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.put(i)

    while not q.empty():
        u = q.get()
        sort_result.append(u)

        for adj_vertex in graph.vertices_reachable_from(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)

    if len(sort_result) != graph.vertices:
        return None 

    return sort_result

def topological_sort_al(graph): #Topological sort for a adjacency lists graph.
    all_in_degrees = compute_indegree_every_vertex_al(graph) #Getting the all_in_degrees.
    sort_result = []
    q = Queue() 

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.put(i)

    while not q.empty():
        u = q.get()
        sort_result.append(u)

        for adj_vertex in graph.vertices_reachable_from(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)

    if len(sort_result) != graph.vertices:
        return None 

    return sort_result