# Define a function that takes as parameter a list that contains both numbers and strings and returns the same list but with zeros intead of strings.
# Replace strings with 0

def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]