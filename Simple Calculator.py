def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a/b
    

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter youre choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", sub(num1, num2))
elif choice == '3':
    print("Result:", mul(num1, num2))
elif choice == '4':
    print("Result:", div(num1, num2))
else:
    print("Invalid choice")