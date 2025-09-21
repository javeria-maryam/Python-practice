#Create a list of 5 numbers, print first and last element.
# Add a new number, remove one number, print updated list



list1 = list(map(int,input("Enter 5 numbers: ").split()))        #Asking user for the number of list

print('First element is',list1[0],"and last element is",list1[-1])

num1 = int(input("Enter a number to add: "))                    #Asking user to add a number

list1.append(num1)

num2 = int(input("Enter the number to remove: "))               #Asking user to remove a number.

if num2 in list1:
 list1.remove(num2)
else:
 print("Number does not exist")


print("Updated list is", list1)





