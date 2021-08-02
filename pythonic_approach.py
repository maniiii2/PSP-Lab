#1. Looping over a range of numbers

for i in [0, 1, 2, 3, 4, 5]:
    print(i**2)

for i in range(6):
    print(i**2)
  



#2. Looping over a collection
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(colors[i])

colors = ['red', 'green', 'blue', 'yellow']

for color in colors:
    print(color)



#3.Looping over dictionary keys

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

for i in d.keys():
    print(i)
 
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}


for i in d.keys():
    if i.startswith('m'):
         print(i)
        


#4. looping backwards   
    
colors = ['red', 'green', 'blue', 'yellow']


for i in range(len(colors)-1,-1,-1):
    print(colors[i])
    
colors = ['red', 'green', 'blue', 'yellow']
for color in reversed(colors):
    print(color)

names = ['priya' , 'chaitu' , 'satya' , 'varma']
colors = ['innocent', 'innocent', 'kantri fellow', 'innocent']
n = min(len(names) , len(colors))
for i in range(n):
    print(names[i] , '-->' , colors[i])
   
names = ['priya' , 'chaitu' , 'satya' , 'varma']
colors = ['innocent', 'innocent', 'kantri fellow', 'innocent']    
for name, color in zip(names, colors):
    print(name, '-->',color)

names = ['priya' , 'chaitu' , 'satya' , 'varma']
colors = ['innocent', 'innocent', 'kantri fellow', 'innocent']
for name,color in zip(names, colors):
    print(name,'-->',color)
  



#5. sorted list
names = ['priya' , 'chaitu' , 'satya' , 'varma']
for names in sorted(names):
    print(names)
   
names = ['priya' , 'chaitu' , 'satya' , 'varma']
print(sorted(names, key = len))




#6.using and and or

x = int(input("Please enter a number between 1 and 10: "))

if x > 0 and x < 11:
	print(x)
else:
	print("Invalid selection")


x = int(input("Please enter a number between 1 and 10: "))

if x < 1 or x > 10:
	print("Invalid selection")
else:
	print(x)



#7. usiing of list in differnt way

student=("chandu","raju","tarak","tejas","ramu")
print(student[0:3])

student=("chandu","raju","tarak","tejas","ramu")
print(student[:3])




#8.

list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]
  
print(list1)
print(list2)

list1 = [5, 4, 3, 2, 1]
list1 = list1 + [1, 2, 3, 4]
list2 = list1

print(list1)
print(list2)



#9.(a)
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print (x)
        t = y
        y = x + y
        x = t
print(fibonacci(5))
#(b)
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print (x)
        x, y = y, x + y
        print(fibonacci(5))



#10.(a)


x=5
y=10

temp=x
x=y
y=temp
print('The value of x after swapping: {}' .format(x))

print('The value ofyx after swapping: {}' .format(y))

#(b)
x=5
y=10
x,y=y,x
print("x = ",x)
print("y = ",y)



#11.(a)
a=[2,5,6]
b=[]
for i in a:
     if i>4:
         b.append(i)
print(b)         

#(b)
a=[2,5,6]
b=[i for i in a if i > 4]
print(b)


#12.(a)
f = open('file.txt')
a = f.read()
print (a)
f.close()
#(b)
with open('file.txt') as f:
    for line in f:
        print (line)





#13.(a)

age = 20
if age > 18 and age < 60:
    print("young man")

#(b)
if 18 < age < 60:
    print("young man")

#14.(a)
s1 = "puppy.net"
s2 = "puppies"
s3 = "welcome to %s and following %s" % (s1, s2)
print(s3)
#(b)
s3 = "welcome to {blog} and following {wechat}".format(blog="puppy.net", wechat="puppies")
print(s3)

#15.(a)
a=3
if a > 2:
    b = 2
else:
    b = 1
    print(b)

#(b)
a = 3   
b = 2 if a > 2 else 1
print(b)


#16.(a).
data = ["one", "two", "three"]
for i in range(0, len(data)):
    print(data[i])

    
#(b)

data = ["one", "two", "three"]
for val in data:
    print(val)
 



#17.(a)
list_number =[]
for i in range(10):
    list_number.append(i)
print(list_number)
  
#(b)
list_number = [idx for idx in range(10)]
print(list_number)





#18.(a)
x=[1, 2, 3, 4, 5, 6]

result = []

for idx in range(len(x)):
    result.append(x[idx] * 2)

print(result)
#(b)

x=[1, 2, 3, 4, 5, 6]

print([(element * 2) for element in x])

#19.(a)
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []

for idx in range(len(x)):
    if x[idx] % 2 == 0:
        result.append(x[idx] * 2)

else:
    result.append(x[idx])

print(result)
#(b)

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([element * 2 for element in x if element % 2 == 0])





#20.(a)
print("Hello Everyone!")
print("How are you?")

#(b)

print("Hello Everyone! \n How are you?")































