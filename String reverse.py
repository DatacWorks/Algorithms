"""
time complexity O(n)
"""
# Python code to reverse a string
# using loop
def solution(s):
    str = ""
    for i in s:
        str = i + str
    # print(str)
    return str

s = "Geeksforgeeks"

print ("The original string  is : ",end="")
print (s)

print ("The reversed string(using loops) is : ",end="")
print (solution(s))



# Python code to reverse a string
# using recursion

def solution(s):
    if len(s) == 0:
        return s
    else:
        return solution(s[1:]) + s[0]

s = "Geeksforgeeks"

print ("The original string  is : ",end="")
print (s)

print ("The reversed string(using recursion) is : ",end="")
print (solution(s))

string = "".join(reversed(s))
print (string)


# Python code to reverse a string
# using extended slice syntax

# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string

def reverse2(x):    # big O(n)
    output_len = len(x)
    output = [None] * output_len
    output_indx = output_len -1
    for c in x:
        output[output_indx] = c
        output_indx -= 1
    return "".join(output)

s = "Mytest"

print ("The original string  is : ",end="")
print (s)

print ("The reversed string is : ",end="")
print (reverse2(s))