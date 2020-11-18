# Apeend the text of "Bear1.txt" to "Bear2.txt"

with open("Bear1.txt") as file:
    content = file.read()

with open("Bear2.txt", "a") as file:
    file = file.write(content)