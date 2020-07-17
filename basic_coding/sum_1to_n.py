# Write a code that helps to display the sum of 1 to N numbers
def sumofn_no(N):
    sum = 0
    for i in range(1, N + 1):
        # print(i)
        sum = sum + int(i)
    print('sum of 1 to' + str(N) + ' number is ' + str(sum))


sumofn_no(20)


def sum_by_formula(N):
    a = 1
    sum = N / 2 * (a + N)
    print('sum of 1 to {} is {}'.format(N, sum))


sum_by_formula(20)
