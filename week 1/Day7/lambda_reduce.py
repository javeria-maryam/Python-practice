# Find product of all numbers

from functools import reduce

nums = [2,4,5,6]

product = reduce(lambda x,y: x*y,nums)

print(product)