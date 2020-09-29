letter=list(input("Enter a letter:"))
for i in letter:
    if i==" ":
        letter.remove(" ")
print(letter)
polyndrom=letter[::-1]
if letter==polyndrom:
    print('letter is polyndrom')
else:
    print('letter is not polyndrom')