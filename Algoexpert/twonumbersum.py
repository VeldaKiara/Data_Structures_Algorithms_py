#sol 1
#using  a for loop to loop through the numbers
#and checking if the sum is equal to the target

# using two for loops with a 0(n^2) / 0(1)space
def twoNumberSum(array, targetSum):
	for i in range(len(array)-1): #all the way to the before last value
		first_number = array[i]  
		for j in range(i + 1, len(array)): #iterate thru all numbers
			second_number = array[j] #goes all the way to the end of array
			if first_number + second_number == targetSum:
				return[first_number, second_number] 
	return [] #in case we do not hit any of the numbers
	

# using sliding window that is two pointers to the left and right
# and checking if the sum is equal to the target

# 0(nlog(n)) / 0(1) space
def twoNumberSum(array, targetSum):
	#sliding windowusing pointers, sort the array first 
    # items on the left are smaller, items on the right are larger
	array.sort() #sort the numbers to arrange them in order of increment
	left = 0
	right = len(array) - 1 #last item
	#iterate
	while left < right:
		currentSum = array[left] + array[right]
		if currentSum == targetSum:
			return [array[left], array[right]]
		elif currentSum < targetSum:
			left += 1 #move the left pointer a step forward
		elif currentSum > targetSum:
			right -= 1 #move the right pointer a step backward
	return []
	
#using a hashtable to store the numbers
#and checking if the sum is equal to the target

# using a hashtable
# 0(n) time / 0(n)space because we are storing this value
def twoNumberSum(array, targetSum):
	numbers = {} #store the numbers you find here
	for number in array:
		potentialMatch = targetSum - number
		if potentialMatch in numbers:
			return [potentialMatch, number]
		else:
			numbers[number] = True #store the number in the hashtable
	return []

  