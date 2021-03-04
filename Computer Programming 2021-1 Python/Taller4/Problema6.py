def factorial(numero):
    total = 1
    for i in range(0, numero):
        total *= numero-i
    
    return total

print(factorial(4))