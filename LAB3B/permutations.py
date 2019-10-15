import BTrees 

def b_tree_rb(words): 
	print(words) 
	
def count_anagrams(words): 
	print("lol") 

def main():
	print("Input textfile name: ") 
	filename = input() 
	
	print("Do you want to use an AVL tree or Black-Red trees? Type A for AVL or type B for Red-Black.") 
	user_input = input()
	
	if (user_input == 'A'): 
		counter = 1 
		with open(filename, encoding='windows-1252') as textFile: 
			print("Making an AVL tree then.  \n") 
			for line in textFile:
				str = line.split() 
				key_num = counter 
				avl_tree = BTrees.AVLTree.avl_insertion(str, key_num) 
				counter += 1 
				
	elif (user_input == 'B'): 
		with open(filename, encoding='windows-1252') as textFile: 
			print("Making a Red-Black tree then.  \n") 
			for line in textFile:
				str = line.split() 
				b_tree_rb(str) 				
	else: 
		print("Invalid input, try again.") 		
main() 