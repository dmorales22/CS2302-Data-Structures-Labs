#Author: David Morales 
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre 
#T.A: Gerardo Barraza
#Assignment: Lab 2 - Option B 
#Last Modification: 09/23/2019
#Purpose: Finds most common passwords from list. 


class Node(object): #Basic constructor of the Node class provided to us. 
	password = ""
	count = -1
	next = None
	
	def __init__(self, password, count, next):
		self.password = password
		self.count = count
		self.next = next
		
#This is part 1. It uses solution A. 
class LList(object): #The linked list node constructor that comes with Node Head and Int size variables. 
	head = Node("", -1, None) 
	size = 0 
	
	def __init__(self): 
		self.head = Node("", -1, None) 
		self.size = 0 
	
	def append_passLList(self, str): #Adds nodes to link list (at the end), but also checks if the password(s) appears more than one.
		if (self.head.count == -1): #Assigns first node to head. 
			node = Node(str, 1, None) 
			self.head = node 
			self.size += 1 
			
		else: 
			node = Node(str, 1, None)
			iter = self.head  
			
			while (iter.next != None):
				if (iter.password == str): #This checks if the password from the node is the same with the string. Adds to count. 
					iter.count += 1 
					break
				iter = iter.next
				if (iter.password == str): #Another if statement to check the next node. 
					iter.count += 1 
					break
					
			if (iter.count < 2): #Only adds nodes to link list if the count is less than two to avoid duplicates. Updates size. 
				iter.next = node  
				self.size += 1
			