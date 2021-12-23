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

#Steps to solve:
#1. create a function, include parameters for the target as well as the list of integers
#2. create a for loop with a range of the length of the function
#3. create a for loop within that for loop again for the range of the function
#4. both for loops will be obtaining indices 
#5. have an if statement checking if the number at the index from the first loop plus the number at the index from the second for
# loop add up to the target
#6. include a nested if statement to exclude when index one and two are the same, to fulfill the not using the same element
# twice requirement
#7. within nested if statement in for loops, return the two indices. this will be so the first solution found is the one
#returned. I have to assume this is what "each input would have exactly one solution" is meant to mean, because there
#seems to be no way to control that from within the function given that the input is passed in through an argument
#8. also print a statement at the end of the function, which will only print if no two numbers add up to the target
#9. tested; success

#Honestly the instructions for this particular problem were very confusing, so I have built this function on the 
# assumption that we want to be able to take in a list of any length, and any target number, and return the index positions
# of the first two numbers that add up to the target. Hopefull that is the correct interpretation

def indices_of_numbers_adding_up_to_target(target, list_of_nums):
    for index in range(len(list_of_nums)):
        for index_2 in range(len(list_of_nums)):
            if list_of_nums[index] + list_of_nums[index_2] == target:
                if index != index_2:
                    return [index, index_2]
    print("Unable to obtain result. No two numbers in the list given add up to the target.")

test_list = [34, 45, 1, 23, 11, 16, 3, 5, 7]
print(indices_of_numbers_adding_up_to_target(25, test_list))



#2. Palindrome is a word, phrase, or sequence that reads the same backward as 
#forward i.e. madam. Write code that takes a user input and checks to see if it 
#is a Palindrome and reports the result. You must handle spaces. 

#Steps to solve:
#1. Already created palindrome checker in previous worksheet, but did not account for spaces.
#2. Paste previous palindrome checker as base.
#3. function to reverse string will include spaces, but that is so Hello World becomes dlroW olleH. That means
# if we passed in the phrase "A man, a plan, a canal: Panama" it would reverse it with all spaces and characters,
#so it would not be exactly equal to the original, and it would say it's not a palindrome when it is
#4. so we need a way to ignore spaces and other characters
#5. we will try to do this from within the palindrome function instead of the reverse function, so that we don't limit the 
# reverse function's utility
#6. we will have to create a new empty string, and a for loop that stores all the letters in it and none of the other characters
#7. we will also convert it to all lowercase
#8. then we will see if this new letters-only string is equal to its reverse
#9. test; success!

def reverse_str(original_str):
    converted_str = ""
    for character in original_str:
        converted_str = character + converted_str
    return converted_str

test_reverse = reverse_str("lizzy")
print(test_reverse)

def palindrome_checker():
    user_entry = input("Enter word or phrase to see if it is a palindrome. ").lower()
    user_entry_letters_only = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for character in user_entry:
        if character in letters: 
            user_entry_letters_only += character
    if user_entry_letters_only == reverse_str(user_entry_letters_only):
        print("Yes, this is a palindrome.")
    else:
        print("Sorry, this is not a palindrome.")

palindrome_checker()


#3. Given a list of integers, return a bool that represents whether or not all 
#integers in the list can form a sequence of incrementing integers
#a. Use case: 
#i. {5, 7, 3, 8, 6}  false (no 4 to complete the sequence)
#ii. {17, 15, 20, 19, 21, 16, 18}  true

#problem solving steps:
#1. create and name a function
#2. create a parameter to pass in a list of integers
#3. create a variable to hold the lowest number and assign it to index 0 of the list
#4. create a for loop going through a range (can exclude index 0) to compare each index of the list to the number at index 0
#5. any time a number is lower than the lowest number variable, it replaces the value of the lowest num variable
#6. once for loop is complete, create a new variable to count and set it equal to the lowest number variable
#(it's not really necessary to use a new variable; we could keep using the lowest_num variable, but because
# it will no longer be containing the lowest number, readability is better with a new variable)
#7. create a while loop so it continues to run as much as necessary
#8. within the while loop, remove count from the list; then check to see if the list still contains the value of count
#9. if the list still contains the value, then the value was there twice, and therefore is not incrementing; return false
#10. then create an elif statement to see if the next number above the current count is in the list
#11. if it isn't, then either the list is not incrementing or that was the highest variable in the list.
# create an if statement for each possibility. if it was the last number in the list, return True. otherwise, return False
#12. test; success!

def can_form_incrementing_int_sequence(list_of_integers):
    lowest_num = list_of_integers[0]
    for index in range(1, len(list_of_integers)):
        if list_of_integers[index] < lowest_num:
            lowest_num = list_of_integers[index]
    count = lowest_num
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

example_list = [7, 1, 9, -1, 3, 0, 2, 6, 8, 5]
print(can_form_incrementing_int_sequence(example_list))




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
#11. within the for loop, separate each part of the email address into different categories
#12. then assess the category for the recipient name with the specific rules for that category
#13. then assess the domain name with the rules for that category
#14. then assess top level domain name with rules for that category. Ideally, we would make a list of all
# possible top level domain names and check to see if it is in that list. But because that list is almost 2000 and doesn't account
# for potential add-ons (like the list includes co and uk but not co.uk, which is also valid) instead, I will make a non-comprehensive
#list that includes only a few very common top level domain names
#15. this list also can't account for mismatches like gmail needing to end in .com, because we can't have a comprehensive list
#of potential domain names and what they match to


