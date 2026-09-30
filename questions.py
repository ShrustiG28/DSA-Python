# # Addition of two numbers
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# sum=num1+num2
# print("The sum of two numbers is:", sum)


# #print hello world
# print("Hello World")


#square root of a number 
# num=float(input("Enter a number: "))
# sqrt=(num)**(1/2)
# print("The square root of the number is:",sqrt)


# #Area of triangle 
# l=float(input("Enter the length: "))
# h=float(input("Enter the height: "))
# area=(1/2)*l*h
# print("The are of the triangle is:",area)


#swapping of two numbers
# a=float(input("Enter a number: "))
# b=float(input("Enter a number: "))
# temp=a
# a=b
# b=temp
# print("The value of a is :", a)
# print("The value of b is :", b)

#without using a third variable 
# x=10
# y=15
# x,y=y,x
# print("The value of x is: ", x)
# print("The value of y is: ", y)


#converting kilometers to miles 
# km=float(input("Enter the distance in km: "))
# miles=km*0.621371
# print("The distance in miles is: ", miles)


#check whether a number is positive or negative
# num=float(input("Enter a number: "))
# if num==0:
#     print("The number is zero")
# elif num>0:
#     print("The number is positive")
# else:
#     print("The number is negative")


#check if a number is even or odd
# num=float(input("Enter a number: "))
# if num%2==0 :
#     print("The number is even")
# else:
#     print("The number is odd")


#check if the given year is leap year 
# year=int(input("Enter a year: "))
# if ((year%400==0) and (year%100==0)):
#     print("The year is leap year")
# elif ((year%4==0) and (year%100!=0)):
#     print("The year is a leap year")
# else:
#     print("The year is not a leap year")


#find the largest of 3 numbers 
# num1=float(input("Enter a number 1: "))
# num2=float(input("Enter a number 2: "))
# num3=float(input("Enter a number 3: "))
# if (num1>num2 and num1>num3):
#     print("Number 1 is the largest number")
# elif (num2>num1 and num2>num3):
#     print("Number 2 is the largest number")
# else:
#     print("Number 3 is the largest number")


#check if a given number is prime or not
# num=int(input("Enter a number: "))
# if num==1:
#     print("The number is not a prime number ")
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("The given number is not a prime number ")
#             break
#     else:
#         print("The number is a prime number")


# print(str(100))
# print(str(3.14))
# print(str(True))
# print(str(False))
# print(str(5+2j))
# print(str('A'))


# generate a random number from a range 
# import random
# num=random.randint(1,100)
# print(num)


# # print all the prime numbers from a range 
# lower=int(input("Enter the starting point: "))
# upper=int(input("Enter the ending point: "))
# for num in range(lower, upper+1):
#     if num>1:
#         for i in range (2,int(num**0.5)+1):
#             if num%i==0:
#                 break
#         else:
#             print(num)



# convert celsius to F
# C=24
# F=(C*9/5)+32
# print(F)



# factorial of a number 
# num=int(input("Enter a number: "))
# fact=1
# if num<0:
#     print("Factorial doesn't exist")
# elif num==0:
#     print("The factorial is 1")
# if num>0:
#     for i in range(1, num+1):
#         fact=fact*i
#     print(fact)


# def fact(num):
#     if num==0:
#         return 1
#     else:
#         return num*fact(num-1)
# print(fact(5))



#print a multiplication table 
# num=int(input("Enter a number: "))
# for i in range(1,11):
#     print(num, "x", i, "=",num*i)


# print fibonacci sequence
# num=int(input("Enter a number: "))
# a=0
# b=1
# if num==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(1,num+1):
#         c=a+b
#         a=b
#         b=c
#         print(c)



# armstrong number 
# num=int(input("Enter a number: "))
# temp=num
# sum=0
# while(temp>0):
#     digit=temp%10
#     cube=digit**3
#     sum=sum+cube
#     temp=temp//10
# if sum==num:
#     print("The number is an armstrong number")
# else:
#     print("Number is not an armstrong number ")


