# Defina a function that takes an indefinite number of numbers as arguments and returns their average. 

def avg(*args):
    return sum(args) / len(args)

print(avg(1, 2, 3, 4, 5, 6))