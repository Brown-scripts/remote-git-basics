'''print("Hello World")

a = 3
a = 32
a = 1
print(a+a+a)'''

# data types
'''a = 3.142
b = 34
c = True
d = "Happy Day"
d1 = "123@csdjkcf"

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(d1))'''

# type conversion
# print(int(a))

#Concatenation
'''print('My '+'name '+'is '+'Nicole ')

name= input('Enter your name: ')
age = input('Enter your age: ')
age= int(age) + 5
print('Your name is ' +name +'. You are '+ str(age)+' years old')

#formatted strings
print(f'Your name is {name} and You are {age} years old')'''

# INDEXING AND SLICING
'''word = 'helicopter'
print(word[-1])
print(word[4])
print(word[:5])
print(word[3:])'''

# ask a user to enter any 2 digit number
# take the number, separate and add
#print the output

'''number = input("Enter any 2 digit number: ")
num1= number[0]
num2= number[1]
sum = int(num1)+int(num2)
print(f'Your number is {number}. The sum is {sum}')'''

#enter weight in kg and height in m
'''weight= float(input('Enter your weight in kilogram '))
height= float(input('Enter your height in meters '))
bmi= weight/(height*height)
print(f'Your weight is {weight} and height is {height}. Your BMI is {round(bmi,2)}')
#Conditional Statements
#determine if the number a user has entered is even or odd'''

'''number= int(input('Enter a number '))

if number%2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')
'''

#use conditonal statements to categorize the bmi
'''if bmi<=18:
    print('You are underweight')
elif bmi>=19 and bmi <=25:
    print('You are normal weight')
elif bmi>=26 and bmi <=30:
    print('You are overweight')
else:
    print('You are Obese')'''


# Randomisation
import random

'''dice_value = random.randint(1,6)
print(dice_value)'''

'''coin_toss = random.randint(1,2)
if coin_toss==1:
    print (coin_toss)
    print("HEADS")
else:
    print (coin_toss)
    print("TAILS")'''

#fruits =['Apple','Orange','Mango','Peach','Grapes']


#For loops
'''import time

for i in range (1,11,2):
    print(i)
    time.sleep(1)'''

#summing first 100 numbers
'''sum=0
for i in range(1,101):
    sum+=i
print(sum)'''

'''sum=0
for i in range(0,101,2):
    sum+=i
print(sum)'''


#While loops

#functions
'''def my_func():
    print('Hello')

my_func()'''


#OOP




    

