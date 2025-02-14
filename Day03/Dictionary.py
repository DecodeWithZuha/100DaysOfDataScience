marks= {
    "Zuha": 89,
    "Alishba": "92",
    "Fajar": "92", # No repitition of Keys
    "92": 100,
    92: 78
}

# print(marks, type(marks))

# ismain 0 index ni hota agr kro toh error dega
# print(marks[0])

#  isko aisay liktay hain
print(marks["Zuha"])
print(marks["92"]) # agr 2nd value lagao tog error deta hy.. usko string kr k b lagao tab b erroe deta hy.. sirf 1st walue k corresponding deta hy
print(marks[92]) # valid

print(marks.items()) # displays all dictornary items inform of tuple
print(marks.values()) # display values of all keys
print(marks.keys()) # display all keys

marks.update({"Zuha" : 95 , "Hadi" : 68 , "Waleed" : 99}) # changes value in orignal dictornary, and if the key is not there it will add new key.
print(marks)

print(marks.get("Zuha"))
print(marks["Zuha"])

# Both of these are different 
print(marks.get("Ameer")) # Prints none if key is not present
print(marks["Ameer"]) # Returns error if key is not present

