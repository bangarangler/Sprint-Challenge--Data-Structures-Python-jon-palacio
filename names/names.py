import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1: # runtime: 5.228913....
    # for name_2 in names_2:
        # if name_1 == name_2:
            # duplicates.append(name_1)

names = names_1 + names_2
'''
This way we don't repeat names like in the original
O(n)
'''
unique = set()
for name in names: # runtime: 0.00717687...
    if name in unique:
        duplicates.append(name)
    else:
        unique.add(name)

'''
This can handle repeated names if there are any.
none in this case so O(n*log(n))
'''

# names.sort()
# for i in range(len(names) - 1): # runtime: 0.01009607...
    # if names[i] == names[i + 1]:
        # duplicates.append(names[i])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

