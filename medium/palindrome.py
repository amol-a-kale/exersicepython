# 7. Write a code that helps to find whether the string is palindrome or not

def check_palidrome():
    string =input('enter the string for check palindrome: ')
    string1 = string[:: -1]
    print(string1)
    if string == string1:
        print("the {} is palindrome".format(string))
    else:
        print("the {} is not palindrome".format(string))

check_palidrome()

