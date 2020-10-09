#! python3
# copy paste with pyperclip
# add bullets to the data
# save in file with pandas


import pyperclip as pc

# getting copied data
text = pc.paste()
print(text)

# spliting the copied data into a list of each copied sentence
lines = text.split('\n')


for i in range(len(lines)):
    # adding a * to the begining of each line
    lines[i] = '*' + lines[i]

# making a document
completedocs = '\n'.join(lines)

with open('autopasted.txt', '+a') as fileitem:
    fileitem.writelines(completedocs)
    print(fileitem.read())
