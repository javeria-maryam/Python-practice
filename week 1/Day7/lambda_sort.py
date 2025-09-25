# Sort list of tuples by second element

pairs = [(3,1) , (5,4) , (2,3)]

pairs.sort(key=lambda x : x[1])

print("Sorted by second element:",pairs)