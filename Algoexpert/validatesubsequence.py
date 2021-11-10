''' 
given two non-empty arrays of integers, write a function that determines
 whether the second array is a subsequence of the first one. A subsequence
 of an array is a set of numbers that aren't necessarily adjacent 
 in the array, but that are in the same order as they appear in the array.
 for instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and
so do the numbers [2, 4]. Note that a single number in an array is also a subsequence of the array.

'''
#sol1
def isValidSubsequence(array, sequence):
    #using a pointer
    sequential_index = 0
    for element in array:
        #check if the numbers match, move the pointer to the next element, we use break to be able to opt out in case we get to the end of the array
        if element == len(sequence):
            break
        if sequence[sequential_index] == element:
            sequential_index += 1
    return sequential_index == len(sequence)
 
 
#sol2
def isValidSubsequence(array, sequence):
    arrindex = 0
	seqindex = 0 
    #using two pointers in tandem
	while arrindex < len(array) and seqindex< len(sequence):
        #if both conditions are true, move the sequence pointer, also move the array pointer 
		if array[arrindex] == sequence[seqindex]:
			seqindex += 1
		arrindex += 1
	return seqindex == len(sequence)
