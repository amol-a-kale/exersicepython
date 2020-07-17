# Write a code that heps to add n number of inputs passed by user

def n_numberof_input(N):
    for i in range(1, N + 1):
        user_input = input('input passed by end used')
    return user_input


result = n_numberof_input(5)

print(result)


#using recursion

def n_no_input():
    user_input = input('input passed by end used')
    n_no_input()
n_no_input()
