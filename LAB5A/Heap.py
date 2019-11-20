# Implementation of max heap
# Programmed by Olac Fuentes
# Modified by David Morales
# Last modified November 19, 2019

import matplotlib.pyplot as plt
import math


class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return -math.inf
        parent_list = self.tree[(i - 1) // 2]

        return parent_list[1]

    def left_child(self, i): #These methods were modified to take an list of two. The count and the word. 
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        c_list = self.tree[c] 
        return c_list[1]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        c_list = self.tree[c]
        return c_list[1]

    def insert(self, item):
        #print(self.tree, item)
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def file_parser(filename): #Takes in filename
        dict = {}
        word_heap = MaxHeap()

        with open(filename, encoding='windows-1252') as textFile:  #Adds to to the dictionary.
            for line in textFile:
                string = line.split()
                word = str(string)
                word_str = word[2:len(word) - 2]

                if word_str in dict: #Adds to count of the word if duplicates are found. 
                    counter = dict.get(word_str) + 1
                    updated_pair = {word_str : counter}
                    dict.update(updated_pair)

                else: 
                    dict[word_str] = 1 

        for key in dict: #Inserts the info from the dictionary into the heap 
            word_heap.insert([key, dict[key]])

        return word_heap, dict

    def caps_detector(self, char): #Checks if a letter is capitalized, then returns the lower case equalivent if the letter is capitalized.  
        cap_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

        lower_char = '' 
        for i in range(len(cap_list)): 
            if (char == cap_list[i]): 
                lower_char = lower_list[i] 
                return lower_char

        return char 

    def print_decending(self, num_of_times): #Prints descending order 
        if (len(self.tree) < num_of_times): 
            print("Invalid number. Try again")
            return

        most_seen_word = self.tree[0]

        for i in range(num_of_times):
            word = self.extract_max()
            print("Word:", word[0], "|", "Number of times:", word[1])

        print("\n")
        print("Most seen word:", most_seen_word[0])
        print("Number of times:", most_seen_word[1])

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2
        parent_val = self.tree[parent_index]
        i_val = self.tree[i] 
        
        if parent_val[1] == i_val[1]:  #If the count equals 
            parent_word = list(parent_val[0])
            i_word = list(i_val[0])
            iter = min(len(i_word), len(parent_word))

            for i in range(iter):
                i_letter = self.caps_detector(i_word[i]) #Replaces uppercase letters with lowercase letters. 
                parent_letter = self.caps_detector(parent_word[i])

                if i_letter > parent_letter: 
                    i_val[0], parent_val[0] = parent_val[0], i_val[0]
                    i_val[1], parent_val[1] = parent_val[1], i_val[1]
                    self._percolate_up(parent_index)

                elif i_letter < parent_letter:
                    return

        if parent_val[1] < i_val[1]:
            i_val[0], parent_val[0] = parent_val[0], i_val[0]
            i_val[1], parent_val[1] = parent_val[1], i_val[1]
            self._percolate_up(parent_index)

    def extract_max(self): 
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]

        self.tree[0] = self.tree.pop()

        self._percolate_down(0)

        return root

    def _percolate_down(self, i): #Modified method to percolate down. 
        i_val = self.tree[i]

        if i_val[1] >= max(self.left_child(i), self.right_child(i)):
            return

        if self.left_child(i) > self.right_child(i):
            max_child_index = 2 * i + 1 

        else:
            max_child_index = 2 * i + 2

        max_list = self.tree[max_child_index]
        i_val[0], max_list[0] = max_list[0], i_val[0]
        i_val[1], max_list[1] = max_list[1], i_val[1]
        self._percolate_down(max_child_index)

    def size(self): 
        return len(self.tree)
