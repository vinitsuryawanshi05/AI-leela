# Let's store a string (string = any kind of text) in a variable. In the following example, 'dummy' is a variable which holds some text data (string) 
# Use print() to print something (it's not necessary in google colab, but tag along with us here for now)

dummy = "Hello world!"
print(dummy)

num1 = 6
num2 = 4.2
print(num1)
print(num2)

print(type(num1))
print(type(num2))

# Let's check the data type of variable 'dummy'

print(type(dummy))

# Let's explore other data type quickly before focusing our attention to strings

num = 3
another_num = 3.0
print(type(num))
print(type(another_num))

val = True
print(type(val))

# Let's just print the actual values 

print(num)
print(another_num)
print(val)

#STRINGS
# Few things to note. String has to be mentioned within '' or ""
# If your string needs ' for some reason, then you can use escape character \ like below. 

test = 'Apple\'s products are beautiful' 
print(test)

# Try running the above example without \ and you'll get an error. 
# When you do need to use ' in the sentence, then you can simply use "" for wrapping the string. 

test = "Apple's products are beautiful" 
print(test)

# Use len() function to check length of the string (this includes the blank spaces as well)

text = "Hello World"
print(len(text))

# To print a character at specific position, pass the position to the variable as shown below. 
# Note, (in python and many other programming languages) positions start with index 0, so 0th index = 1st letter and so on. 

text = "Hello Planet"
print(text[0])
print(text[4])

text = "Welcome to Python!"

# prints string from index 2 upto 5 (i.e. from 3rd letter to 6th letter)
print(text[2:5])

# prints string upto index 2 (i.e. print index 0 and index 1 (first and second letter))
print(text[:2])

# prints string starting from index 2 onwards
print(text[2:])

# prints the datatypes of the passed string.
# Sliced String is a string only, so its datatype is string only. 

text = "Welcome to Python!"
print(type(text))
print(type(text[2:4]))


text = "heLLo worLD!"

# prints string in uppercase
print(text.upper())

# prints string in lowercase
print(text.lower())

# prints first letter of each word in uppercase and rest in lowercase
print(text.title())

# Use count() to check how many times a particular character is repeated in the text
text = 'hello world'
print(text.count('l'))

# You can use count() to check more than one word
# In the following example 'rl' has appeared only once, hence output is 1

print(text.count('rl'))

# To check at what index a particular letter exists, use find(). 

print(text.find('o'))

# If the passed character does not belong to the string, then it returns -1
print(text.find('Z'))

# Note that above functions are case sensitive by default. 

print(text)             # our sample string - hello world
print(text.count('H'))  # we are trying  to count 'H' (not 'h')
print(text.find('H'))

# A full word can also be found with the help of find() function
# In the following example, beautiful word stats with index 10 (i.e. 11th letter onwards including space)

text = 'This is a beautiful world'
print(text.find('beautiful'))

print(text.count('beautiful'))   # exists only once
print(text.count('is'))          # 'is' appears twice (in first and second word)

# Let's replace a word by some other word

print(text.replace('world', 'planet'))

# Replace function does not change our original text, instead it returns us a new string. So as you can see below, the original text is maintained as it was. 
print(text)

# Here we are defining another variable and using it to store the output of replace() function.

new_text = text.replace('world','planet')
print(new_text)
print(text)

fruit = 'applllllleeeeeee'
print(fruit.replace('e','E'))
print(fruit.replace('z','E'))    # No change because 'z' does not exist in the original string

# strip() removes the blank spaces before and after the first and last character respectively 

msg = '   Hello World    '
print(msg)
print(msg.strip())

# To cross check whether it is really deleting the blank spaces, let's use the len() function

print(len(msg))
print(len(msg.strip()))

# The other way to cross check is to measure the number of blank spaces with count() function

print(msg.count(' '))
print(msg.strip().count(' '))  # The other way to do the same thing is ==>  new = msg.strip()    THEN    print(new.count(' ')). We just combined two commands in one. 

# split() is important one. It comes handy in many programs. 
# split() separates the content of the string accord to a specific (passed) character

# The following string will be broken into a list of string whenever ',' is observed
address = '102, Baker St, London'
print(address.split(','))

test = 'how are you doing'
print(test.split(' '))  # Break the string whenever there is a single blank space

# Let's store the result of about command in a variable and see the data type of that new variable

output = test.split(' ')
print(output)
print(type(output))

# Connecting two strings together
# Simply use + to combine strings

first = 'Bill'
last = 'Musk'
name = first + last
print(name)

name = first + ' ' + last
print(name)

name = first + '    ' + last
print(name)

# Another way to do the same 


name = '{}{}'.format(first, last)
print(name)

name = '{} {}'.format(first, last)
print(name)

name = '  {}     {}  '.format(first, last)
print(name)

name = '  {}     {}  '.format(last, first)
print(name)

# {} is a special placeholder, that can be used within string, and passing the desired variable with .format()

# Yet another way to do the same (short and sweet)
# This is called 'f string'. Simply pass the variable name inside f'' within {}

name = f'{first}{last}'
print(name)

name = f'{first} {last}'
print(name)

name = f'{first}    {last}'
print(name)


# You can use the string functions within fstrings

name = f'{first.upper()} {last.lower()}'
print(name)

num1 = 3
num2 = 5
print(num1, num2)
print(type(num1), type(num2))

# You can carry out addition simply by +

res = num1 + num2
print(res)

# You can carry out arithmatic operations simpy by using arithmatic operations such as + - * / // %

print(num1-num2)
print(num1*num2)
print(num2 / num1)   # division sometimes may result in float
print(num2 // num1)  # this is called floor division i.e. the output is quotient without reminder
print(num2 % num1)   # this is called modulus i.e. the reminder after division

# Let's cross check data type of division

print(type(num2/num1))

# Just like integer, arithmatic operations can be applied on float

new1 = 2.1
new2 = 0.3

print(new1 + new2)
print(new1 - new2)


# Float and integer can be added to each other

fir = 3
sec = 0.1
print (fir + sec)

# Let's accept input from user
# input is a special function that allows user to type (and pass) user's own input

name = input('enter your name')   # once this is run, type anything in the box
print(name)
print(type(name))

 # Now let's do some string operations on the passed string

text = input('Enter some text    ->')    # Pass any text
print(text.upper())
print(text.title())
print(text.find('e'))
print(text.count('e'))
print(text.replace('e','z'))
print(len(text))


# Use help() function to get brief info about all the methods supported by a data type (or claass)

help(str)   