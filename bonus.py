#Steps of the software development process:
#1. Based on a given starting point (feature, task, code block, etc.), what is the 
#expected end result?
#2. What are the written-out steps to go from point A to point B? You need to 
#solve the problem before you begin coding it.
#3. Implementation (coding it out, researching)
#4. Test and debug code (run code with breakpoint, unit test, etc.)
#5. Refactor if necessary. Test again. This continues until functionality is 
#solidified.

#The above steps should be rinse and repeated for every single problem you 
#encounter. Ignoring these steps or straying from them will result in the long way 
#around to solving a problem or even possibly never solving the problem. 

#To be a good problem solver, it is important to be able to break problems down. 
#One way to go about this is to write out the steps it will take to solve the problem. 
#These steps are written down in English in a manner that are easily explainable to 
#someone who may not be technical. The idea is that in order to code something out,
#you first need to have a good understanding of what it is you are attempting to 
#solve. 
# 
# For each of the problems below, write out the steps it will take to go about 
#solving the problem. Then code it out and test!
#You may jump around in these problems. If you get stuck on one problem, begin 
#working on another. If you get stuck on that new problem, go back to working on 
#the previous one. 
#The use cases below are just examples to give you a better idea of what might be 
#passed into the method or what might be outputted from the method. You shouldn’t
#be coding exactly to these examples, but rather, be flexible to handle any data of 
#that data type.

#Whiteboard Challenges
#1. Given an array of integers, return indices of the two numbers such that they 
#add up to a specific target. You may assume that each input would 
#have exactly one solution, and you may not use the same element twice.
#a. Use Case:
#i. Given numbers in an array: [5, 17, 77, 50] 
#ii. Target: 55


#2. Palindrome is a word, phrase, or sequence that reads the same backward as 
#forward i.e. madam. Write code that takes a user input and checks to see if it 
#is a Palindrome and reports the result. You must handle spaces. 


#3. Given a list of integers, return a bool that represents whether or not all 
#integers in the list can form a sequence of incrementing integers
#a. Use case: 
#i. {5, 7, 3, 8, 6}  false (no 4 to complete the sequence)
#ii. {17, 15, 20, 19, 21, 16, 18}  true

#problem solving steps:
#1. create and name a function
#2. create a parameter to pass in a list of integers
#3. create a while loop so the it continues to run
#4. outside the while loop, create a variable and set it equal to 1
#5. within the while loop create a second while loop that checks if our count variable is in the list
#6. 

def can_form_incrementing_int_sequence(list_of_integers):
    something = True
    count = 1 #COME BACK TO THIS BECAUSE RN IT ONLY WORKS FOR POSITIVES
    while something is True:
        while count in list_of_integers:
            list_of_integers.remove(count)
            if count in list_of_integers:
                return False
            elif (count + 1) in list_of_integers:
                count += 1
            else:
                if len(list_of_integers) == 0:
                    return True
                else:
                    return False
        if count not in list_of_integers:
            count += 1
        
list_of_nums = [5, 7, 3, 8, 6]
result = can_form_incrementing_int_sequence(list_of_nums)
print(result)



#4. Create a method that takes an array of positive and negative numbers. 
#Return an array where the first element is the count of the positive numbers 
#and the second element is the sum of negative numbers. 
#a. Use case: [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]

#Steps to solve:
#1. create and name a function
#2. create an if statement for negative numbers
#3. create an if statement for positive numbers
#4. create a variable for sum of negative numbers
#5. create a variable to hold a new array to move the positive numbers to
#6. create a third variable to hold a new array, and put in it the length of the positive numbers array and the value of the negative numbers variable
#7. return new array
#8. debug and test--it works!

def count_pos_sum_of_neg(orig_array):
    sum_of_negs = 0
    array_of_pos = []
    for number in orig_array:
        if number < 0:
            sum_of_negs += number
        else:
            array_of_pos.append(number)
    new_array = [len(array_of_pos), sum_of_negs]
    return new_array

test_array = count_pos_sum_of_neg([7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21])
print(test_array)


#5. Create a method that accepts a string of space separated numbers and 
#returns the highest and lowest number as a string
#a. Use case: “3 9 0 1 4 8 10 2” --> “0 10”

#Steps to solve:
#1. create and name a function
#2. create a for loop 
#3. create an if statement within the for loop for if the character is a space, and one for if it's not a space
#4. create a variable for the highest number and the lowest number and place them at the beginning of the function, outside the for loop
#5. assign variables for highest and lowest number euqal to 0
#6. create second state of if statements within the for loop to convert the caracter in the string to an integer, then compare it to the number set as the lowest/highest numnber
#7. outside the for loop, create a new string adding the lowest number to the highest number
#8. convert the numbers to strings within the new string and add a space
#9. return the new string
#10. realize that if all numbers are negative then 0 will be too high, or if the lowest number is higher than zero then 0 will be too low
#change highest and lowest num variables at beginning to equal the number at index 0 instead
#11. test; realize function works but can only evaluate a single digit at a time, so the highest number can only go up to 9 even if it's actually 999
#12. added in a temporary variable to hold each integer until the next space in the string comes. then when 
#the next space comes, convert the string in the temporary variable to an integer and compare it to the highest and 
# lowest num variables. set the temporary variable back to an empty string
#13. test; realize if the string does not end in a space, the last number will never be evaluated. 
#14. copy logic to compare number to lowest and highest variables, and place it at the end of the function outside the for loop
#15. test; success
#16. code currently doesn't work if string starts with a space. which is probably fine, but to make it more versatile
# I will add in an if statement when setting highest and lowest num variables in the beginning 
#17. changed if statement to while statement so that the code just uses the first non space character in the string
#18. realized this still only works for the first character not the whole number; this is a problem with a negative,
# or if all the numbers are multi-digit numbers, then if the first number is 43 for example it will claim the 
# lowest number is 4, even though there is no 4 in the list
# 19. created an if/else statement following the first while loop to account for single digit numbers and multi digit numbers
#20. tested; realized code doesn't account for extra spaces/starting with spaces in the second half; added an if statement to resolve this
#21. tested; success

