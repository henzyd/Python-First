##### PEMDAS
## Parantesis
## Exponentials
## Multiply
## Divide
## Addition 
## substraction




## Write a program that takes 3 numbers from the user and computes the average
first_num_input = int(input('I need 3 numbers from you, give me the first number: ')) 
second_num_input = int(input('Give me the second number: ')) 
third_num_input = int(input('Give me the third number: '))

average = (first_num_input + second_num_input + third_num_input) / 3
print(f'The average is : {average}')



## Write a program that takes a sentence from the user and changes the first word to upper case.
sentence = input('Are you wise: ').lower
if 'yes':
    user_input = input('Ok then, type in a quote: ').capitalize()
    print(f'Your quote was "{user_input}"')
elif 'no': 
    print('Well this is not for you leave now')
else:
    print('Did you give me an answer? cause i specified yes or no')



## Write a program with the sentence "I am learning python". When your program is run, the string "I" should be changed to "you"
program = 'I am learning python😁'
print(program.replace('I am', 'You are'))



## Write a program that takes the string "I hope you had fun today in class". Print the number of times that the string "a" appears in the sentence.
fun_in_class = 'I hope you had fun today in class'
print(fun_in_class.count('a'))