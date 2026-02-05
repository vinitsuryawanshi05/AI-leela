num1= 3
num2 = 5
print(num1 , " , " , num2)
print(type(num1) , type(num2))

print(num1 + num2)
print(num1 ** num2)

print(5*4 + 2 - (2-1) / 2)

print(3!= 2)
print(3 == 2)
print( 3> 3)
print( 3>= 3)

num = 4
num += 3
print(num)

print(True and True)
print(True and False)
print(False & False)

print(True or False)
print( True | True)
print(False | False)

x=5
a = (( x> 2) & ( 4 < x))

x= 9
b = (( x> 2) & ( 4 < x))

x=1
c = (( x> 2) & ( 4 < x))

print("first answer" , a)

print("Second answer" , b)

print("Third answer" , c)

x = 5
print(not(x > 3 and x < 10))

print(round(3.45))
print(round(3.5111))
print(round(3.65))
print(round(3.495))
print(round(3.495 , 2))
print(round(3.4956 , 3))

new1 = 2.1
new2 = 0.3

print(new1 + new2 )
print(new1 - new2)


num1 = "hello"
num2 = '5'
print(num1 + num2) 


a = 'a'
b = str(a)
print(b)
print(type(a))
print(type(b))

a= int(input("enter the number 1"))
b = int(input("Enter the number 2"))
print(a+b)
print("--------------")
a= input("enter the number 1")
b = input("Enter the number 2")
print(a+b)


x = int(input("Enter the first number"))
y = int(input("Enter the Second number"))

if x>y:
  print(f" x = {x} is big number")

else:
  print(f" y = {y} is big number")

a= 5
if a:
  print(a)
else:
  print("eroro-drh")

# You can pass boolean value (True or False) to the condition in if. In that case, you don't need any logical operator like == or !=


is_subscribed = True
if is_subscribed:              # Read it like - if True do THIS else do THAT
    print('Thank you for the subscription!')  
else:
    print('Please subscribe')



x=7
if x < 10:
  print("x is smaller")

  if ( x < 5):
    print("internal if runs")
  
  else:
    print("internal else runs")

else:
    print("x is bigger")

