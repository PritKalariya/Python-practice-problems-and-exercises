# Define a function that takes as a parameter a list that contains both integers and strings and returns the list containing only integers.

def foo(lst):
    return [i for i in lst if isinstance(i, int)]