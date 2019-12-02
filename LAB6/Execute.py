#Author: David Morales
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre
#T.A: Gerardo Barraza
#Assignment: Lab 6
#Last Modification: 12/02/2019
#Purpose: Implementation of Kruskal algorithm and topological sort.

import graph_al
import graph_am
import topological_sort as topsort
import kruskal

def main():
	g = graph_am.GraphAM(6, weighted=True)
	g.insert_edge(0, 1, 4)
	g.insert_edge(0, 2, 3)
	g.insert_edge(1, 2, 2)
	g.insert_edge(2, 3, 1)
	g.insert_edge(3, 4, 5)
	g.insert_edge(4, 1, 4)

	print("Printing graph1 before Kruskal.")
	g.display()
	g.draw()

	print("\n")

	print("Printing graph1 minimun spanning trees.")
	T = kruskal.kruskal_am(g)
	print(T)

	print("\n")

	g2 = graph_am.GraphAM(6, weighted=True)
	g2.insert_edge(0, 1, 2)
	g2.insert_edge(0, 2, 3)
	g2.insert_edge(1, 2, 0)
	g2.insert_edge(2, 3, 1)
	g2.insert_edge(3, 4, 2)
	g2.insert_edge(4, 1, 3)

	print("Printing graph2 before Kruskal.")
	g2.display()
	g2.draw()

	print("\n")

	print("Printing graph2 minimun spanning trees.")
	T = kruskal.kruskal_am(g2)
	print(T)
	
	print("-----------------------------------------------------------------------------------------------------------------\n")

	print("Printing graph1 before topological sort.")
	g = graph_am.GraphAM(9, directed=True)
	g.insert_edge(0, 1)
	g.insert_edge(4, 0)
	g.insert_edge(4, 1)
	g.insert_edge(5, 1)
	g.insert_edge(5, 2)
	g.insert_edge(5, 4)
	g.insert_edge(5, 7)
	g.insert_edge(7, 4)
	g.insert_edge(8, 5)
	g.insert_edge(8, 7)
	g.insert_edge(2, 1)
	g.insert_edge(2, 3)
	g.insert_edge(6, 2)
	g.insert_edge(6, 3)
	g.insert_edge(6, 5)
	g.insert_edge(6, 8)
	g.display()
	g.draw()


	print("\n")

	print("Printing sorted graph1 path after topological sort.")
	g_sorted = topsort.topological_sort_am(g)
	print(g_sorted)

	print("\n")
	

	print("Printing graph2 before topological sort.")
	g2 = graph_am.GraphAM(4, directed=True)
	g2.insert_edge(0, 1)
	g2.insert_edge(0, 2)
	g2.insert_edge(0, 3)
	g2.insert_edge(1, 3)
	g2.insert_edge(1, 4)
	g2.insert_edge(2, 3)
	g2.display()
	g2.draw()


	print("\n")

	print("Printing sorted graph1 path after topological sort.")
	g_sorted = topsort.topological_sort_am(g2)
	print(g_sorted)
main()