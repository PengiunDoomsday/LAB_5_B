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

import Heap
import io
def read_file_to_heap(file):
	'''reads from file numbers seperated by commas'''
	heap = Heap.Heap()
	for_heap = io.open(file ,'r+', encoding = "UTF-8")
	for line in for_heap:
		a = line.split(',')
		print("The file reads:-------------",a)
		for num in a:
			heap.insert(float(num))
	return heap

def heap_sort(heap):
	'''simply extracts min and appends it to tnew array'''
	sortedheap = []
	while heap.is_empty() == False:
		sortedheap.append(heap.extract_min())
	return sortedheap

#-------main---------
myheap = read_file_to_heap('numbers.txt')
print("Heap array after insertion:-",myheap.heap_array)
sheap = heap_sort(myheap)
print("Heap sorted:----------------",sheap)

#Please read comment
#What happens when a non integer is added to the equation, 
#lets say ")" or "sd" would the code still work? If it does would it use the ascii value of the character?
