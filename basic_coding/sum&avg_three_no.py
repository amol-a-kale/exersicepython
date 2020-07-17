# def sum_three_no(first_no, second_no, third_no):
#     sum1 = first_no + second_no + third_no
#     print('the addition of {}, {} and {} is {}'.format(first_no, second_no, third_no, sum1))
#     average = sum1 / 3
#     print('average of three no is ' + str(average))
#
#
# sum_three_no(10, 20, 30)

# Write a code that helps to find the sum and average of any 3 numbers by accepting input at runtime


def average_no():
    # n1 =int(input('enter first no is :'))
    # n2 = int(input('enter second no is :'))
    # n3 = int(input('enter third no is :'))
    n1, n2, n3 = (input('enter multiple number are: ').split())

    sum1 = int(n1) + int(n2) + int(n3)
    print('the addition of {}, {} and {} is {}'.format(n1, n2, n3, sum1))
    average = sum1 / 3
    print('average of three no is ' + str(average))


average_no()
