#!/usr/bin/python
# Ask user
enter_string =raw_input("Enter a string: ")    
x= list(enter_string)                         
print list(enter_string)
x.reverse()                           											 
if list(enter_string) == x:                     
	print("It is a palindrome")
else:
	print("It is not a palindrome")