# set aur dictonary dono curly brackets main bantay hain

s1 = {1,3,5}

s2= set() 
# dont use set = {} for empty set as this creates an empty dictonary.
# set() is used to create empty set

# set main koi item repeat ni ho sakta.. jese k agr main

s3 = { 10, 3 , -5 , 0.6, 7, 8.33, 1, 3, 1, 4, 2, 1, "Zuha"}
#print(s3) # {0.6, 1, 2, 3, 4, 7, 8.33, 10, 'Zuha', -5}

#set methods
s3.add("Alishba")
#print(s3)

setA = { 3,6,48,44,1,68,97}

setB = {44,68,2,77,88,34,22,56}

print(setA.union(setB))
print(setA.intersection(setB))
print(setA - setB)

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations? 20 == 20.0 is true so length is 2

set1 = {}
print(type(set1))