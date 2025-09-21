# Write a program that asks user for 5 numbers, stores them in a list, and prints average.

mylist = list(map(int,input("Enter 5 numbers: ").split()))

average = sum(mylist)/len(mylist)

print("Average is:",average)


# Create a program where you store friends' names in a list and allow user to search for a name.

friends = ["Ali","Eman","Fatima","Umair"]

name = input("Enter a name: ")

if name.lower() in [friend.lower() for friend in friends]:

    print(name,"is in your friend list")
else:
     print(name,"is not in your friend list")



# Convert a list into a tuple.

mylist = [2,4,6,7]

mylist = tuple(mylist)

print("List is now a tuple",type(mylist))