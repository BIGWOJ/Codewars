def factorial_division(n, d):
    output = 1
    for i in range(d+1, n+1):
        output *= i
    return output