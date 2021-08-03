# Given an integer 'n' write a program to generate a dictionary with (i, i*i) such that i is  an integer between 1 and n (both included).The program should then print the dictionary.


number = int(input("Enter a number: ")) 

number_dictionary = {}
for i in range(1, number+1):
    number_dictionary[i] = i*i

print(number_dictionary)
