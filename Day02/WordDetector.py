#This program can detect your input word from any paragraph

paragraph = input(" Enter a Statement or a Paragraph: ")
word = input(" Enter word to find: ")

index = paragraph.find(word) 
print(f" The \" {word} \" word is on {index} index." )