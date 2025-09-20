#Function that takes a number and checks if it’s prime.

def prime_num(num):

    if num<=1:
        return "is not a prime number"
    
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return "is not a prime number"
        
    return "is a prime number"


num = int(input("Enter a number: "))
print(num,prime_num(num))

