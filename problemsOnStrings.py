#1. Given a string, check if the string is palindrome or not."  A string is said to be palindrome
#if the reverse of the string is the same as the string.
str = input("Enter a string:")
temp = str[::-1]  
if temp == str:
    print("Palindrome")
else:
   print("Not palindrome")
 
  #2. write a program to count the number of vowels, consonants, and spaces in that string.

str1 = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0

for ele in str1:
    if ele in "AEIOUaeiou":
        vowels += 1
    elif ele == " ":
        spaces += 1
    elif ele not in "AEIOUaeiou":  
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
#3. Given a character, Find the ASCII value of the character.
a = input("enter a character:")
ascii_value = ord(a)  

print("The ASCII value of", a, "is", ascii_value)
#4.calculate the sum of numbers in a string (multiple consecutive digits are considered one number)
str1 = input("Enter a string: ")

num = ""
total = 0

for ch in str1:
    if ch.isdigit():
        num += ch       
    else:
        if num != "":
            total += int(num)
            num = ""    


if num != "":
    total += int(num)

print("Sum of numbers in string:", total)
#5.Write a program to concatenate one string's contents to another. 
# Concatenation means to join two (or more) strings and form a combined string having the characters of both ( or all) strings in the same order as they were before in separate strings.
str1 = input("Enter a string:")
str2 = input("Enter a string:" )
temp = str1 + str2
print(temp) 