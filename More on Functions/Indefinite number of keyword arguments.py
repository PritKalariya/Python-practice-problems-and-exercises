# Define a function that takes a number of indefinite number of keyword arguments and find it's sum

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=4, b=5))
print(find_sum(a=4, b=5, c=1))