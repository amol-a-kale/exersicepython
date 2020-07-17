# Design a code that helps to display number 1 to N in reverse order

# n=20
# no=[
# no_reverse_list=[]
# for i in range(1, 21):
#     # print(i)
#     no.append(i)
# no.reverse()
# # print(no)
# for i in no:
#     print(i)

def find_reverese_no(N):
    for i in range(1, N + 1):
        # print(i)
        print(N + 1 - i)


# find_reverese_no(5)

def printrevesre_order(N):
    for i in range (N,0,-1):
        print(i)
printrevesre_order(5)

def reverse_order(N):
    if N<=0:
        print(N)
reverse_order(5)
