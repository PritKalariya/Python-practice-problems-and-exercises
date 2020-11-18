# Read the "bear.txt" file and print out the first 90 characters.

with open("Bear.txt") as file:
    words = file.read()
    print(words[:90])