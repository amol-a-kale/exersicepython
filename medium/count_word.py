# Write a program to count the number of words and letters in a sentence

def count_word():
    string_input = input('enter the string :')
    count1 = 0
    for i in string_input:
        #  we use if loop for calculate  no of space
        if i == " ":
            count1 += 1
        # word is greater than one by space for that we write following syntax
    no_word = count1 + 1

    print(no_word)


# count_word()


# it is used to find number of characteristic

def count_char():
    string_input = input('enter the string :')
    count1 = 0
    for i in string_input:
        #  we use if loop for calculate  no of space
        if i == " ":
            count1 += 1
        # word is greater than one by space for that we write following syntax
    no_char =len(string_input)- count1

    print(no_char)


# count_char()

def print_vowol():
    string_input = input('enter the string :')
    string=string_input.lower()
    count1 = 0
    vowel_list=['a', 'i', 'e', 'o','u']
    for i in string:
        #  we use if loop for calculate  no of space
        if i in vowel_list:
            print(i)
            count1 += 1
        # word is greater than one by space for that we write following syntax

    print(count1)


# print_vowol()

 # print_ consonants

def print_cons():
    string_input = input('enter the string :')
    string=string_input.lower()
    count1 = 0
    vowel_list=['a', 'i', 'e', 'o','u',' ']
    for i in string:
        # we create list in list we add vowels and space and compare with actual string
        if i not in vowel_list:
            print(i)
            count1 += 1
        # word is greater than one by space for that we write following syntax

    print('the number of consonant is : ',count1)

# print_cons()



# find number of word by using splict function

#
# count=0
# string=' hi amol kale'
# split_string=string.split()
# for i in split_string:
#         print(i)
#         count=1+count
#
# print('the number of word :', count )



# count the number of charactertics
count=0
string=' hi amol kale'
for i in string:
    if i== " ":
        print(i)
        count=1+count

print('the number of word :', len(string)-count )
