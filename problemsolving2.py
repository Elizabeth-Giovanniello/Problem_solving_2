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
#8. create a variable for the new number and have it outside the for loop, set equal to 0
#8. within the for loop, have each character converted back into an integer and multipy by itself
#9. then add the squared number to the new number variable
#10. create an outer while loop so the loop continues until the number equals 1
#11. Now we need a way of determining when a number is sad, otherwise the while loop will go forever
#12. Researched and found that 7 is the only happy number between 1 and 10
#13. Create an if statement for when the new_num variable is a single digit again
#14. Create an if statement for when it is 7 (because once a number gets to single digits and is anything other than 1 or 7, we know it can never be happy)
#15. return false if the number is single digit and not 7
#16. debug; see issue because number isn't updating
#17. set new_num equal to num at the end of the for loop. move where num is converted to a string to within the while loop, 
# so that the string updates with each round
#18. debug; issue because new_num isn't resetting. move the statement setting new_num to 0 within the while loop
#19. return True at end, if function makes it past the while loop

def determine_if_happy(num):
    num = int(num)
    while num != 1:
        num_str = str(num)
        new_num = 0
        for character in num_str:
            integer = int(character)
            squared_num = integer * integer
            new_num += squared_num
            num = new_num
        if new_num > 1 and new_num <= 9:
            if new_num != 7:
                print("This value is not a happy number")
                return False
    print("This value is a happy number!")
    return True
    
is_happy = (determine_if_happy(100))
print(is_happy)

        



# 2. Prime Numbers

# a. A prime number is a number that is only divisible by one and itself.

# b. Write a method that prints out all prime numbers between 1 and 100

# 1. create and name the function
# 2. create a for loop with a range 1-101 so that numbers 1 through 100 are addressed
# 3. create an if statement to see if num remainder 2 equals 0. Since 2 is the only prime number divisible by 2, 
# create a nested if statement to see if num is equal to 2
# 4. if num is equal to 2, print num because that means it is prime
# 5. create further elif statements with nested if statements for all other single digit prime numbers
# 6. the thought is, all numbers are divisible by 1 so we can skip that. otherwise, a non-prime number will have to be 
# divisible by at least one of these single digit numbers.
# 7. make else statement so if none of the conditions are met, it prints num
# 8. put in parameters instead of numbers for the range, so the range can be adjusted
# 9. debug; no issues

def print_prime_nums_in_range(starting_num, ending_num):
    for num in range(starting_num, (ending_num + 1)):
        if num % 2 == 0:
            if num == 2:
                print(num)
        elif num % 3 == 0:
            if num == 3:
                print(num)
        elif num % 5 == 0:
            if num == 5:
                print(num)
        elif num % 7 == 0:
            if num == 7:
                print(num)
        else:
            print(num)


print_prime_nums_in_range(1, 51)

# 3. Fibonacci

# a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.

# b. Write a method that does the Fibonacci sequence starting at 1

# c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs


#Steps to solve:
#1. create and name a function
#2. create a variable to hold the list of numbers and set it equal to [1]
#3. create a while loop for while the length of the list is less than 15, so it doesn't go on forever
#4. create an if statement for when the list has only one value. Append that value to the list 
#5. outside the if statement but still in the while loop, create a variable to hold a new value
#6. add the last value in the list to the second to last value in the list and store it in the new variable
#7. append the new value to the end of the list
#6. test and debug; works. add in parameter instead of 1, and test again with new number
#7. Now to change so that it works with user input: add user input as argument to be passed into function, and convert to integer

def fibonacci(num):
    sequence = [num]
    while len(sequence) < 15:
        if len(sequence) == 1:
            sequence.append(sequence[0])
        else:
            new_value = sequence[-1] + sequence[-2]
            sequence.append(new_value)
    return sequence

fibonacci_sequence = fibonacci(1)
print(fibonacci_sequence)

fib_number = int(input("Enter a number to use as a starting point for our Fibonacci sequence: "))
print(fibonacci(fib_number))

start_fibonacci = fibonacci(int(input("Enter a number to begin our Fibonacci sequence: ")))
print(start_fibonacci)