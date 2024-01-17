x = 5
y = "John"
print(x)
print(y)


k = 4       #k is type of int
k = "Sally" #k is now type of str
print(k)


#Casting

z = str(4) #z will be '4'
o = int(4)  #o will be 4
l = float(4) #l will be 4.0

#Get the type

j = 5
p = "John"
print(type(j))
print(type(p))



x = "John"
# is the same as
x = 'John'


a = 6
A = "Mansur"
print(a)
print(A)        #a and A is not same variables


#Variable names
#correct:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#incorrect:
"""
2myvar = "John"
my-var = "John"
my var = "John"

"""

#camel case
myNameIs = "Mansur"

#pascal case
MyNameIs = "Mansur"

#snake case
my_name_is = "Mansur"


#Multiple Values
e, f, r = "Besh", "Qurt", "Irimshik"
print(e)
print(f)
print(r)

g = s = q = "Orange"
print(g)
print(s)
print(q)


#unpack a list
foods = ["pizza", "burger", "sushi"]
t, i, j = foods
print(t)
print(i)
print(j)

var = "python is awesome"
print(var)


first = "Python"
second = "is"
third = "awesome"
print(first, second, third)


first = "Python "
second = "is "
third = "awesome"
print(first + second + third)


num1 = 4
num2 = 5
print(num1 + num2)

#incorrect
"""

x = 5
y = "John"
print(x + y)

"""


number = 5
name = "John"
print(number, name)



word1 = "awesome"
def myfunc():
    print("Python is " + word1)
myfunc()





word1 = "awesome"
def myfunc():
    word1 = "fantastic"
    print("Python is " + word1)
myfunc()

print("Python is " + word1)




#The Global Keyword
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)




word2 = "awesome"

def myfunc():
    global word2
    word2 = "fantastic"
myfunc()
print("Python is " + word2)