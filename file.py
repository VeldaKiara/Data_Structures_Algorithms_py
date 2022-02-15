#sequential
a=40
b=20
c=a-b
print("Subtraction is : ",c) #20

#selection statements
#simple if statements
n = 10
if n % 2 == 0:
   print("n is an even number")

#if-else statements
n = 5
if n % 2 == 0:
   print("n is even")
else:
   print("n is odd")

#nested if statements
l = 10
u = 12
x = 17
if l > u:
   if l > x:
      print("l value is big")
   else:
       print("x value is big")
elif u > x:
    print("u value is big")
else:
     print("x is big")   #x is big

#if-elif-else statements
v = 15
k = 12
if v == k:
   print("Both are Equal")
elif v > k:
    print("v is greater than k")
else:
    print("v is smaller than k")
    # v is greater

#repetition

#sets
print(set())
print(my_set:={1,4,5,6,7,8,})
if 4 in my_set:
    print("in set")
else:
    print("nada")
    
"""output
set()
{1, 4, 5, 6, 7, 8}
in set
"""

#dictionaries
#using default dict
from collections import defaultdict
v = defaultdict()
v[1] = 'apple'
v[2] = 'pineapple'
print(v) 

#normal dictionaries, key value pair
k = {}
k = {1: 'banana', 2: 'orange'}
print(k)
print(k[1])

'''
output
defaultdict(None, {1: 'apple', 2: 'pineapple'})
{1: 'banana', 2: 'orange'}
banana
'''
#tuples
my_tuple = (2, 5, 4)
print(my_tuple)
print(my_tuple[0])
#cannot be updated but can be used to form other tuples
print(my_2_tuple := (5,6,7))

my_3_tuple = my_tuple + my_2_tuple
print(my_3_tuple)
'''output
(2, 5, 4)
2
(5, 6, 7)
(2, 5, 4, 5, 6, 7)
'''
#lists
empty_list = [ ]
print(array := [1,2,3,4,5,6,7])
print(array[3])
array.append(10)
print(array)
#deleting a list
# del array
# print(array)

#for loops
lst = [1, 2, 3, 4, 5]

for i in range(len(lst)):
     print(lst[i], end = " ")
 
for j in range(0,10):
    print(j, end = " ")
'''Output
1 2 3 4 5 0 1 2 3 4 5 6 7 8 9 
'''
#while loops
v = 6
k = 1
while k < v:
     print(k, end = " ")
     k += 1
print("End")

''' output
1 2 3 4 5 End
'''

#functions
#built in 
print(x := abs(-8.35)) #8.35

#user-defined
def lux():
   print("Just a function having fun in lux workshop")
lux()
 #Just a function having fun in lux workshop

 #syntax of functions
def IsEven(v):
    """ function to find even numbers"""
    if (v % 2 == 0):
        return "Even"
    else:
        return "Not Even"
    
print(IsEven (11)) #Not Even

# Python code to demonstrate call by value
def greet(sal):
    ''' call by value'''
    string = "Good Morning"
    print(string)
   
greet("hi")
#good morning


# Python code to demonstrate call by reference
def append_to_list(list1):
    '''call by reference'''
    list1.append(35)
    print(list1)
append_to_list(multiples_of_5 := [5,10,15,20,25,30])
#[5, 10, 15, 20, 25, 30, 35]

#naming functions with their work
def multiply(a:int, b:int):
   print (a*b)
multiply(5,10)
#50

#single parameter
def hello(name):
    print ("Hello", name)
hello("Anna")
#Hello Anna

#multiple parameters
def hello(name1, name2, name3):
    print("Hello", name1, "\nSasa",  name2, "\nMambo",  name3)
hello("Harun", "Lux", "Mentees")

# Hello Harun 
# Sasa Lux 
# Mambo Mentees

#required arguments
def hello(name):
    print ("Hello", name)
hello("Anna")
#Hello Anna

#keyword args
def hello(fname, lname):
    print('Hello', fname, lname)
 
hello(lname='Murithi', fname='Gerard')
#Hello Gerard Murithi
#not knowing keywords
hello(fname="Nadella", lname="Satya")
hello(lname="Pichai", fname="Sundar")
#results to error if more than 3 names, or 1 name provided
#Hello Nadella Satya
#Hello Sundar Pichai

