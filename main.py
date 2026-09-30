# import calculator
# print(calculator.add(30,10))
# print(calculator.sub(34,31))
# print(calculator.mul(3,9))
# print(calculator.div(5,2))


# from math import sqrt
# print(sqrt(25))


# import math as m
# print(m.pi)

# from college import students
# students.hello()


# class Employee:
#     def __init__(self,name,salary,dept):
#         self.name=name
#         self.salary=salary
#         self.dept=dept
#     def show(self):
#         print(self.name,self.salary,self.dept)


class BankAccount:
    def __init__(self,balance=0):
        self._balance=balance
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
    def withdraw(self,amount):
        if 0<amount<=self._balance:
            self._balance-=amount
        else:
            print("Invalid or insufficient funds")
    def check_balance(self):
        print("Balance: ",self._balance)
acc=BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()
