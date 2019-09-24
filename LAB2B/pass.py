#Author: David Morales 
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre 
#T.A: Gerardo Barraza
#Assignment: Lab 2 - Option B 
#Last Modification: 09/23/2019  
#Purpose: Finds most common passwords from list. 

import Node
def common_pass(passLList): #This is part 2 solution A. It is uses bubble sort, and uses a loop to print the top 20 nodes.  
	temp = Node.Node("", -1, None) 
	iter = passLList.head 
	
	for i in range(passLList.size): #Bubble sort algorithm. 
		iter = passLList.head
		while (iter.next != None): 
			nextNode = iter.next 
			if (iter.count < nextNode.count):
				temp.password = iter.password #Switches password and count values. 
				temp.count = iter.count 
				
				iter.password = nextNode.password 
				iter.count = nextNode.count 
				
				nextNode.password = temp.password
				nextNode.count = temp.count 
			iter = iter.next 
		
	iter = passLList.head 
	counter = 1
	counter_str = ""
	
	print("1. ", iter.password, "Count:", iter.count) #Prints head. 
	while (iter.next != None): #Prints elements of the nodes in a nice format until counter goes above 19. 
		if (counter > 19): 
			break 
		iter = iter.next
		counter += 1
		counter_str = str(counter) + ". " 
		print(counter_str, iter.password, "Count:", iter.count)  

def parse_list(): #This is part 1 solution (A). It is implemented and done. Parsing textfile and uses append method from Node.py. 
	print("Input textfile name: ") 
	filename = input() 
	passLList = Node.LList() 
	
	with open(filename, encoding='windows-1252') as textFile: 
		print("Printing the top 20. This may take a while... \n") 
		for line in textFile:
			str = line.split() #Reads the textfile line by line so it won't kill the computer's memory.
			if (len(str) == 1): #For single column password lists. 
				passLList.append_passLList(str[0])
			if (len(str) != 1): #If statement used if password is blank to prevent out of bound errors.
				passLList.append_passLList(str[1])  #Uses append_passLList method from Node.py to add the strings to a link list. 
	
	return passLList
	
def main():
	passLList = parse_list() 
	common_pass (passLList) 
	
main()