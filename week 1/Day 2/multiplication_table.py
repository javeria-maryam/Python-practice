# Ask user for a number.

# Print its multiplication table up to 10 using a for loop.

num = int(input('Enter the number you want multiplication table of: '))

for i in range(1,11):

    print(num, 'x', i, '=', num*i)


# Print  multiplication table up to 10 using a while loop.

num = int(input('Enter the number you want multiplication table of: '))

i=0

while i <10:
    i+=1

    print(num, 'x', i, '=', num*i)
