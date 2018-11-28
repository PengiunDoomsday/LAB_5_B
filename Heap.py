"""
@author Rocorral
ID: 80416750
Instructor: David Aguirre
TA: Saha, Manoj Pravakar
Assignment:Lab 5-B -Heaps
Last Modification: 11/27/2018
Program Purpose: The purpose of this program is to practice the
implementation of heaps and use its data structure to preform a heap sort.
"""

class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self,k):
        '''adds a new element to the heap and ensures it is in the right location'''
        self.heap_array.append(k)
        self.bubbleup()
        
    def swap(self, index_one, index_two):
        '''given two indecies swaps the elements'''
        temp = self.heap_array[index_one]
        self.heap_array[index_one] = self.heap_array[index_two]
        self.heap_array[index_two] = temp

    def extract_min(self):
        '''returns the element in position 0 of the array the "min elemnt"  '''
        if self.is_empty():
            return None
        if len(self.heap_array) == 1:#avoids index out of bounds
            return self.heap_array.pop(0)
        min_elem = self.heap_array[0]
        self.heap_array[0] = self.heap_array.pop(len(self.heap_array)-1)
        #replaces position 0 with and while removing the end
        self.bubbledown()
        return min_elem

    def is_empty(self):
        '''returns True if empty'''
        return len(self.heap_array)==0

    def bubbleup(self):
        '''moves element in last index position to its correct position'''
        index = len(self.heap_array)-1
        while self.has_parent(index)  and  self.parent(index) > self.heap_array[index]:
        # do we have a parent and is it smaller
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def bubbledown(self):
        '''moves element from position one down to its correct position'''
        index = 0
        while self.has_left_child(index):#has to have a left child if any
            smaller_child_index = self.get_left_child_index(index)#we assume its the smallest
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
            #we switch if its not the smallest'''
                smaller_child_index = self.get_right_child_index(index)
            if self.heap_array[index] < self.heap_array[smaller_child_index]:
            #if the parent is smaller than the child no need to continue
                break
            else:# all else fails swap
                self.swap(index,smaller_child_index)
            index= smaller_child_index #update index for next possible swap

#-------Helper Defs--------
    ''' a set of definitions to make things clear'''

    '''gets indecies'''
    def get_left_child_index(self, parent_index):
        return (2 * parent_index) + 1
    def get_right_child_index(self, parent_index):
        return (2 * parent_index) + 2
    def get_parent_index(self, child_index):
        return (child_index -1) // 2

    '''checks for children or parent'''
    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap_array)
    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap_array)
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    '''returns elements of parent or children'''
    def left_child(self, index):
        return self.heap_array[self.get_left_child_index(index)]
    def right_child(self, index):
        return self.heap_array[self.get_right_child_index(index)]
    def parent(self, index):
        return self.heap_array[self.get_parent_index(index)]