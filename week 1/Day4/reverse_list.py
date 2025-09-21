#Reverse a list without using .reverse()function

mylist = [23, 45, 54 ,53, 66]

reversed_list = [] 


for i in range(len(mylist)-1,-1,-1):
    reversed_list.append(mylist[i])

print("Reversed list:",reversed_list)
