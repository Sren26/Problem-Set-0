# Author: Sanford Ren
# Date: March 30th 2016

# Functions for each purpose below

""" Function 0 """
def is_even(number):

	''' Takes an integer as a parameter and returns True if the number is even, False if it is odd. ''' 

	number = int(number) 
	if number % 2 == 0: 
		return "Even" 
	else:
		return "Odd" 
	

""" Function 1 """
def num_digits(number):

	''' Takes a non-negative integer as a parameter and returns the number of its digits. '''
	
	count = 0 
	
	while number >= 1:
		number = number / 10  
		count += 1 

	return count 


""" Function 2 """
def sum_digits(number):
	
	''' Takes a non-negative integer as a parameter and returns the sum of its digits. '''
	
	sum = 0
	while number > 0: 
		nextDigit = number % 10 # To find the last digit of number 
		sum = sum + nextDigit  # To add the digit to the sum 
		number = (number - nextDigit) / 10  # Taking off the ones digit on the remaining number
	return sum 
	

""" Function 3 """
def sum_less_ints(number):

	''' Takes a non-negative integer as a parameter 
	and returns the sum of all the integers that are less than the given number. ''' 

	number = int(number)
	intList= []  # To create the list of integers 
	
	while number >= 1: 
		intList.append(number)
		number = number - 1 # To find all the integers above 0
	
	return sum(intList)
	

""" Function 4 """
def factorial(number):

	''' Takes a non-negative integer as a parameter and returns its factorial. '''
	
	if number == 0: 
		return 1  # The factorial of 0 is 1 
	else:
		number = int(number)
		intList= [] # To create the list of integers less than the number to be factorialized(Is that a word?)
	
		while number >= 1: 
			intList.append(number) # To add each smaller integer to teh list 
			number = number - 1 
	
		product = 1  # Set factorial to 1 before the multiplication
		for x in intList[:len(intList)]: 
			product *= x # Multiply each integer in the list together 
	
		return product 
	
	
""" Function 5 """
def is_factor(number1,number2):

	''' Takes two positive integers and finds out whether
	 the second number is a factor (divisible w/o remainders) of the first. '''
	
	if number1 == 0 or number2 == 0: # 0 is not a factor of anything
		return False
	else: 
		if int(number2) % int(number1) == 0: # To see if number2 is a factor of number1 
			return True 
		else:
			return False
			

""" Function 6 """
def is_prime(number):

	''' Takes an integer greater than or equal to 2 and returns 
	whether the integer is a prime number. ''' 
	
	if number == 1 or number == 0: # 1 and 0 are not prime, can be automatically eliminated
		return False 
	else:  # To test if the number can be divided evenly by 2, 3, 5, 7, common prime factors
		if int(number) % 2 == 0 and int(number) != 2: 
			return False
		if int(number) % 3 == 0 and int(number) != 3:
			return False
		if int(number) % 5 == 0 and int(number) != 5:
			return False
		if int(number) % 7 == 0 and int(number) != 7:
			return False
		else:
			return True
	
		
""" Function 7 """
def is_perfect(number):

	''' Takes a positive integer and returns whether the number is perfect. '''
	
	l = [] 
	numbers = []
	
	for i in range(1, number + 1): 
		if number % i == 0: 
			l.append(i) 
	if number == 0: # Number cannot be 0, as it's not perfect 
		return False 
	else:
		if sum(l) - number == number: # If the sum of the factors = number 
		 	return  True 
		else: 
			return False


""" Function 8 """
def divisble_by_sum_digits(number): 

	''' Takes a positive integer and returns true if the sum of the digits
	 of the number divides evenly into the number, false otherwise. '''
	
	if number == 0: # Number cannot be zero 
		return False 
	else:
		sum = sum_digits(number)   # If the sum of digits = Sum of the digits 
		if number % sum == 0:
			return True
		else:
			return False 

	
