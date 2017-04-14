words = "Write a loop over this"
new = ""
vowels = ["e", "i", "o", "u", "y"]

for index, letter in enumerate(words):
    if letter in vowels and (index + 1) % 2 == 0:
        new +="a"
    elif (index+1)%5!=0:
        new+=letter

print(new)




