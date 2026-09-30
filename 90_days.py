# arr=list(map(int, input().split()))
# right=0
# left=len(arr)-1
# while right<left:
#     if arr[right]!=arr[left]:
#         print("not palindrome")
#         break
#     right+=1
#     left-=1
# else:
#     print("Palindrome")


#problem 977
# arr = list(map(int, input().split()))
# i = 0
# j = len(arr) - 1
# result = [0] * len(arr)
# k = len(arr) - 1
# while i <= j:
#     if abs(arr[i]) > abs(arr[j]):
#         result[k] = arr[i] ** 2
#         i += 1
#     else:
#         result[k] = arr[j] ** 2
#         j -= 1
#     k -= 1
# print(result)



# def isPalindrome(i,j):
#     while i<j:
#         if arr[i]!=arr[j]:
#             return False
#         i+=1
#         j-=1
#     return True
# arr = input().strip()
# i = 0
# j = len(arr) - 1
# while i < j:
#     if arr[i] == arr[j]:
#         i += 1
#         j -= 1
#     else:
#         print(isPalindrome(i+1,j) or isPalindrome(i,j-1))
#         break
# else:
#     print(True)



# time complexity:
# rate of increase of time taken with respect to the input size 
# calculate worst case, avoid lower bound, avoid constant values


# num=5438
# n=num
# count=0
# while n>0:
#     count+=1
#     n=n//10
# print(count)



# from math import *
# def countDigits(num):
#     return int(log10(num)+1)
# print(countDigits(5438))


# arr=list(map(int,input().split()))
# rev=[]
# for num in range(len(arr)-1,-1,-1):
#     rev.append(arr[num])
# print(rev)
# if arr==rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# n=1234
# num=n
# result=0
# while num>0:
#     ld=num%10
#     result=(result*10)+ld
#     num=num//10
# print(result)



# n=int(input("Enter a number: "))
# num=n
# total=0
# nod=len(str(n))
# while num>0:
#     ld=num%10
#     total=total+(ld**(nod))
#     num=num//10
# print(total)
# if total==n:
#     print("The number is an armstrong number ")
# else:
#     print("The number is not an armstrong number ")


#print all the factors of a number
# n=int(input("Enter a number: "))
# result=[]
# for i in range(1, n+1):
#     if n%i==0:
#         result.append(i)
# print(result)

# n=int(input("Enter a number: "))
# result=[]
# for i in range(1, (n//2)+1):
#     if n%i==0:
#         result.append(i)
# result.append(n)
# print(result)


# from math import sqrt
# n=int(input("Enter a number: "))
# result=[]
# for i in range(1,int(sqrt(n))+1):     #Tc-  O(sqrt(n))
#     if n%i==0:
#         result.append(i)
#         if n//i!=i:
#             result.append(n//i)
# result.sort()                         # Tc- O(N log N)
# print(result)                         #TC=  O(sqrt(n))+O(N log N)        SC= O(K), K is number of factors



# nums = [5, 6, 7, 7, 1, 9, 11, 1, 1, 5, 1, 7]
# hash_map = {}
# n = len(nums)
# for i in range(0, n):
#     hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
# print(hash_map)


#extracting the frequencies of the occurance of the numbers in m using hasing
# n=[5,3,4,6,7,7,5,1,2,3,10,4]
# m=[10,111,64,2,7,45,5,7]
# for num in m:
#     count=0
#     for x in n:
#         if x==num:
#             count+=1
#     print(count)

# giving manual input 
# n = [5, 3, 4, 6, 7, 7, 5, 1, 2, 3, 10, 4]
# num = int(input())
# count = 0
# for x in n:
#     if x == num:
#         count += 1
# print(count)


# using hash function
# n=[5,3,4,6,7,7,5,1,2,3,10,4]
# m=[10,111,64,2,7,45,5,7]
# hash_list=[0]*11
# for num in n:
#     hash_list[num]+=1
# for num in m:
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])

# using dictionary
# n = [5, 3, 4, 6, 7, 7, 5, 1, 2, 3, 10, 4]
# m = [10, 111, 64, 2, 7, 45, 5, 7]
# hash_map={}
# for num in n:
#     hash_map[num]=hash_map.get(num,0)+1
# for num in m:
#     print(hash_map.get(num,0))


# def func(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i,i+1,n)
# func(0,1,4)


# def func(n):
#     if n==1:
#         return 1
#     return n+func(n-1)
# print(func(4))



# def func(n):
#     if n==1:
#         return 1
#     return n*func(n-1)
# print(func(5))


# n=int(input())
# factorial=1
# if n==1 or n==0:
#     print("Factorial: 1")
# for i in range(1,n+1):
#     factorial=factorial*i
# print(factorial)


# reversing an array
# arr=list(map(int, input().split()))
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)


# arr=list(map(int, input().split()))
# left=2
# right=6
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)


# arr=list(map(int, input().split()))
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i], end=" ")


# def func(arr, left, right):
#     if left>=right:
#         return
#     arr[left],arr[right]=arr[right],arr[left]
#     func(arr, left+1, right-1)
# arr = [1, 2, 3, 4, 5, 6]
# func(arr, 0, 5)
# print(arr)


