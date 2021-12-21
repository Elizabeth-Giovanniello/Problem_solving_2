#To be a good problem solver, it is important to be able to break problems down. 
# One way to go about this is to write out the steps it will take to solve the problem. 
# These steps are written down in English in a manner that are easily explainable to someone who may not be technical. 
# The idea is that in order to code something out, you first need to have a good understanding of what it is you are attempting to solve.

# For each of the three problem solving problems below, write out the steps it will take to go about solving the problem. 
# For example, once you are done writing out the steps for the “happy numbers” problem, you would then write out the code to solve the problem. 
# You would then repeat the process for each ensuing problem. 
# Ideally, this will be a good habit that you will develop and carry forward with you for all problems you encounter at devCodeCamp and beyond.



# 1. Happy Numbers a. https://en.wikipedia.org/wiki/Happy_number

# b. A happy number is a number defined by the following process: 
# starting with any positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1. 
# An example of a happy number is 19

# c. Write a method that determines if a number is happy or sad

#Steps to solve:
#1. Read and understand what a happy number is.
#2. Just by looking at this, we will probably need to use loops, possibly both a for loop and a while loop, and possibly need to use indexing
#3. name the function
#4. create a parameter for the function
#5. search to see if it is possible to have a for loop loop through an integer; it is not. Same for finding the index.
#6. we will need to temporarily convert the integer to a string for this to work
#7. create a for loop to loop through each character in the variable used as the parameter
#8. create a variable for the new number and have it outside the for loop, set equal to None
#8. within the for loop, have each character converted back into an integer and multipy by itself
#9. then add the squared number to the new number variable
. create an outer while loop so the loop continues until the number equals 1

def determine_if_happy(num):
    num_str = str(num)
    new_num = None
    for character in num_str:
        integer = int(character)
        squared_num = integer * integer
        new_num += squared_num

        (num1 * num1) + (num2 * num2)



# 2. Prime Numbers

# a. A prime number is a number that is only divisible by one and itself.

# b. Write a method that prints out all prime numbers between 1 and 100

# 3. Fibonacci

# a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.

# b. Write a method that does the Fibonacci sequence starting at 1

# c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs