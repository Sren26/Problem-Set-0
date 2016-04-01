# Author: Sanford Ren
# Date: March 31st 2016

# Import da other ps0 file where the main functions are at
import ps0 


# Tests for each function below

# Function 0
print (" \n Function 0: Is a number Even or Odd?: Testing 0, 6, 277") 
print ("0: " + ps0.is_even(0)) 
print ("6: " + ps0.is_even(6))
print ("277: " + ps0.is_even(277))


# Function 1
print (" \n Function 1: Number of Digits in a Number: Testing 0, 5, 447, 5236783") 
print ("0: " + str(ps0.num_digits(0)))
print ("5: " + str(ps0.num_digits(5)))
print ("447: " + str(ps0.num_digits(447)))
print ("5236783: " + str(ps0.num_digits(5236783)))


# Function 2
print (" \n Function 2: Sum of Digits in a Number: Testing 0, 7, 123, 8924") 
print ("0: " + str(ps0.sum_digits(0)))
print ("7: " + str(ps0.sum_digits(7)))
print ("123: " + str(ps0.sum_digits(123)))
print ("8924: " + str(ps0.sum_digits(8924)))


# Function 3
print (" \n Function 3: Sum of the numbers smaller than a Number: Testing 0, 6, 27, 100") 
print ("0: " + str(ps0.sum_less_ints(0)))
print ("6: " + str(ps0.sum_less_ints(6)))
print ("27: " + str(ps0.sum_less_ints(27)))
print ("100: " + str(ps0.sum_less_ints(100)))


# Function 4
print (" \n Function 4: Factorial of Number: Testing 0, 4, 79") 
print ("0: " + str(ps0.factorial(0)))
print ("4: " + str(ps0.factorial(5)))
print ("79: " + str(ps0.factorial(79)))


# Function 5
print (" \n Function 5: Is x a factor of y?  Factoring 0 into 8, 4 into 56, 23 into 69, 345 into 9832")
print ("0 into 8: " + str(ps0.is_factor(0,8)))
print ("4 into 48: " + str(ps0.is_factor(4,56)))
print ("23 into 69: " + str(ps0.is_factor(23,69)))
print ("345 into 9832: " + str(ps0.is_factor(345,9832)))


# Function 6
print (" \n Function 6: Is a number Prime?: Testing 0, 1, 2, 11, 64, 93: True = Prime, False = Not Prime") 
print ("0: " + str(ps0.is_prime(0)))
print ("1: " + str(ps0.is_prime(1)))
print ("2: " + str(ps0.is_prime(2)))
print ("11: " + str(ps0.is_prime(11)))
print ("64: " + str(ps0.is_prime(64)))
print ("93: " + str(ps0.is_prime(93)))


# Function 7
print (" \n Function 7: Is a number Perfect?: Testing 0, 6, 12, 20, 48, 496: True = Perfect, False = Not Perfect") 
print ("0: " + str(ps0.is_perfect(0)))
print ("6: " + str(ps0.is_perfect(6)))
print ("12: " + str(ps0.is_perfect(12)))
print ("20: " + str(ps0.is_perfect(20)))
print ("48: " + str(ps0.is_perfect(48)))
print ("496: " + str(ps0.is_perfect(496)))


# Function 8
print (" \n Function 8: Is a number Divisible by the sum of its Digits?: Testing 0, 12, 59, 81, 333, 7836: True = Divisible, False= Not Divisible") 
print ("0: " + str(ps0.divisble_by_sum_digits(0)))
print ("12: " + str(ps0.divisble_by_sum_digits(12)))
print ("59: " + str(ps0.divisble_by_sum_digits(59)))
print ("81: " + str(ps0.divisble_by_sum_digits(81)))
print ("333: " + str(ps0.divisble_by_sum_digits(333)))
print ("7836: " + str(ps0.divisble_by_sum_digits(7836)))