#print armstrong numbers from the given interval
# lower=int(input("Enter the starting point: "))
# upper=int(input("Enter the ending point: "))
# for num in range(lower,upper+1):
#     sum=0
#     order=len(str(num))
#     temp=num
#     while(temp>0):
#         digit=temp%10
#         power=digit**order
#         sum=sum+power
#         temp=temp//10
#     if(num==sum):
#         print(num)


#print the sum of n natural numbers 
# n=int(input("Enter the value of n: "))
# sum=0
# while(n>=0):
#     sum+=n
#     n-=1
# print(sum)


# sum of n numbers using recurssion
# def sum(n):
#     if n==1:
#         return 1
#     return n*(n+1)//2
# print(sum(5))



#print all elements 
# n=int(input("Enter n: "))
# arr=[]
# for i in range(n):
#     elements=int(input(f"Enter elements {i+1}: "))
#     arr.append(elements)
# print(arr)


# arr=list(map(int, input().split()))
# print(arr)


#Sum of elements 
# arr=list(map(int, input().split()))
# sum=0
# for i in range(0,len(arr)):
#     sum+=arr[i]
# print(sum)



#Average of numbers 
# arr=list(map(int, input().split()))
# sum=0
# for num in arr:
#     sum+=num
# avg=(sum)/(len(arr))
# print(avg)



# arr=list(map(int,input().split()))
# max=arr[0]
# for i in range(len(arr)):
#     if max<arr[i]:
#         max=arr[i]
# print(max)


# arr=list(map(int,input().split()))
# max=arr[0]
# for num in arr:
#     if max<num:
#         max=num
# print(max)


# minimum of arr
# arr=list(map(int,input().split()))
# min=arr[0]
# for num in arr:
#     if min>num:
#         min=num
# print(min)


#print both minimum and maximum fri=om the string 
# arr=list(map(int,input().split()))
# maximum=arr[0]
# minimum=arr[0]
# for num in arr:
#     if maximum<num:
#         maximum=num
#     if minimum>num:
#         minimum=num
# print(maximum)
# print(minimum)



#count the number of evens 
# arr=list(map(int,input().split()))
# count=0
# for num in arr:
#     if num%2==0:
#         count+=1
# print(count)


#count the number of odds
# arr=list(map(int,input().split()))
# count=0
# for num in arr:
#     if num%2!=0:
#         count+=1
# print(count)



#count positive numbers in arr
# arr=list(map(int,input().split()))
# count=0
# for num in arr:
#     if num>0:
#         count+=1
# print(count)


# arr=list(map(int,input().split()))
# e_count=0
# o_count=0
# pos_count=0
# neg_count=0
# zero_count=0
# for num in arr:
#     if num%2==0:
#         e_count+=1
#     if num%2!=0:
#         o_count+=1   
#     if num>0:
#         pos_count+=1
#     if num<0:
#         neg_count+=1
#     if num==0:
#         zero_count+=1
# print(e_count)
# print(o_count) 
# print(pos_count)
# print(neg_count)
# print(zero_count)



# arr=list(map(int,input().split()))
# neg_count=0
# for num in arr:
#     if num<0:
#         neg_count+=1
# print(neg_count)

# arr=list(map(int,input().split()))
# count=0
# for num in arr:
#     if num==0:
#         count+=1
# print(count)



# find the number in the arr
# arr=list(map(int,input().split()))
# target=int(input())
# for num in arr:
#     if num==target:
#         print("Found")
#         break
# else:
#     print("Not Found")



#find the index of the target
# arr=list(map(int,input().split()))
# target=int(input())
# for i in range(len(arr)):
#     if arr[i]==target:
#         print(i)
#         break
# else:
#     print(-1)



