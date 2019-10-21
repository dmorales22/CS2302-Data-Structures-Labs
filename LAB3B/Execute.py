#Author: David Morales 
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre 
#T.A: Gerardo Barraza
#Assignment: Lab 3 - Option B 
#Last Modification: 10/21/2019  
#Purpose: Find anagrams in a text file using trees.   

import AVLTrees, RBTrees

def bst_search(tree, key): #Basic binary search algorithm adapted from zybooks.
	cur = tree.root   
	while (cur != None):
		if (key == cur.key):
			return cur 
		
		elif (key < cur.key):
			cur = cur.left
			
		else:
			cur = cur.right
		
	return None
	
def key_generator(word): #This method generates keys for each word by stringing together character numbers of each letter of a word. 
	key = "" 
	res = list(word) #Creates a list of characters from a word . 
	
	if (len(res[0]) > 1):  #If a non-string character gets inputted, it makes it into a string and runs the method again. 
		str_word = str(res[0]) 
		return key_generator(str_word)
		
	for i in range(len(res)): 
		char = caps_detector(res[i]) #Checks if a character is capitalize. 
		char_num = ord(char) #Gets the character number of a letter. 
		char_str = str(char_num) #Makes the character number a string. 
		key += char_str #Strings together the character numbers. 
		
	key_int = int(key) 
	
	return key_int   #Returns an integer of the character numbers. 
	
def caps_detector(char): #Checks if a letter is capitalized, then returns the lower case equalivent if the letter is capitalized.  
	cap_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
	
	lower_char = '' 
	for i in range(len(cap_list)): 
		if (char == cap_list[i]): 
			lower_char = lower_list[i] 
			return lower_char
			
	return char 
 
def find_anagrams(tree, word, prefix=""): #This method is very similar to the print_anagrams method provided to use.  Except it use binary search and counts the anagrams. 
	if len(word) <= 1: 
		str = prefix + word
		key = key_generator(str) 
		
		found_word = bst_search(tree, key)
		if (found_word != None): 
			return 1 
			
		return 0 
			
	else:
		count_anagrams = 0 
		for i in range(len(word)):
			cur = word[i: i + 1]
			before = word[0: i] # letters before cur
			after = word[i + 1:] # letters after cur
			
			if cur not in before: # Check if permutations of cur have not been generated.
				count_anagrams += find_anagrams(tree, before + after, prefix + cur)
				
	return count_anagrams
	
def avl_tree(filename): #This method reads a text file, parses through it line by line, and inserts words into a AVL Tree. 
	avl_tree = AVLTrees.AVLTree()
	key_num = 0
	print("Making an AVL tree then. \n")
	
	with open(filename, encoding='windows-1252') as textFile: 
		for line in textFile:
			string = line.split()
			word = str(string) 
			word_str = word[2:len(word) - 2] 
			
			key_num = key_generator(word_str) 
			avl_tree.avl_insertion(word_str, key_num)

	return avl_tree
	
def rb_tree(filename): #This method reads a text file, parses through it line by line, and inserts words into a RBTree. 
	rb_tree = RBTrees.RedBlack()
	key_num = 0 
	print("Making a Red-Black tree then.  \n") 
	
	with open(filename, encoding='windows-1252') as textFile: 
		for line in textFile:
			string = line.split()
			word = str(string) 
			word_str = word[2:len(word) - 2]
			
			key_num = key_generator(word_str)   
			rb_tree.rb_insert(word_str, key_num)
				
	return rb_tree 

def num_anagrams(tree): #This method executes after a tree is created. You input a word and runs find_anagrams. Prints out the total number of anagrams. 
	print("") 
	print("Input a word: ") 
	new_word = input() 
	count = find_anagrams(tree, new_word) 
	print("") 
	print("Total number of anagrams found for this word:", count, "\n")  

def max_anagrams(): #This method reads a text file in by user input, creates a RBtree, and finds the word with the most anagrams within the textfile.  
	print("Want to load another file to find the word that has the most anagrams? Y/N") 
	user_input = input() 
	
	if (user_input == "Y" or user_input == "y"):
		print("")
		print("Input filename of the textfile:")
		filename = input() 
		tree = rb_tree(filename) #Creates RBTree of words from textfile. 
	
		most_anagrams = "" 
		most_anagrams_num = 0 
	
		with open(filename, encoding='windows-1252') as textFile:  
			for line in textFile:
				string = line.split()
				word = str(string)
				word_str = word[2:len(word) - 2]
				count = find_anagrams(tree, word_str)   
				
				if (most_anagrams_num < count): #Sets variable with the word with the most anagrams using this if statement. 
					most_anagrams = word_str 
					most_anagrams_num = count
					
		print("The word with the most anagrams is '", most_anagrams, "' with the total of", most_anagrams_num, "anagrams.")
		
	elif (user_input == "N" or user_input == "n"): #Exits program.
		print("Goodbye. \n")
		exit() 
		
	else: 
		print("Invalid input. Try again. \n") 
		max_anagrams() 
		
def main(): #Main method asks for user input. User can choose to create an avl or rb tree. 
	print("Input textfile name: ") 
	filename = input() 
	
	print("") 
	print("Do you want to use an AVL tree or a Black-Red tree? Type 'A' for AVL or type 'B' for Red-Black.") 
	user_input = input()
	
	if (user_input == 'A' or user_input == 'a'):  
		tree = avl_tree(filename) 
		num_anagrams(tree) 
		
	elif (user_input == 'B' or user_input == 'b'): 
		tree = rb_tree(filename)
		num_anagrams(tree) 
		
	else: 
		print("Invalid input, try again. \n") 
		main() 
		
main() 
max_anagrams() #Executes after main() 