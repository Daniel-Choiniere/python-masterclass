parrot = "Norwegian Blue"

# Positive Indexing
print(parrot)

print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

# Negative Indexing
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# Positive Slicing
print(parrot[0:6]) # Norweg  - up to but not including
print(parrot[3:5]) # we
print(parrot[0:9]) # Norwegian
print(parrot[:9])  # Norwegian - start defaults to the begining of the sequence
print(parrot[10:14]) # Blue
print(parrot[10:]) # Blue - Need the colon or we would just get a single character
print(parrot[:]) # Norwegian Blue

# Negative Slicing - Counting from the end of the string instead of the beginning
print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl
print(parrot[-14:-8]) # Norweg
print(parrot[-11:-9]) # we
print(parrot[-4:]) # Blue
print(parrot[-4:14]) # Blue

# Slicing using step
print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = "9,223:373:036 854,775:807"
seperators = number[1::4]
print(seperators)
