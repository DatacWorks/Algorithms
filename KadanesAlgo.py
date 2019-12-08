"""
return maximum sum that can be obtained by summing up all
the numbers in a non-empty subarray of the input array
sample input: [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
output : 19 ([1, 3,-2,3,4,7,2,-9,6,3,1])
"""


# O(n) time | O(1) space - where n is the length of the array

def kadanesAlgo(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        num = array[i]
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar

array = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
print(kadanesAlgo(array))



