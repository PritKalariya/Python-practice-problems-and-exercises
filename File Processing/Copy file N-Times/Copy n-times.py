# Write a python code to duplicate the data within the given file

with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    new = file.write(content)
    new = file.write(content)