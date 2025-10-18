def Fibonacci(n):
    a,b =0,1
    for _ in range(n):
        print(a, end =' ')
        a,b = b,a+b
        
print("digite un numero entero positivo")
usuario = int(input())
Fibonacci(usuario)

"""Fizzbut"""

print()