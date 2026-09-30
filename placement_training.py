# print("Hey this is Shrusti \nIm currently studying 4th year of engineering \nIm attending placement training right now")


# age="22"
# print(age)
# print(type(age))


# college_name="MVJ college of engineering"
# branch="Computer science"
# CGPA=9
# print(college_name, branch, CGPA)



# list=["Shrusti","Arun",28,True]
# print(list)
# print(type(list))
# list.append(3.14)
# print(list)


# name="Shrusti"
# nationality="Indian"
# age=21
# vote_casted=True
# marks=[98,84,97,88]
# profile= {
#     "working":"TCS",
#     "marriage_status": "Single",
#     "salary LPA": 15
# }
# print(name, nationality, age, vote_casted, marks, profile)


# marks=(90,97,97)   #tuple
# print(type(marks))
# age=[20,21,23]       #list
# print(type(age))
# boolean={True,False,False}    #set
# print(type(boolean))


# name=input("Enter your name: ")
# print("Welcome", name)


# num1=int(input("Enter number a: "))
# num2=int(input("Enter number b: "))
# print(num1+num2, num1-num2, num1*num2, num1/num2, num1%num2)


# name="shrusti"
# marks=92
# print(f" {name} scored {marks} marks ")


# profile= {
#     "working":"TCS",
#     "marriage_status": "Single",
#     "salary LPA": 15
# }
# for key,value in profile.items():
#     print(key,value)


# num=int(input("Enter a number: "))
# if num%2==False:
#     print("Even")
# else:
#     print("Odd")

# calculator
# area of circle
# c to f
# swap 
# avg of 3 num

# a=int(input("Enter the radius: "))
# radius=3.14*a**2
# print(radius)



# marks=int(input("Enter your marks: "))
# name= "Shrusti"
# if marks >= 90:
#     print(f"{name} has secured Grade A+")
# elif marks>=75:
#     print(f"{name} has secured Grade A")
# elif marks>=60:
#     print(f"{name} has secured Grade B")
# else:
#     print("Fail")


# square={
#     x:x*x
#     for x in range(10)
#     if x%2==0
# }
# print(square)


# multiples=[i for i in range(165,185)if i%3==0]
# print(multiples)
# print(len(multiples))


# count=0
# for i in range(0,31):
#     if i%3==0:
#         print(i)
#         count+=1
# print(count)


# for i in range(5):
#     print("*" * (i+1))


# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" " * (n-i) + "*" * (2*i-1))
# for i in range(n-1,0,-1):
#     print(" " * (n-i) + "*" * (2*i-1))


# for i in range(1,101):
#     print(i)


# for i in range(1,51):
#     if i%2==0:
#         print(i)


# for i in range(1,51):
#     if i%3==0:
#         print(i)



# num=28
# rev=0
# temp=num
# while temp>0:
#     digit=temp%10
#     rev=rev*10+digit
#     temp=temp//10
# print(rev)
# if(rev==num):
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")


# str="All is well"
# word=str.split(" ")
# print(word)

# t=""
# for words in word:
#     t1=words[::-1]
#     t=t+" "+(t1)
# print(t)



count=0
# fruits=["Apple","Mango"]
# fruits.append("Orange")
# print(fruits)
# print(fruits[2])
# print(fruits.reverse())
# print(fruits.count("Apple"))
# print(fruits.append("Banana"))
# print(fruits)
# # print(fruits.pop())
# print(fruits.insert(3,"Kiwi"))



# def greet(greeting, *names):
#     for name in names:
#         print(f"{greeting},{name}")
# greet("Hello", "Alice", "Bob", "Charlie")


# def config(**options):
#     for key,value in options.items():
#         print(f"{key}={value}")
# config(theme="dark",font=14,debug=True)


#comprehension


# def outer(x):
#     def inner(y):
#         return x+y 
#     return inner(5)
# print(outer(3))



# def multiples(n):
#     for i in range(1,11):
#         print(n*i)
# multiples(9)


# def make_multiplier(n):
#     def multiply(x):
#         return x*n
#     return multiply
# times3=make_multiplier(3)
# print(times3(4))
# print(times3(10))


# nums=[1,2,3,4,5,6]
# evens=list(filter(lambda x:x%2==0, nums))    # filter() keeps only items where the function returns true 
# print(evens)


# nums=[1,2,3,4,5,6]
# squares=list(map(lambda x:x**2, nums))         #map() applies the function to every item and collect the data
# print(squares)



# from functools import reduce
# nums=[1,2,3,4,5]
# product=reduce(lambda a,b: a*b, nums)             #reduce() rolls the list into a single value using binary function(aggregates into one value)
# print(product)



# sum of n numbers using recurssion
# def sum(n):
#     if n==1:
#         return 1
#     return n*(n+1)//2
# print(sum(5))


# nums=[2,3,4,5,6,7,8]
# squares=list(map(lambda x:x*x, nums))
# print(squares)


# print("abc123".isalnum())


# a="10"
# b=10
# print(repr(a))
# print(repr(b))


# import datetime
# now=datetime.datetime.now()
# print(str(now))
# print(repr(now))



