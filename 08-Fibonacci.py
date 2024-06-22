#Fibonacci
def fibonacci(n):
    if n < 1:
        return n
    else:
        return fibonacci(n-1) + (n-2)
    
num = int(input("Please Enter a number :"))
result = fibonacci(num)
print("The Fibonacci sequence at index", num, "is:", result)
