import math
import os
# definition class for our simple calculator
class Calc:
    def __init__(self, a , b):
        self.a = a
        self.b = b

    
    def add  (self):
       
        return f"the sum of the numbers is : {self.a + self.b}"
    
    def minus (self):
       
        return f"the difference of the numbers is : {self.b - self.a}"
    
    def multiply (self):
        
        return f" the multiplication of the numbers is : {self.a * self.b}"
    
    def division  (self):
        
        try:
            return f"the division of the numbers is : {self.b / self.a}"
        
        except ZeroDivisionError as e:
            return f"Error!  {e}"


    def power (self):
        
        return f"the power of the numbers is : {math.pow(self.a , self.b)}"
    
    def sqrt (self):
        
        return f"the squirt of the first numbers is : {math.sqrt(self.a)} and the squirt of the second numbers is : {math.sqrt(self.b)}"
    
    
    def __str__(self):
        return f"a = {self.a} b= {self.b}"



print("welcome to the simple calculator")
#checking if the user input is valid or not
while True:
    print("===============================")
    print("the available operations are :")
    print("-------------------------------")
    print("1. Add ")
    print("2. Minus")
    print("3. Multiply")
    print("4. Division ")
    print("5. Power")
    print("6. Sqrt")
    print("7. Exit")
    print("0. Clear screen (Only for command Line)")
    print("===============================")

    User_input = input("Enter the operation you want to perform : ")

    if User_input == "7":
        print("thanks for using the calculator, bye bye!")
        break
    elif User_input == "0":
        os.system('cls')
        continue
#error handling if the user input is not a number
    try:
        a = float(input("Enter the first number : "))
        b = float(input("Enter the second number : "))
        print("\n")
    except ValueError:
        print("Wrong input , please enter a valid input \n")
        continue    
    
    result = Calc(a,b)
#checking the user input and performing the operation
    if User_input == "1":
        
        print(result.add(),"\n")

    elif User_input == "2":
        print(result.minus(),"\n")

    elif User_input == "3":
        print(result.multiply(),"\n")

    elif User_input == "4":
        print(result.division(),"\n")

    elif User_input == "5":
        print(result.power(),"\n")

    elif User_input == "6":
        print(result.sqrt(),"\n")

  
