#Author: David Morales 
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre 
#T.A: Gerardo
#Assignment: Lab 1 - Option B (Password Cracking) 
#Date: 09/06/2019 
#Purpose: Password Cracker for Hashes

import hashlib

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def max_num(char_num): #This method gets the max number of a certain amount of digits using recursion. Ex: 999, 9999, 99999...
	if (char_num == 0): 
		return ''
	return '9' + max_num(char_num - 1) 
	
def password_gen(salt_name, char_num, hash_pass):
	max_digit = int(max_num(char_num)) #Converts the string into a integer from the max_num method.
	
	if (char_num >= 8):
		print("Password not found. Not in the range of 3 to 7. This program only does digits within that range. Anything else is too much for me.")
		return "Error. Password not found."
		
	for x in range (0, max_digit): #This for loop generates the numbers, adds them to the salt string, and uses the hashing method. Then compares string to the hashed password.
		pass_iter = str(x) 
		hex_dig = hash_with_sha256(pass_iter.zfill(char_num) + salt_name) #zfill is used to pad left side with zeros. Ex: 001, 00243, 02
		if (hex_dig == hash_pass): 
			return pass_iter.zfill(char_num)
			
	return password_gen(salt_name, char_num + 1, hash_pass) #This is the recursive part. Just adds one to char_num to signify to add another character to the brute forcing.
	
def main():
	print("Input textfile name: ") 
	filename = input() 
	
	with open(filename) as textFile: 
		textFile_lines = [line.split(',') for line in textFile]
	
	print("Brute force in progress! \n") 
	
	char_num = 3 
	
	for x in range (len(textFile_lines)):  #This for loop feeds the password_gen method with relevant information like the salt and hash from the textfile. Prints out password (if found).
		hash_pass = textFile_lines[x][2]
		hex_dig = password_gen(textFile_lines[x][1], char_num, hash_pass.rstrip('\n'))
		print(textFile_lines[x][0] + ' password is: ' + hex_dig) 
	
main()