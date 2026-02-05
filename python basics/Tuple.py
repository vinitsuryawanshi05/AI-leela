# Let's define one tuple by putting some data in round brackets. Separate data must be separated by comma. 

courses = ('ba', 'bcom', 'bsc')
print(courses)
print(type(courses))     # Note that we get class 'tuple' as output. 

# To access data, just like list, simply pass index within []

print(courses[1])    # Index 1 = Position 2

# If you type courses. you'll get only two suggestions, meaning tuples has only two functions defined specifically for them. Let's explore them 
# Check the last two entries when you run help()

help(tuple)

# count() - returns number of occurances of value
# Here 'ba' is used only once, hence output is 1

print(courses.count('ba'))
print(courses.count('baa'))    # 'baa' not part of courses. Output = 0

#  index() - returns the first index of value
# bsc is defined at third position (second index)

print(courses.index('bsc'))

#As you saw in list, you cannot add or change element of tuple once it is created. That's why there is no method like add() or insert() to tuple which allows you to add. 

### Let's explore further

# Let's re-define courses, and allow duplicate

courses = ('ba', 'bcom', 'bsc', 'bsc', 'ba')
print(courses)
print(courses.count('bsc'))            # 'bsc' is used twice hence 2
print(courses.index('bsc'))            # index returns the index of first occurance (so even if bsc is defined at index 2 and index 3, output will be 2)


# As we saw in the list, whenever there is collection of data, for loop becomes important. 
# Let's see simple example of for loop

for item in courses:     
  print(item)

# Use enumerate() function to get index of element as well

for id, item in enumerate(courses):    # enumerate() returns index along with main data. Hence you need two variables at the left (id, item). These names could be any. 
  print(id, item)

# Check length of the tuple
# len() comes handy. This function can be used over str, list, tuple and few more..

print(len(courses))

# If you are storing numbers in tuple, you don't need ''

nums = (2, 3, 4)
print(type(nums))

# Mix of str and int and bool is allowed in tuple

data = ('ba', 2, True, 'bsc')
print(data)
print(type(data))

# For the sake of it, let's check data type of each of the object

print(type(data[0]))
print(type(data[1]))
print(type(data[2]))

# Let's do the same with for loop
for item in data:
  print(item, type(item))

# TRICKY ONE. For single valued tuple, you have to add a comma, else it'll be treated as a string

new = ('50')              # this will be treated as string
print(type(new))

print('-----------------------------')

new1 = ('50',)            # this will be treated as tuple
print(type(new1))

#**Concat two tuples**

# simply use + to combine two tuples into one

print(('a','b','c') + (1, 2, 3))


# More than two tuples can also be added the same way

new = ('50',)
new1 = ('apple',)
new2 = ('mango','orange')
print(new + new1 + new2)



# To delete, use del
del new2
# print(new2)    # This will give error because new2 is not defined any more, it's deleted already

# check whether an element is in the tuple

fruits = ('apple','mango')

print('mango' in fruits)     # return True if 'mango' is part of fruits else False. Thanks to 'IN', it comes handy many times in the real world programs. 
print('mangoes' in fruits)



#  Algebraic operations like max, min etc

print(max(2, 1, 3, 7))
print(min(2, 1, 3, 7))


# To convert list into a tuple
num = [1, 2, 3, 4]
new = tuple(num)

print(num)
print(new)

### Playing with indexes