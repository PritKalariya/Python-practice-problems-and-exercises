# Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings in UPPERCASE and sorted alphabetically.

def foo(*args):
    args = [i.upper() for i in args]
    return sorted(args)

print(foo("snow", "glacier", "iceberg"))