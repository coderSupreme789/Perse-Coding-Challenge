name1, name2 = input(), input()
x = False

name = (name1.lower())[0] + (name2.lower())[0] + (name2.lower())[-1] + str(len(name1))
for letter in name:
    if name.count(letter) > 1:
        x = True
if x == True:
    name += "x"

print(name)