#print the number of times the number appeared in the array 
# arr=list(map(int,input().split()))
# target=int(input())
# count=0
# for num in arr:
#     if num==target:
#         count+=1
# print(count)



# #find the first occurrence of the target
# arr=list(map(int,input().split()))
# target=int(input())
# for i in range(len(arr)-1,arr[0]):
#     if arr[i]==target:
#         print(i)
#         break
# else:
#     print(-1)



#reverse an array (method 1)
# arr=list(map(int,input().split()))
# reverse=[]
# for i in range(len(arr)-1,-1,-1):
#     reverse.append(arr[i])
# print(reverse)

# #method(2)
# arr=list(map(int,input().split()))
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i], end=" ")

#method(3)
# arr=list(map(int,input().split()))
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)



# check array palindrome
#method 1
# arr=list(map(int,input().split()))
# rev=[]
# for i in range(len(arr)-1,-1,-1):
#     rev.append(arr[i])
# print(rev)
# if arr==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#check for palindrome
# arr=list(map(int,input().split()))
# left=arr[0]
# right=len(arr)-1
# while left<right:
#     if arr[left]==arr[right]:
#         print("Palindrome")
#         break
#     else:
#         print("Not Palindrome")



# arr=list(map(int,input().split()))
# largest=float('-inf')
# second=float('-inf')
# for current in arr:
#     if current>largest:
#         second=largest
#         largest=current
#     elif current>second and current!=largest:
#         second=current
# print(second)



# arr = list(map(int, input().split()))
# largest = float('-inf')
# second = float('-inf')
# for current in arr:
#     if current > largest:
#         second = largest
#         largest = current
#     elif current > second and current != largest:
#         second = current
# print(f"Current={current}, Largest={largest}, Second={second}")
# print("Answer =", second)


#check if array is sorted 
# arr=list(map(int, input().split()))
# for i in range(len(arr)-1):
#     if(arr[i]>arr[i+1]):
#         print("Array is not sorted")
#         break
# else:
#     print("Array is sorted")


# move zeros
# arr=list(map(int, input().split()))
# for _ in range(len(arr)-1):
#     for i in range(len(arr)-1):
#         if (arr[i]==0):
#             arr[i],arr[i+1]=arr[i+1],arr[i]
# print(arr)



#find duplicate elements
# arr=list(map(int, input().split()))
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i]==arr[j]:
#             print(arr[j], end=" ")


#find the sum of the duplicates
# arr=list(map(int, input().split()))
# total=0
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i]==arr[j]:
#             total+=arr[j]
# print(total)



# find the most frequent element
# arr=list(map(int, input().split()))
# max_count=0
# most_frequent=0
# for i in range(len(arr)):
#     count=0
#     for j in range(len(arr)):
#         if arr[i]==arr[j]:
#             count+=1
#     if count>max_count:
#         max_count=count
#         most_frequent=arr[i]
# print(most_frequent)



# find the first repeating element
# arr=list(map(int, input().split()))
# found=False
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i]==arr[j]:
#             print(arr[i])
#             found=True
#             break
#     if found:
#         break
        


#find the missing number in an array
# arr=list(map(int, input().split()))
# total=0
# n=len(arr)+1
# actual_total=n*(n+1)//2
# for num in arr:
#     total+=num
# missing_value=actual_total-total
# print(missing_value)



#find the second largest element 
# arr=list(map(int, input().split()))
# largest=float("-inf")
# s_largest=float("-inf")
# n=len(arr)
# for i in range(0, n):
#     largest=max(largest, arr[i])
# for i in range(0,n):
#     if arr[i]>s_largest and arr[i]!=largest:
#         s_largest=arr[i]
# print(s_largest)

# for i in range(0, len(arr)):
#     if arr[i]>largest:
#         s_largest=largest
#         largest=arr[i]
#     elif arr[i]>s_largest and arr[i]!=largest:
#         s_largest=arr[i]
# print(s_largest)



