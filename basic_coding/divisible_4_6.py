# Design a code to check whether number is divisible by 4 & 6
def check_no_divby4_6(number):
    if number%4==0 and number%6==0:
        print('{} number is divisible by 4 and 6'.format(number))
    else:
        print(str(number) + ' number  is not divisible by 4 and 6')
check_no_divby4_6(24)
check_no_divby4_6(20)



