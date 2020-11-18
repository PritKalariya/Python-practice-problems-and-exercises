# Create a file.txt that contains the first 90 characters of bear.txt

with open("Bear.txt") as file:
    file = file.read()
    words = file[:90]

with open("File.txt", "w") as file2:
    file2 = file2.write(words)