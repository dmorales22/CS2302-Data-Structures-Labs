#Author: David Morales 
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre 
#T.A: Gerardo Barraza
#Assignment: Lab 2 - Option B 
#Last Modification: 09/19/2019 (Part 1 only finished) 
#Purpose: Finds most common passwords from list. 


class Node(object): #Basic constructor of the Node class provided to us. 
	password = ""
	count = -1
	next = None
	
	def __init__(self, password, count, next):
		self.password = password
		self.count = count
		self.next = next
		
#This is part 1 solution (A). It is implemented and done. 
class LList(object): #The linked list node constructor that comes with Node Head and Int size variables. 
	head = Node("", -1, None) 
	size = 0 
	
	def __init__(self): 
		self.head = Node("", -1, None) 
		self.size = 0 
		
	def append_passLList(self, str): #Adds nodes to link list, but also checks if the password(s) appears more than one. 
		node = Node(str, 1, None)
		iter = self.head  
		
		while iter.next != None:
			iter = iter.next 
			if (iter.password == str): #This checks if the password from the node is the same with the string. Adds to count. 
				iter.count += 1 
		if (iter.count < 2): #Only adds node to link list if the count is less than two. Updates size. 
			iter.next = node 
			self.size += 1
			