x = 6    # int
y = 8.8  # float
z = 3j   # complex


#Int, or integer, is a whole number, positive or negative, 
#without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#Float, or "floating point number" is a number, 
#positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


#Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))



import random

print(random.randrange(1, 10))