courses = ['ba' , 'engineering' , 'farmancy', 'mba']
print(courses)

a= courses[1]
print(a)

a = courses[1:4]
print(a)

print(courses[-1])

courses = ['ba' , 'engineering' , 'farmancy', 'mba']
print(courses)

b = courses.append('homopbthy')
print(courses)

courses.insert(3 , 'ME')
print(courses)

new = ['1th' , '12th']
courses.append(new)
print(courses)

print(courses[-1])
#Hii
# The last 4 words are important in above definition - ELEMENTS FROM THE ITERABLE. ITERABLE in this case is thew new list that we are passing (see the first argument being passed to the function definiion)
# In other words, extend actually unpacks the other list and adds items to the original list instead of creating a nested list by simply inserting one list into the other

# Let's check
courses.extend(new)
print(courses)


print(courses[-1])

courses.remove("ba")
print(courses)

courses.remove(['1th' , '12th'])
print(courses)

courses.sort()
print(courses)

courses.append("['BEE' ,'B.tech']")
print(courses)

courses.pop(1)
print(courses)

print(courses)
for course in courses:
  print(course)

countries = ['russia' , 'india' , 'US', 'japan' , 'Germany' ]
print(len(countries))

print(len('HELLOjjmb'))

nums = [8,4,2,1,16]
print(max(nums))

for country in countries:
  print(country)
  print('inside loop(i am executing each time)')
print("i am i outside loop")

for country in countries:
  print(country)
  if country == 'india':
    print('inside loop(i am executing each time)')
print("i am i outside loop")

print("--------------------------")

for country in countries:
  print(country , len(country))

print("--------------------------")

for country in countries:
  print(country , "length of this country is :" , len(country))


for id,item in enumerate(countries):
  print(id , item)

cubes = []

for i in range(5):
  cubes.append(i**3)
  print(cubes)


cubes = []

for i in range(5):
  print(i)
  print(f" {i} *3 = " , i * 3)
  cubes.append(i**3)
  print(cubes)

print("final cube list is: " , cubes)

students = [['Durgesh', 'gaurav'] , ['mahesh' , 'manas', 'shiv' , 'gauri']]
print(students)
print(len(students))

print(students[0][1])
print(students[0])
students.append('rahul')
# students.extends['janhavi' , 'santosh'])
new = ['janhavi' , 'santosh']
students.extend(new)
print(students)
print(students[1])
print(students[1][1])