#Default args
def hello (name="Vee"):
   print("Hello", name)
hello()
hello("You")
#Hello Vee
#Hello You

#variable length
def hello(*names):
    for name in names:
        print("Hello", name)
hello("Velda", "Maryann", "Ressie")
''' output
Hello Velda
Hello Maryann
Hello Ressie
'''

#Recursive functions
def recursive_sum(v):
    if v<=1:
        return v
    else:
        return v + recursive_sum(v-1)
print(v:=recursive_sum(5))
#15

#anonymous functions
double = lambda v: v * 2
print(double(4))
#8

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda v: (v % 2 == 0) , my_list))

print(new_list)
#[4, 6, 8, 12]

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda v: v * 2 , my_list))

print(new_list) 
#[2, 10, 8, 12, 16, 22, 6, 24]

#decorators
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper 

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())
#HELLO THERE

#classes
class Person:
    
    # class attribute
    species = "human"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Person class
Tony = Person("Tony", 20)
Stark = Person("Stark", 25)

# access the class attributes
print("Tony is a {}".format(Tony.__class__.species))
print("Stark is also a {}".format(Stark.__class__.species))

# access the instance attributes
print("{} is {} years old".format( Tony.name, Tony.age))
print("{} is {} years old".format( Stark.name, Stark.age))

'''output
Tony is a human
Stark is also a human
Tony is 20 years old
Stark is 25 years old
'''

class Person:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now moon walking".format(self.name)

# instantiate the object
Tony= Person("Tony", 20)

# call our instance methods
print(Tony.sing("'Happy past Valentine's day'"))
print(Tony.dance())
'''output
Tony sings 'Happy past Valentine's day'
Tony is now moon walking
'''
#inheritance
# parent class
class Person:
    
    def __init__(self):
        print("This Person is ready")

    def whoisThis(self):
        print("Person")

    def sing(self):
        print("Sing faster")

# child class
class Velda(Person):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Velda is ready")

    def whoisThis(self):
        print("Person")

    def run(self):
        print("Run faster")

karimi = Velda()
karimi.whoisThis()
karimi.sing()
karimi.run()
'''output
This Person is ready
Velda is ready
Person
Sing faster
Run faster
'''

#encapsulation
class Computer:
    
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

'''output
Selling Price: 900
Selling Price: 900
Selling Price: 1000
'''

#polymorphism
class Velda:
    
    def sing(self):
        print("Velda can sing")
    
    def swim(self):
        print("Velda can swim")

class Kiara:

    def sing(self):
        print("Kiara can't sing")
    
    def swim(self):
        print("Kiara can swim")

# common interface
def singing_test(person):
    person.sing()

#instantiate objects
Karimi = Velda()
Mugambi = Kiara()

# passing the object
singing_test(Karimi)
singing_test(Mugambi)

'''output
Velda can sing
Kiara can't sing
'''

#dsa
# Creating a stack
def stack():
    stack = []
    return stack

# Creating an empty stack
def isEmpty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (isEmpty(stack)):
        return "stack is empty"

    return stack.pop()

stack = stack()
push(stack, "me")
push(stack, "we")
push(stack, "us")

print("popped item: " + pop(stack))
print("stack after popping an element: ", stack)

'''output
pushed item: me
pushed item: we
pushed item: us
popped item: us
stack after popping an element:  ['me', 'we']
'''
#queues
class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(0)
q.enqueue(2)
q.enqueue(0)
q.enqueue(2)
q.enqueue(2)

q.display()

q.dequeue()

print("After removing an element")
q.display()

''' output
[0, 2, 0, 2, 2]
After removing an element
[2, 0, 2, 2]
'''
#linkedlist
class Node:
    def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()
'''output
Mon
Tue
Wed
'''

# HashTable 
hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "make a circle")
insertData(456, "a big circle")
insertData(789, "like a sufuria")

print(hashTable)

removeData(123)

print(hashTable)

'''output
[[], [], [123, 'make a circle'], [], [], [456, 'a big circle'], [], [], [789, 'like a sufuria'], []]
[[], [], 0, [], [], [456, 'a big circle'], [], [], [789, 'like a sufuria'], []]
'''