def lowest_and_highest(string_of_nums):
    n = 0
    first_num = ""
    while string_of_nums[n] == " ":
        n += 1
    if string_of_nums[n+1] == " ":
        highest_num = int(string_of_nums[n])
        lowest_num =  int(string_of_nums[n])
    else:
        while string_of_nums[n+1] != " ":
            first_num += string_of_nums[n]
            n += 1
        first_num += string_of_nums[n]
        highest_num = int(first_num)
        lowest_num = int(first_num)
    temp_num = ""
    for character in string_of_nums:
        if character != " ":
            temp_num += character
        else:
            if temp_num != "":
                num = int(temp_num)
                temp_num = ""
                if num < lowest_num:
                    lowest_num = num
                elif num > highest_num:
                    highest_num = num
    if temp_num != "":
        num = int(temp_num)
        if num < lowest_num:
            lowest_num = num
        elif num > highest_num:
            highest_num = num
    new_str = str(lowest_num) + " " + str(highest_num)
    return new_str

test = lowest_and_highest("-12 345 -4 -4 -4   -5  -6 -6789 0  ") 
print(test)



#6. Create a method that accepts a string, check if it’s a valid email address and 
#returns either true or false depending on the valuation. Think about what is 
#necessary to have a valid email address.
#a. Use case:
#i. “mike1@gmail.com”  true
#ii. “gmail.com”  false

#Steps to solve:
#1. a valid email address needs at least one character before the @ sign, an @ sign, and then something .com or .net or .edu or .gov
#can't necessarily specify what website, like gmail/aol etc., because some emails are from a person's own website, or a university, etc.
#2. we could have a series of if statements to just see if it even contains the @ sign or the ., but that won't 
# account for if someone enters like l@sdfalkdfsajcom.
#3. look up to see if special characters are allowed in email addresses; see long list of rules for what a valid email is
#4. we may need to create lists or strings for different categories (like letters, numbers, special characters)
#5. probably need to create for loops within for loops to check and see if each character is a certain type of category
#6. Let's start. create and name the function
#7. create variables for numbers letters and spec. characters. assign them everything of each character, as strings for now
#8. we will probably need to create a variable for the first part of the email, and have a for loop go through
# each character in the original string, and add each one to the variable for the first part until it hits an @ symbol
#9. create if statements to return false if the string doesn't have an @ sign or a .
#10. create for loop to address each character in the email
#11. 


def validate_email_address(email_provided):
    email = email_provided.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    special_characters = ".!#$%&'*+-/=?^_`{|"
    recipient_name = ""
    at_symbol = ""
    domain_name = ""
    top_level_domain = ""
    if "@" not in email:
        print("This is not a valid email.")
        return False
    if "." not in email:
        print("This is not a valid email.")
        return False
    for character in email:
        if character == "@":
            at_symbol += character
            if len(at_symbol) > 1:
                print("This is not a valid email.")
                return False
        elif character != "@":
            if at_symbol == "":
                recipient_name += character
            elif top_level_domain == "":
                if character != ".":
                    domain_name += character
                else: 
                    top_level_domain += character
            else:
                top_level_domain += character
    if len(recipient_name) < 1 or len(recipient_name) > 64:
        print("This is not a valid email.")
        return False
    elif recipient_name[0] not in letters and recipient_name[0] not in numbers:
        print("This is not a valid email.")
        return False
    elif recipient_name[-1] not in letters and recipient_name[-1] not in numbers:
        print("This is not a valid email.")
        return False
    prev_character = ""
    for character in recipient_name:
        if character not in letters and character not in numbers and character not in special_characters:
            print("This is not a valid email.")
            return False
        elif character in special_characters:
            if prev_character == "":
                prev_character = character
            else:
                if prev_character == character:
                    print("This is not a valid email.")
                    return False
        else:
            prev_character = ""
                
email_address = "testing.what@gmail.com"
is_valid_email = validate_email_address(email_address)

#need to create a for loop for recipient name, to check for double special characters. also to say if character is not in letters/num/spec.char list, then it isn't valid






#7. Create a method that takes in a string and replaces each letter with its 
#appropriate position in the alphabet and returns the string
#a. Use case:
#i. “abc”  “1 2 3”
#ii. “coding is fun”  “3 15 4 9 14 7 9 19 6 21 14”

#8. A briefcase has a four-digit rolling-lock. Each digit is a number from 0-9 that 
#can be rolled either forwards or backwards. Write a method that returns the 
#smallest number of turns it takes to transform the lock from current 
#combination to the target combination. One turn is equivalent to rolling a 
#number forwards or backwards by one. 
#a. Use case: 
#i. Current lock: 3893
#ii. Target lock: 5296

#9. Happy Numbers
#a. A happy number is a number defined by the following process: starting
#with any positive integer, replace the number by the sum of the 
#squares of its digits, and repeat the process until the number equals 1. 
#An example of a happy number is 19

#10.Given a number, return the reciprocal of the reverse of the original number, 
#as a double. 
#a. Use case: If given 17, return 0.01408 (1/71)