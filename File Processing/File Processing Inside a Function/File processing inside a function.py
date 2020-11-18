# Define a functionn that gets a single string character and a file path as parameters and return the number of occurences of the character in the file

def foo(ch, filepath = "bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(ch)

print(foo('a'))
print(foo('v'))