# Design a code to check whether number is a prime number or not
def check_prime_no(N):
    if N > 1:
        for i in range(2, N):
            if N % i == 0:
                print(N, '  is not prime number')
                break
        else:
            print(N, ' is prime number')
    else:
        print(N, ' is not prime number')


check_prime_no(1)

# Design a code to print all the prime numbers between 1 to 100

x = 0  # counter


def find_primeno(N):
    global x
    for N in range(1, 101):
        if N > 1:

            for i in range(2, N):

                if N % i == 0:
                    # print(N, '  is not prime number')
                    break
            else:
                x += 1
                print(N)
    print( 'total number of odd number is ', x)



# find_primeno(100)


# Write a code to print sum of all the prime numbers between 1 to N

def sumof_primeno(N):
    sum = 0

    for N in range(1, N + 1):  # write this syntax n number must between upper and lower number
        if N > 1:  # this condition write for prove 1 is not prime number
            for i in range(2, N):  # this loop find the number is divisible or not
                if N % i == 0:
                    # print(N,'is not prime no')
                    break
            else:  # use else conditon ousider of if loop

                sum = sum + N

    print('the sum of prime number is', sum)

# sumof_primeno(100)
