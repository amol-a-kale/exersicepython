# Design an application that helps to reverse the any string/text

# by using slicing concept
def reverse_by_slicing(s):
    return s[::-1]


result = reverse_by_slicing('hi my name is  amol patil')
print(result)


# by using for loop
def reverse_by_loop(s):
    my_new = ""
    for i in s:
        my_new = i + my_new
    return my_new


result = reverse_by_loop('hi everyone')
print(result)


# by using recursion
# recursion means call the function it self

def reverse_by_recursion(s):
    if len(s) == 0:
        return s

    else:
        return reverse_by_recursion(s[1:]) + s[0]


result = reverse_by_recursion('hi amol')
print(result)
