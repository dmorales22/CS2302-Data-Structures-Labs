#Author: David Morales 
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre 
#T.A: Gerardo Barraza
#Assignment: Lab 2 - Option B 
#Last Modification: 09/19/2019 (Part 1 only finished) 
#Purpose: Finds most common passwords from list. 

import Node
def common_pass(passLList): 
	#TODO 1: add sorting method 
	sorted_list = Node.LList() 
	iter = passLList.head 
	
	#while (iter.next != None): 

def parse_list(): 
	print("Input textfile name: ") 
	filename = input() 
	passLList = Node.LList() 
	
	with open(filename, encoding='windows-1252') as textFile: 
		for line in textFile:
			str = line.split() #Reads the textfile line by line so it won't kill the computer's memory. 
			if (len(str) != 1): #If statement used if password is blank to prevent out of bound errors. 
				passLList.append_passLList(str[1])  #Uses Append method from Node.py to add the strings to a link list. 
				print(str[1])
	
	return passLList
	
def main(): 
	passLList = parse_list() 
	common_pass (passLList) 
	
main()