#find the smallest element
# arr=list(map(int,input().split()))
# smallest=arr[0]
# for i in range(1, len(arr)):
#     if arr[i]<smallest:
#         smallest=arr[i]
# print(smallest)


#find the second smallest element
# arr=list(map(int, input().split()))
# smallest=float("inf")
# s_smallest=float("inf")
# for i in range(0, len(arr)):
#     if arr[i]<smallest:
#         s_smallest=smallest
#         smallest=arr[i]
#     elif arr[i]<s_smallest and arr[i]!=smallest:
#         s_smallest=arr[i]
# print(s_smallest)



#print only the unique numbers
# arr=list(map(int, input().split()))
# unique=[]
# for num in arr:
#     if num not in unique:
#         unique.append(num)
# print(unique)


#find the intersection of 2 arrays
# arr1=list(map(int, input().split()))
# arr2=list(map(int, input().split()))
# intersection=[]
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if arr1[i]==arr2[j]:
#             if arr2[j] not in intersection:
#                 intersection.append(arr2[j])
# print(intersection)



#find the union of the 2 arrays
# arr1=list(map(int, input().split()))
# arr2=list(map(int, input().split()))
# union=[]
# for num in arr1:
#     if num not in union:
#         union.append(num)
# for num in arr2:
#     if num not in union:
#         union.append(num)
# print(union)


#find the difference between 2 arrays
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# difference = []
# for num in arr1:
#     if num not in arr2:
#         difference.append(num)
# print(difference)


#find the count of common elements
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# unique=[]
# count=0
# for num in arr1:
#     if num in arr2:
#         if num not in unique:
#             unique.append(num)
#             count+=1
# print(unique)
# print(count)



# find the frequency of each element
# arr=list(map(int, input().split()))
# unique=[]
# for num in arr:
#     if num not in unique:
#         unique.append(num)
# for num in unique:
#     count=0
#     for x in arr:
#         if x==num:
#             count+=1
#     print(count)



#find the most frequent element
# arr=list(map(int, input().split()))
# max_count=0
# most_frequent=0
# unique=[]
# for num in arr:
#     if num not in unique:
#         unique.append(num)
# for num in unique:
#     count=0
#     for x in arr:
#         if x==num:
#             count+=1
#     if count>max_count:
#         max_count=count
#         most_frequent=num
# print(max_count)
# print(most_frequent)



#Find the First Non-Repeating Element
# arr=list(map(int, input().split()))
# unique=[]
# for num in arr:
#     if num not in unique:
#         unique.append(num)
# for num in unique:
#     count=0
#     for x in arr:
#         if x==num:
#             count+=1
#     if count==1:
#         break
# print(num)



#find the last non repeating element
# arr=list(map(int, input().split()))
# last_non_repeating=0
# unique=[]
# for num in arr:
#     if num not in unique:
#         unique.append(num)
# for num in unique:
#     count=0
#     for x in arr:
#         if x==num:
#             count+=1
#     if count==1:
#         last_non_repeating=num
# print(last_non_repeating)


#find the first repeating element 
# arr=list(map(int, input().split()))
# unique=[]
# for num in arr:
#     if num not in unique:
#         unique.append(num)
# for num in unique:
#     count=0
#     for x in arr:
#         if x==num:
#             count+=1
#     if count>1:
#         break
# print(num)



#Print the element with the second-highest frequency, choosing the first one encountered
# arr=list(map(int, input().split()))
# unique=[]
# max_count = 0
# second_max = 0
# second_most_frequent=0
# most_frequent=0
# for num in arr:
#     if num not in unique:
#         unique.append(num)
# for num in unique:
#     count=0
#     for x in arr:
#         if x==num:
#             count+=1
#     if count > max_count:
#         second_max = max_count
#         second_most_frequent = most_frequent

#         max_count = count
#         most_frequent = num
#     elif count > second_max and count != max_count:
#         second_max = count
#         second_most_frequent = num
# print(second_most_frequent)



