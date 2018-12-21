# base-lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#initialize result list 
result = []

# iterate over list a to find all elements of a in b 
# only insert to result list if elem is not already in the list
for elem in a: 
    if elem in b:
        if elem not in result:
            result.append(elem)

print result