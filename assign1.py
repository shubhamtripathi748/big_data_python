#Why q1....do we call Python as a general purpose and high-level programming language

#we can write code or logic in high level english and that is understandable to developer
#and down the line compiler will covert that high to low level that is machine format

#Q2. Why is Python called a dynamically typed language?

#once we create any data structure in python it is having some type and type of data is calculated at the run time.

#Q3. List some pros and cons of Python programming language?

#it is dynamic typed language and very handy to write a logic and numpy and pandas api available to do
# machine learning and  support of big data things as well.

#Q4. In what all domains can we use Python?

# machine learning,data analytics,big data, design a UI

#Q5. What are variable and how can we declare them?

#variable is nothing but a memory location on the computer or we can say address location.

#Q6. How can we take an input from the user in Python?

#str=input("please enter some value : ")


#Q7. What is the default datatype of the value that has been taken as an input using input() function?

#string

#Q8. What is type casting?

#convertion of one data type to another that is type casting for e.g int to string or float to int etc..


#Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

#x,y,z=input("please enter three values ").split()


#Q10. What are keywords?

#reserve words are called keywords for e.g int float string..

#Q11. Can we use keywords as a variable? Support your answer with reason.
# no we can not use keyword as identifier and functions

#Q12. What is indentation? What's the use of indentaion in Python?
#paython follow some rules to write a code pascal indentation.

#Q13. How can we throw some output in Python?
# print("value of b is ",b)

#Q14. What are operators in Python?
#to perform some operation for e.g addition,* /,//,or,and,not,|,&


#Q15. What is difference between / and // operators?

#9/2 is 4.2 and 9//2 is 4 only means floading point will not be there in case of  //

#16

print('''iNeuroniNeuroniNeuroniNeuron''')

#17

number_even_odd =int(input("enter a number : "))
if number_even_odd % 2 == 0:
    print(f'number {number_even_odd} is even ')
else:
    print(f'number {number_even_odd} is odd ')

#Q18. What are boolean operator?

# True or False and and or and not will return True or False

#19

# 1,0,False,1

#Q20. What are conditional statements in Python?,21

#if else elif and those can we use to evaluation expression.

#22

age = int(input('enter the age of person '))

if age >= 18:
    print('I can vote')
else:
    print('I can not vote')


#23

numbers = [12, 75, 150, 180, 145, 525, 50]
sum_of_even_number = 0
for item in numbers:
    if item % 2 == 0:
        sum_of_even_number += item
print(sum_of_even_number)

#24

a, b, c = input("kindly enter 3 numbers ").split()

list_temp = (a, b, c)
max_num = a
for item in list_temp:
    if item > max_num:
        max_num = item

print(max_num)


#25
numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item % 5 == 0:
        if item > 150:
            continue
        if item > 500:
            break
        print(item)


#string = "Big Data iNeuron"
#op desired_output = "iNeuron"

str_28 = "Big Data iNeuron"
desired_output = ''
for item in str_28.split(" "):
    if item == 'iNeuron':
        desired_output = 'iNeuron'
print(desired_output)

#29 desired_output = "norueNi"
actual_str=''
desired_output_rev=''
for item in str_28.split(" "):
    if item == 'iNeuron':
        actual_str = 'iNeuron'

desired_output_rev = actual_str[-1:: -1]
print(desired_output_rev)


#Q30. Resverse the string given in the above question.
print(str_28[-1::-1])
# del str_28
# print('str_28 value is ', str_28)

print("iNeuron's Big Data Course")

#q37
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])

set_s={}
set_s.clear()


























































































