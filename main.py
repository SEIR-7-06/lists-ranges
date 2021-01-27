arr1 = []
numsList = [1, 2, 3]
colors = ['red', 'blue', 'yellow', 'purple']

# print(colors)

# List Length
# print(len(colors))


#------------------- Accessing Elements
# print(colors[3])

# Accessing Last Element
index = len(colors) - 1
# colors.length - 1 JavaScript
# print(colors[-3])


#------------------- Assigning Elements

# Reassignment
colors[0] = 'brown'


# Insert
colors.insert(0, 'magenta')
# print(colors)

# Extend
colors.extend(['green', 'orange'])


# Append
colors.append('polka-dots')
# print(colors)


#------------------- Deleting Elements

# Pop
last_item = colors.pop(-2)
# print(last_item)

# Remove
second_item = colors.remove('brown')
# print(second_item)
# print(colors)

# Clear
colors.clear()
# print(colors)


# ---------------------- ITERATION

foods = ['hamburger', 'taco', 'pizza']

# Iteration
for food in foods:
  pass
  # print(food)


# Iteration with Index
# for idx, food in enumerate(foods):
  # print(idx, food)



# ---------------------- DICTIONARY REVIEW

menu = {
  'hamburger': 4.99,
  'french_fries': 1.99,
  'taco': 2.99,
}

# Mut use bracket notation to access properties
hamburger = menu['hamburger']
# taco = menu['taco']
# pizza = menu['pizza']
# the get() method will return None instead of throwing an error
pizza = menu.get('pizza')

# print(hamburger)
# print(taco)
# print(pizza)

# Square nums (long hand)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for num in nums:
  squares.append(num * num)

# Square nums (short hand with comprehension)
# [expression for item in list]

squares_comp = [num * num for num in nums]

# print(squares_comp)


# Filtering (long hand)
even_nums = []

for num in nums:
  if num % 2 == 0:
    even_nums.append(num)


# Filtering (short hand with comprehension)

even_nums_comp = [num for num in nums if (num % 2) == 0]


# print(even_nums_comp)




# ------------------------- TUPLES

# names = ('John', 'Sara', 'Steve', 'Jane')
names = 'John', 'Sara', 'Steve', 'Jane'

# print(type(names)) # => <class tuple>

# Assignment/Reassignment not supported
# names[1] = 'Devon'

# Access Elements
first_person = names[0]
second_person = names[1]

# Unpacking
first_name, second_name, third_name, fourth_name = names

# print(second_person)
# print(second_name)
