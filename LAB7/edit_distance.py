#Author: David Morales
#Course: CS 2302 Data Structures Fall 2019
#Instructor: Diego Aguirre
#T.A: Gerardo Barraza
#Assignment: Lab 7
#Last Modification: 12/02/2019
#Purpose: Implementation of the edit distance algorithm.

def edit_distance(string1, string2): #The recursive version of the edit distance algorithm. (Recursive stacks)
    if len(string1) == 0:  #Returns when it goes through the all string.
        return 0

    if len(string2) == 0: 
        return 0

    if string1[len(string1) - 1] == string2[len(string2) - 1]:  #If characters are equal, it just the returns the substring (minus one of of both string counts). 
        return edit_distance(string1[0 : len(string1) - 1], string2[0 : len(string2) - 1]) 
        
     #Runs through insertion, replacment, and deletion. Gets the minimum of all the added operations.
    return 1 + min(edit_distance(string1, string2[0 : len(string2) - 1]), 
    edit_distance(string1[0 : len(string1) -1], string2), 
    edit_distance(string1[0 : len(string1) - 1], string2[0 : len(string2) - 1]))

def edit_distance_dp(string1, string2): #Dynamic version of edit distance algorithm (using a 2D array).
    m = len(string1)
    n = len(string2)
    sol_table = [[0 for i in range(n + 1)] for i in range(m + 1)]  #Creates the table.

    for i in range(m + 1): #Nested for loop to populate the solution table. 
        for j in range(n + 1): 

            if i == 0:  #Populates top array with 1, 2, 3, 4...
                sol_table[i][j] = j

            elif j == 0: #Populates side array with 1, 2, 3, 4...
                sol_table[i][j] = i

            elif string1[i - 1] == string2[j - 1]: #Compares last character of the two strings, passes down the value if equal. 
                sol_table[i][j] = sol_table[i - 1][j - 1] 

            else: #Gets minimum operations of insertion, deletion, replacment and adds one.
                sol_table[i][j] = 1 + min(sol_table[i][j - 1], 
                sol_table[i - 1][j], 
                sol_table[i - 1][j - 1]) 

    return sol_table[m][n] #Minimum operations at the end of the table.

def main():  #Test cases using hard coded strings. 
    print("Testing 'money' and 'miners'. Getting minimum operations.")
    string1 = "money"
    string2 = "miners"

    min_num = edit_distance(string1, string2)
    min_num2 = edit_distance_dp(string1, string2)

    print("Recursive version:", min_num)
    print("Dynamic programming version:", min_num2, "\n") 

    print("Testing 'testing' and 'nesting'. Getting minimum operations.")
    string3 = "testing"
    string4 = "nesting"

    min_num = edit_distance(string3, string4)
    min_num2 = edit_distance_dp(string3, string4)

    print("Recursive version:", min_num)
    print("Dynamic programming version:", min_num2, "\n") 

    print("Testing 'tommy' and 'johnny'. Getting minimum operations.")
    string5 = "tommy"
    string6 = "johnny"

    min_num = edit_distance(string5, string6)
    min_num2 = edit_distance_dp(string5, string6)

    print("Recursive version:", min_num)
    print("Dynamic programming version:", min_num2, "\n") 
main()