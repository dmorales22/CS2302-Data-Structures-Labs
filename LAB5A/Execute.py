#Author: David Morales
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre
#T.A: Gerardo Barraza
#Assignment: Lab 5
#Last Modification: 11/19/2019
#Purpose: Implement a LRU cache and find the most seen word in a list using heaps.

import LRU as lru
import Heap as heap

def lru_testing():
	new_lru = lru.LRU(10)
	new_lru.put(1, "Test")
	new_lru.put(2, "Opp")
	new_lru.put(3, "Test")
	new_lru.put(4, "opp")
	new_lru.put(5, "testtt") 
	new_lru.put(6, "asdsad")
	new_lru.put(8, "ddd") 
	new_lru.put(9, "3323")
	new_lru.put(10, "Last")
	new_lru.put(11, "sdds") 
	new_lru.put(11, "sddsss") 
	new_lru.put(8, "wiped")
	new_lru.put(9, "wiped")
	new_lru.put(6, "wiped")
	new_lru.put(11, "wiped")
	new_lru.put(6, "testssss")
	new_lru.put(12, "1222")
	empty = new_lru.get(12)
	new_lru.print_inorder()
	

def main(): 
	print("Do you want to use a LRU (press A), or find the most found word in a list using heaps (press B):")
	choice = input()
	
	if (choice == "A" or choice == "a"):
		lru_testing() 
		
	elif (choice == "B" or choice == "b"): 
		print("\n")
		print("Input filename:")
		filename = input()
		word_heap, dict = heap.MaxHeap.file_parser(filename)
		size_of_heap = word_heap.size()
		
		print("How many words do you want to see printed? There are", size_of_heap, "words in the heap.")
		k = int(input())
		
		word_heap.print_decending(k)

	else: 
		print("Invalid input try again.") 
		
main()