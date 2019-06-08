#ques 1 - Reverse String
#sample input                               Sample output
# Mohit Mathur                              ruhtam tihom

def reverse_string():
    name= input('Enter name - ')
    string_list = list(name)
    reverse_string=''
    length = 0

    for i in string_list:
        length = length + 1

    for i in string_list:
        reverse_string= reverse_string+ string_list[length-1]
        length = length -1

    print(reverse_string)

reverse_string()

