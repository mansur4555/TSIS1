"""
All types of data:
- Text Type:	str
- Numeric Types:	int, float, complex
- Sequence Types:	list, tuple, range
- Mapping Type:	dict
- Set Types:	set, frozenset
- Boolean Type:	bool
- Binary Types:	bytes, bytearray, memoryview
- None Type:	NoneType

"""
x = 5
print(type(x))
#<class 'int'>


#1
x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#2
x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#3
x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#4
x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#5
x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#6
x = ("apple", "banana", "cherry")

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#7
x = range(6)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#8
x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#9
x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#10
x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#11
x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#12
x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#13
x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#14
x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#15
x = None

#display x:
print(x)

#display the data type of x:
print(type(x)) 


#Setting the Specific Data Type:

x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview