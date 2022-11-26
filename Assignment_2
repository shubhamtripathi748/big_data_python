#Write a Python program to find the factorial of a given numbe

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number*factorial(number-1)
#print(factorial(5))

def simple_interest(p,r,t):
    si = (p*r*t) / 100
    return si
#print(simple_interest(1,2,3))

#Q79. Write a Python program to check if a number is prime or not.
from math import sqrt
def is_prime(n):
    if n <= 1:
        return False
    for m in range(2  ,int(sqrt(n)+1)):
        if n % m == 0:
            return False
    else:
        return True

#print(is_prime(5))

#Q80. Write a Python program to check Armstrong Number.
import math
def armstrong_number(number):
        armstrong_number = 0
        temp_number = number
        while temp_number > 0:
            mod = int(temp_number % 10)
            armstrong_number += (mod*mod*mod)
            temp_number = int(temp_number/10)
        if number == armstrong_number:
            print("the number is armstrong number " , number)
        else:
            print("the number is not armstrong number ", number)


#armstrong_number(153)


#armstrong_number(227)

#Q81. Write a Python program to find the n-th Fibonacci Number.

# 1,1,2,3,5,8
lst_fib = [0 , 1]
def fibonacci_series(number):
    for num in range(2,number):
        n1 = lst_fib[num-1]
        n2 = lst_fib[num-2]
        n3 = n1+n2
        lst_fib.append(n3)


#fibonacci_series(5)
#print(lst_fib)

#Q82. Write a Python program to interchange the first and last element in a list.

org_list=[0, 1, 1, 2, 3]
first=org_list[0]
last=org_list[-1]
org_list[0]=last
org_list[len(org_list)-1]=first
#print(org_list)

#Q84. Write a Python program to find N largest element from a list

def find_largest(list):
    largest=list[0]
    for num in list:
        if largest < num:
            largest = num
    return largest

#print(find_largest(org_list))


#Q85. Write a Python program to find cumulative sum of a list.

def sum_of_list_elements(list):
    sum_num = 0
    for num in list:
        sum_num += num
    return sum_num

#print(sum_of_list_elements(org_list))

#Q86. Write a Python program to check if a string is palindrome or not.

def check_palindrome(orignal_str):
    reversed_str = orignal_str[-1::-1]
    if orignal_str == reversed_str:
        print(f'{orignal_str} is palindrome ')
    else:
        print(f'{orignal_str} is not palindrome ')

#check_palindrome("ABBA")
#check_palindrome("ABBAB")

#Q87. Write a Python program to remove i'th element from a string.

def remove_element_in_string(actual_str , i):
    part1 = actual_str[:i]
    part2 = actual_str[i+1:]
    return part1+part2

print(remove_element_in_string("shu",2))
#sh shubham

#Q88. Write a Python program to check if a substring is present in a given string.
#str1 will be present in str2
def present_of_substring(str1,str2):
    if str1 in str2:
        return str2.index(str1)
    return -1


str1 = "sh"
str2 = "shubham"
op = present_of_substring(str1,str2)
#
# if op != -1:
#     print(f"{str1} is present in {str2}")
# else:
#     print(f"{str1} is not present in {str2}")

dict = {

    'A': [1, 3, 5, 4], 'B': [4, 6, 8, 10], 'C': [6, 12, 4, 8], 'D': [5, 7, 2]

}

list = []
for val in dict.values():
    list.extend(val)

#print(set(list))

input = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]


dictonary={}

for item in input:
    x,y = item[0],item[1]
    dictonary.setdefault((x,y))

#print(dictonary)

#Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.

list = [9, 5, 6]

list_new=[]
for item in list:
    tuplex=(item,item*item*item)
    list_new.append(tuplex)

#print(list_new)

def all_combination(tuple1,tuple2):
    list =[]
    for t1 in tuple1:
        for t2 in tuple2:
            list.append((t1,t2))
    return list

test_tuple1 = (7,2)
test_tuple2 = (7, 8)

#print(all_combination(test_tuple1,test_tuple2))

#Write a Python program to sort a list of tuples by second item.

input = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
#Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

lamda_second= lambda x :x[1]

print(sorted(input ,key=lamda_second))

#Q96. Write a python program to print below pattern.

for i in range(1,6):
    tem_str=''
    for j in range (1,i+1):
        tem_str += '*'
    print(tem_str)

print('---------------------------')
for i in range(1,6):
    tem_str=''
    for k in range(i,5):
        tem_str+=' '
    for j in range (1,i+1):
        tem_str += '*'
    print(tem_str)




