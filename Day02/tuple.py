a= (1,2,3,4,5)

print(type(a)) #<class 'tuple'>

b=()#empty tuple

c= (1) # <class 'int'>
print(type(c))

d = (1,) # tuple with  value
print(type(d))

e= (1, "hi" , 6.2 , '56')
e[1] = "hello"
print(e[1]) # TypeError: 'tuple' object does not support item assignment
print(e)