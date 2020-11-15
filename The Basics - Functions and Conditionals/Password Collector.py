# Define a function that:
# 1. Takes a string as parameter
# 2. Returns 'False' if the string contains less than 8 characters
# 3. Returns 'True' if the string contains 8 or more characters

def foo(myStr):
    if len(myStr) < 8:
        return False
    else:
        return True
        
print(foo("mypass"))
print(foo("mylongpass"))