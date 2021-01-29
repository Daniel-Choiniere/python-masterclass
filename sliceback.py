letters = "abcdefghijklmnopqrstuvwxyz"


print(letters[25::-1]) #zyxwvutsrqponmlkjihgfedcba

# reversing a sequence
print(letters[::-1]) #zyxwvutsrqponmlkjihgfedcba


print(letters[16:13:-1]) #qpo
print(letters[4::-1]) #edcba

print(letters[25:17:-1]) #zyxwvuts
print(letters[25:-9:-1]) #zyxwvuts
print(letters[:-9:-1]) #zyxwvuts

# A programming idiom or code idiom is expressing a special feature of a recurring construct in one or more programming languages
print(letters[-4:]) # wxyz - last four characters
print(letters[-1:]) # z - last character
print(letters[:1]) # a - first character - will not throw an error if string is empty
print(letters[0]) # a - first character - will throw an error if string is empty
