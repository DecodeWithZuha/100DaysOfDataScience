#you can create a new string with existing string but cannot change the orignal string.

a ="Zuha"

print(a[0])
a[0] = 'z' #TypeError: 'str' object does not support item assignment
print(a[0])


#Method #01
name = input(" Enter your name: ")
Date = input(" Enter Date: ")

print(f" Dear {name}, \n Your'e Selected! \n {Date}")

#Method#02

letter = '''Dear <|Name|>,
                You are selected!
                <|Date|>'''

#Strings are immutable which means the orignal straing never changes even if we use replace or any function

#Using ".replace chaining"
print(letter.replace("<|Name|>", "Zuha Nasir").replace("<|Date|>","14 Feb,2025"))
#With 1st replace it will create a new string, and then on that new string we will change date.

#What happens if we dont do it in new string
print(letter.replace("<|Name|>", "Zuha Nasir"))
print(letter.replace("<|Date|>","14 Feb,2025"))


# Every new method applied on string creates a new string.