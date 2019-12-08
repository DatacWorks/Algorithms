"""
Find Missing Element in two arrays
[4, 12, 9, 5, 6] assume all unique.. hash table ? or sets in python ?
[4, 9, 12, 6]
should return ==> 5
"""

def set_solution(list1, list2):
    diff = set(list1).difference(list2)
    return diff

x = [4, 12, 9, 5, 6]
y = [4, 12, 9, 6]
print(set_solution(x, y))


# Linear time solution , but not constant space .. because we dont know how big the sum is going to be..
def solution (x, y):
    set1 = sum(x)
    set2 = sum(y)
    return abs(set2 - set1)

x = [4, 12, 9, 5, 6]
y = [4, 12, 9, 6]
print(solution(x, y))

def solution2(x,y):
    A = x + y
    n = len(A)
    result = 0
    for i in range(0, len(A)):
        result ^= A[i]  # ^ bitwise operator XOR (Swaps binary values a=0, b= 1.. a^= b => a=1 , b =0
        # print(f"results {result}")
    return result

x = [4, 12, 9, 5, 6]
y = [4, 12, 9, 6]
print(solution2(x, y))


def find_missing_xor(full_set, partial_set):
    xor_sum = 0
    for num in full_set:
        xor_sum ^= num
    for num in partial_set:
        xor_sum ^= num

    return xor_sum

x = [4, 12, 9, 5, 6]
y = [4, 12, 9, 6]

print(find_missing_xor(x, y))




