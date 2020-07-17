# Write a code to find the factorial of a number


def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    print('the factotrial of {} is : {}'.format(n, result))

factorial(10)
factorial(6)

