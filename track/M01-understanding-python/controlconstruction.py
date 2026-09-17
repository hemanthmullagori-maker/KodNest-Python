#Selection Statements

#if statement
#Write a Python program to check whether a person is eligible to vote. If the age is 18 or above, print "Eligible to vote".
age = int(input("enter your age: "))
if age >= 18:
    print("Eligible to vote")
#if-else statement
#Write a Python program to check whether a person is eligible to vote or not. If the age is 18 or above, print "Eligible to vote", otherwise print "Not Eligible to vote".
age = int(input("enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
#if-elif-else ladder
#write a Python program to accept marks and print the grade using the following conditions: 90+ → A, 70+ → B, 50+ → C, 35+ → D, otherwise → Fail.
marks = int(input("enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")   
#Nested if statement
#Write a Python program to check whether you are free tonight. If you are free, check whether your friends are available. Print "Go out for party" if both are true; otherwise print the appropriate message.
temp = int(input("Enter the temperature: "))
if temp > 40:
    if temp > 50:
        print("It's very hot")
    else:
        print("It's hot")
else:
    if temp > 30:
        print("It's warm")
    else:
        print("It's pleasant")      
#match-case statement
#Write a Python program that accepts a number from 1 to 7 and uses match-case to print the corresponding day of the week.
day = int(input("Enter the day number: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")    
#match-case with multiple cases
#Write a Python program that accepts a month number and uses match-case to print the season: 3,4,5 → Summer, 6,7,8 → Rainy, 9,10,11,12 → Winter, and 1,2 → Autumn.
month = int(input("Enter the month number: "))
match month:
    case 3|4|5:
        print("Summer")
    case 6|7|8:
        print("Rainy")
    case 9|10|11|12:
        print("Winter")
    case 1|2:
        print("Autumn")
    case _:
        print("Invalid month")

#Looping Statements
#for loop with range
#Write a Python program to print numbers from 1 to 5 using a for loop.
for i in range(1, 6):
    print(i)
#for loop – first 5 numbers
#Write a Python program to print the first five numbers starting from 0 using a for loop.
for i in range(5):
    print(i)
#for loop with if condition
#Write a Python program to print all even numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    if i % 2 == 0:
        print(i)        
#while loop
#Write a Python program to print numbers from 0 to 4 using a while loop.
i = 0
while i < 5:
    print(i)
    i += 1
#Jumping Statements
#break statement
#Write a Python program to print numbers from 1 to 5, but stop the loop when the number reaches 4.
for i in range(1, 6):
    if i == 4:
        break
    print(i)
#continue statement
#Write a Python program to print numbers from 1 to 5, but skip the number 4 using continue.
for i in range(1, 6):
    if i == 4:
        continue
    print(i)
#pass statement
#Write a Python program using a for loop from 1 to 9 and use pass as a placeholder inside the loop.
for i in range(1, 10):
    pass
    print(i)
#pass in function
#Write a Python program to create a function called add() without implementing its logic. Use pass inside the function.
def add():
    pass
#return statement
#Write a Python function called square(n) that accepts a number and returns its square. Call the function with 3 and print the result.
def square(n):
    return n * n
print(square(3))
# looping statements
# for loop with range 
# write a python program to print number from 1 to 5 using a for 
for i in range (1,6)
    print(i)
    
