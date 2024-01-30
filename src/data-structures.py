'''
    LISTS
'''

'''
    lists are mutable
    lists are ordered (0-indexed) and can contain duplicates
'''

nums = [1, 2, 3, 4, 5]

print(nums[:2]) # non-destructive

nums.append(6) # destructive

nums[5] = "six"

print(nums.pop(2)) # destructive

nums2 = [1, 2, 3, 4, 5, 6]

squares = []

for num in nums2:
    num_squared = num ** 2
    squares.append(num_squared)

# list comprehension
squares2 = [num ** 2 for num in nums2]

even_cubes = []

for num in nums2:
    if num % 2 == 0:
        even_cubes.append(num * num * num)

# list comprehension
even_cubes2 = [num * num * num for num in nums2 if num % 2 == 0]

print(even_cubes2)

'''
    DICTIONARIES
'''

'''
    dictionaries are mutable
    dictionaries contain key:value pair mapping and cannot contain duplicate keys
'''

ages = {"Eleanor" : 25, "Tim" : 32, "Jay": 29, "Andrew" : 23, "Ethan" : 31, "Isaiah" : 33, "Dave" : 37, "Kylie" : 28, "Kevin" : 29}

ages["Tyler"] = 30 # adds new key:value pair

ages["Dave"] = 15 # changes existent value

for key in ages:
    print(ages[key])

'''
    SETS
'''

'''
    sets are mutable
    sets are unordered and do not contain duplicates
'''

plants = set()

buildings = {"Empire State Building", "Chrysler Building", "Washington Monument"}

print(buildings)

plants.add("tree")
plants.add("flower")
plants.add("grass")
plants.add("flower")
plants.add("dandelion")

print(plants)

print(len(plants)) # gets number of items

'''
    TUPLES
'''

'''
    tuples are immutable
    tuples are ordered (0-indexed) and have a set length
'''

coordinate = (20, 30)
color = (3, 200, 0)

print(color)