a='md sohag hossain'
print(len(a))
a=a.split()
#for i in range(len(a)):
print(a[0])

import keyword
print(keyword.kwlist)

def my_function(): # This is a function definition. Note the colon (:)
   a = 2 # This line belongs to the function because it's indented
   return a # This line also belongs to the same function
print(my_function())

x= str(input('Please give me your name='))
y=int(input('Enter your number='))
y/2
z=float(y)/2
print(x)
print(z)

str_name='Md Sohag'
print(str_name[0])
print(str_name[0:5])

b=frozenset('asdfagsa')
print(b)

tuple =(123,'hello')
tuple1=('sohag')
print(tuple[0])
print(tuple)
print(tuple+tuple1)
