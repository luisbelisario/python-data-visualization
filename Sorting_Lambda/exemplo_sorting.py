import random

# Easily create a list of numbers
data = list(range(10))
print("range data:", data)

# Randomly shuffle those numbers
random.shuffle(data)
print("shuffled data:", data)

# Sort the list of numbers
data.sort()
print("sorted data with .sort():", data)

# Shuffle it again
random.shuffle(data)
print("shuffled data:", data)

# Use sorted to sort the list
newdata = sorted(data)
print("data after sorted():", data)
print("returned from sorted():", newdata)

# Convert to a tuple
datatup = tuple(data)
print("data tuple:", datatup)

# Sort the tuple of numbers
# datatup.sort() -> ERROR! Tupla não tem esse método!
# print("tuple after sort:", datatup) -> Tupla não podem ser mudadas

# Use sorted to sort the tuple
newdatatup = sorted(datatup)  # It works!
print("returned from sorted:", newdatatup)  # returns a list

# Create a dictionary of squares (dictionary comprehension)
datamap = {key: key ** 2 for key in datatup}
print("data dictionary:", datamap)

# Use sorted to sort the dictionary
sortmap = sorted(datamap)
print("returned from sorted:", sortmap)
