for i in range(1, 13):
    # {0:2} - 2 is the field width so when we print the format is easier to read and visually appealing with everything lining up
    # {1:<3} - the < symbol denotes that the column will be formatted left aligned
    # {2:^4} - the ^ symbol denotes that the column will be formatted center aligned
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

# default format prints 15 decimals
print("Pi is approx {0:12}".format(22 / 7))
# adding f prints 6 decimals
print("Pi is approx {0:12f}".format(22 / 7))
# adding 50 before the f allows 50 decimals, but Python will not only allow a value with 50 decimals in 12,
# it overrides and decides the precision is more important and defaults to 50
print("Pi is approx {0:12.50f}".format(22 / 7))
# maximum precision in Python on a float decimal is ~51 points so there is no use in getting more precise
print("Pi is approx {0:52.50f}".format(22 / 7))
print("Pi is approx {0:62.50f}".format(22 / 7))
print("Pi is approx {0:72.50f}".format(22 / 7))