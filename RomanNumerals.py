numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

# def convert_roman(input_number):
#     range_flag = None
#     for symbol, integer in numerals.items():
#         if integer == input_number: return symbol
#         if input_number > integer:
#             range_flag = symbol
#
#     remaining = input_number - numerals[range_flag]
#     return range_flag + convert_roman(remaining)

# for k,v in numerals.items():
#     print(k,v)


def convert_roman(input_number):
    range_flag = [None]
    for symbol, integer in numerals.items():
        if integer == input_number:
            return symbol
        if input_number > integer:
            range_flag = symbol

    remaining = input_number - numerals[range_flag]
    print (f"input number {input_number} - numerals[range_flag] {numerals[range_flag]} = {remaining}")
    return range_flag + convert_roman(remaining)


print(convert_roman(17)) # I
# print(convert_roman(17)) # XVII
# print(convert_roman(1111)) # MCXI



print("-----------------")

# # function calling
# def dictionairy():
#
# # Declaring the hash function
#     key_value ={}
#
#     # Initialize value
#     key_value[2] = 56
#     key_value[1] = 2
#     key_value[5] = 12
#     key_value[4] = 24
#     key_value[6] = 18
#     key_value[3] = 323
#
#     print ("Task 2:-\nKeys and Values sorted in",
#            "alphabetical order by the key ")
#
#     # sorted(key_value) returns an iterator over the
#     # Dictionary’s value sorted in keys.
#     for i in sorted(key_value) :
#         print ((i, key_value[i]), end =" ")
#
# def main():
#     # function calling
#     dictionairy()
#
# # main function calling
# if __name__=="__main__":
#     main()
#
#
# print("-----------------")
#
# # Function calling
# def dictionairy():
#
#     # Declaring hash function
#     key_value ={}
#
#     # Initializing the value
#     key_value[2] = 56
#     key_value[1] = 2
#     key_value[5] = 12
#     key_value[4] = 24
#     key_value[6] = 18
#     key_value[3] = 323
#
#
#     print ("Task 3:-\nKeys and Values sorted",
#            "in alphabetical order by the value")
#
#     # Note that it will sort in lexicographical order
#     # For mathematical way, change it to float
#     print(sorted(key_value.items(), key = lambda kv: (kv[1], kv[0])))
#
# def main():
#     # function calling
#     dictionairy()
#
# # main function calling
# if __name__=="__main__":
#     main()
