#Author: David Morales
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre
#T.A: Gerardo Barraza
#Assignment: Lab 7
#Last Modification: 12/02/2019
#Purpose: Implementation of the edit distance algorithm.

def edit_distance(string1, string2, len_string1 , len_string2): #The recursive verison of the edit distance algorithm. (Recursive stacks)
    if len_string1 == 0:  #Returns when it goes through the all string. 
        return len_string1

    if len_string2 == 0: 
        return len_string2 

    if string1[len_string1 - 1] == string2[len_string2 - 1]:  #If characters are equal, it just the returns the substring (minus one of of both string counts). 
        return edit_distance(string1, string2 , len_string1 - 1, len_string2 - 1) 
        
     #Runs through insertion, replacment, and deletion. Gets the minimum of all the added operations.
    return 1 + min(edit_distance(string1, string2, len_string1, len_string2 - 1), edit_distance(string1, string2, len_string1 - 1, len_string2), edit_distance(string1, string2, len_string1 - 1,  len_string2 -1))

def main():  #Test cases using hard coded strings. 
    print("Testing 'money' and 'miners'. Getting minimum operations.")
    string1 = "money"
    string2 = "miners"

    min_num = edit_distance(string1, string2, len(string1), len(string2))
    print(min_num, "\n")

    print("Testing 'testing' and 'nesting'. Getting minimum operations.")
    string3 = "testing"
    string4 = "nesting"

    min_num = edit_distance(string3, string4, len(string3), len(string4))
    print(min_num, "\n")

    print("Testing 'tommy' and 'johnny'. Getting minimum operations.")
    string5 = "tommy"
    string6 = "johnny"

    min_num = edit_distance(string5, string6, len(string5), len(string6))
    print(min_num)
main()