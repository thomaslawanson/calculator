# Function1: Increase Number by 1 (increment)
# Function2: Decrease Number by 1 (decrement)
# Function3: Add 2 numbers
# Function4: Subtract 2 numbers
# Function5: Multiply 2 numbers
# Function6: Divide 2 numbers


def increment(num):
    results = num+1
    print(results)


def decrement(num):
    results = num -1
    print(results)


def add_2(num1,num2):
    results = num1 + num2
    print(results)


def sub_two(num1,num2):
    results = num1-num2
    print(results)


def multiply_2(num1,num2):
    results = num1 * num2
    print(results)


def divide_2(num1,num2):
    results = num1 / num2
    print(results)

def modulus_2(num1,num2):
    results  = num1 % num2
    print(results)

print("what do you want to do?")
print("(1) +1")
print("(2)  -1")
print("(3)   +")
print("(4)  -")
print("(5)   *")
print("(6)   /")
print("(7)   %")
a =int(input("what are you doing today "))

if a == 1:
   user = int(input("what number "))
   increment(user)

elif a == 2:
    number = int(input("number please? "))
    decrement(number)

elif a == 3:
    n1 = int(input("enter number 1 "))
    n2 = int(input("enter number 2 "))

    add_2(n1,n2)

elif a == 4 :
    num1 = int(input("enter number 1 "))
    num2 = int(input("enter number 2 "))
    sub_two(num1,num2)
elif a == 5:
    num1 = int(input("number 1 "))
    num2 = int(input("number 2 "))
    multiply_2(num1,num2)
elif a == 6:
    num1 = int(input("number 1 "))
    num2 = int(input("number 2 "))
    divide_2(num1,num2)
elif a == 7:
    num1 =int(input("num 1 " ))
    num2 = int(input("num 2 " ))
    modulus_2(num1,num2)






