# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
import time
start = time.time()

import itertools
tuple_perms = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))

possible_nums = []
products = []
answer = 0

def convert(list):
    num = sum(digit * pow(10,i) for i, digit in enumerate(list[::-1]))
    return (num)

for permutation in tuple_perms:
    num = list(permutation)
    possible_nums.append(convert(num))

for num in possible_nums:
    for i in range(1, 10):
        for k in range(i + 1, 9):
            if int(str(num)[0:i]) * int(str(num)[i:k]) == int(str(num)[k:]):
                if int(str(num)[k:]) not in products: # This is hinted
                    products.append(int(str(num)[k:]))

for m in products:
    answer += m

print(answer)

stop = time.time()
print('Time: ', stop - start)