def validate_email_address(email_provided):
    top_level_domains = [".net", ".com", ".edu", ".org", ".gov"]
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
    if len(domain_name) < 1 or len(domain_name) > 253:
        print("This is not a valid email.")
        return False
    for character in domain_name:
        if character not in letters and character not in numbers:
            if character != "." and character != "-":
                print("This is not a valid email.")
                return False
            else:
                if prev_character == "":
                    prev_character = character
                else:
                    print("This is not a valid email.")
                    return False
        else:
            prev_character = ""
    if top_level_domain not in top_level_domains:
        print("This is not a valid email.")
        return False
    print("This is a valid email.")
    return True

email_address = "testing.what@gmail.com"
is_valid_email = validate_email_address(email_address)







#7. Create a method that takes in a string and replaces each letter with its 
#appropriate position in the alphabet and returns the string
#a. Use case:
#i. “abc”  “1 2 3”
#ii. “coding is fun”  “3 15 4 9 14 7 9 19 6 21 14”

#Steps to solve:
#1. we know we will need a for loop to analyze each character in the string
#2. probably the simplest way to do it will be to use indices. 
#3. search how to find the index of a specific element in python: .index() function
#4. create and name a function
#5. create a string with the alphabet
#6. convert input to lowercase so we don't have to deal with caps 
#7. create an empty string to hold the converted string
#8. create for loop
#9. create an if statement to account for spaces or any other characters that aren't letters
#10. create a variable and set it equal to the index of the character in the alphabet plus one
#11. convert the value to a string
#12. add the string value of the variable to our conversion string
#13. the example has spaces. add a space after the value
#14. the end of the string doesn't have a space. how do we account for this?
#15. added an if statement in the for loop to see if it is the first character to be added to the conversion string. 
# if it is, we will add it without a space. for all others, we will add a space first and then the number
# 16. return the new string
#17. test; success!

def replace_letter_with_position_in_alphabet(orig_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    orig_string = orig_string.lower()
    num_str = ""
    for character in orig_string:
        if character in alphabet:  
            num = str(alphabet.index(character) + 1)
            if num_str == "":
                num_str += num
            else:
                num_str += " " + num
    return num_str

convert_phrase_to_nums = replace_letter_with_position_in_alphabet("What's good party people??? Test it!")
print(convert_phrase_to_nums)


#8. A briefcase has a four-digit rolling-lock. Each digit is a number from 0-9 that 
#can be rolled either forwards or backwards. Write a method that returns the 
#smallest number of turns it takes to transform the lock from current 
#combination to the target combination. One turn is equivalent to rolling a 
#number forwards or backwards by one. 
#a. Use case: 
#i. Current lock: 3893
#ii. Target lock: 5296

#Steps to solve
#1. create a function
#2. we will probably need to create a variable to count the total turns. start by assigning that variable to 0
#3. then we will just need to know the difference between the current lock at each index and the target lock at that same index
#4. we will make that number positive regardless, then add it to the count variable
#5. since it will be exactly 4 digits every time, we don't need a for loop. but we will use one because it is prettier.
#6. realize that this function works but does not account for the fact that the lock rolls in both directions
#7. realize it takes 10 turns in either direction to get a number back to itself. so the highest acceptable amount of turns should
# be 5, because if it's 5 it's the same either way. Any difference higher than 5 and it is quicker to go the opposite direction
#8. make an if statement for if the difference is less than or equal to five, add it to the count
#9. make an else statement where if the difference is greater than 5, subract the difference from 10 and add that to the count
#10. test; issue because cannot take index of a number. convert combos to string, then when finding difference convert 
#individual numbers back to integers
#11. test again; success!

def smallest_number_of_turns_to_unlock(current_combo, correct_combo):
    count = 0
    current_combo = str(current_combo)
    correct_combo = str(correct_combo)
    for index in range(4):
        difference = int(current_combo[index]) - int(correct_combo[index])
        if difference < 0:
            difference *= -1
        if difference <= 5:
            count += difference
        else:
            opp_diff = 10 - difference
            count += opp_diff
    return count

open_brief_case = smallest_number_of_turns_to_unlock(3893, 5296)
print(open_brief_case)




#9. Happy Numbers
#a. A happy number is a number defined by the following process: starting
#with any positive integer, replace the number by the sum of the 
#squares of its digits, and repeat the process until the number equals 1. 
#An example of a happy number is 19

#COPIED FROM PREVIOUS WORKSHEET

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
    
is_happy = (determine_if_happy(999))
print(is_happy)


#10.Given a number, return the reciprocal of the reverse of the original number, 
#as a double. 
#a. Use case: If given 17, return 0.01408 (1/71)

#Steps to solve:
#1. we can use a lot of the same process as we did to reverse a string for the first part of this. 
#2. we will make a function, create an empty string to hold the backwards string, and make a for loop
#3. in the for loop we will use range and go from the end of the loop to the beginning
#4. in the for loop we will add each character to the string
#5. then we can convert the string to an integer 
#6. then we'll divide one by the integer and return the result
#7. test--success!

def reciprocal_of_reverse_num(orig_value):
    orig_str = str(orig_value)
    reverse_str = ""
    for index in range(len(orig_str) -1, -1, -1):
            reverse_str += orig_str[index]
    reverse_num = int(reverse_str)
    reciprocal = 1 / reverse_num
    return reciprocal

print(reciprocal_of_reverse_num(34556))

