splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print("The pet shop owner said 'No, no, \'e\'s uh,...he\'s resting'.")
# or you can do the same with this syntax
print("The pet shop owner said \'No, no, 'e's uh,...he's resting\'.")
# or using triple quotes you don't need an escape backslash
print("""The pet shop owner said "No, no, 'e's uh,...he's resting". """)

# when using triple quotes it will take your newlines literally
anotherSplitString = """This string
has been 
split
over several lines"""

print(anotherSplitString)

# escaping backslash characters by using double backslashes or using the "raw string"
print("C:\\Users\\tanchoiniere\\notes.txt")
print(r"C:\Users\tanchoiniere\notes.txt")

