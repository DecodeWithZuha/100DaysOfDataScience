#list is a container to store set of values
# in list we can change the string 

#  For example

list= ["Hadi" , 68 , 52.66, 'hello', False]

print(list[0])
list[0] = "Nasir"

print(list[0]) 
#Lists are mutable, are flexible can change can store any type of data, we can add, remove , modify data

# List slicing same as string slicing

print(list)

print(list[1:4])#startfrom index 1 and end index will not be included

print(list[1:4:2]) # start from index 1, 4 will not beincluded.. from 1 jump 2 indexes until reach 4

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(nums[1:21:3])
print(nums[0:21:5])

# Every method applied on list changes the existing list

