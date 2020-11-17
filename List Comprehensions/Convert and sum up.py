# Define a function thaat takes as parameter a list that contains decimal numbers as strings and return the sum of those numbers.

def doo(lst):
    return sum([float(i) for i in lst])