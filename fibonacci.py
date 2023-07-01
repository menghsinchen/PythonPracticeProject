def Fibonacci(n):
    if n < 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
print(Fibonacci(0))
print(Fibonacci(1))
print(Fibonacci(2))
print(Fibonacci(3))
print(Fibonacci(4))
print(Fibonacci(5))
print(Fibonacci(6))
print(Fibonacci(7))
print(Fibonacci(8))
print(Fibonacci(9))