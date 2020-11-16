# Loop over the colors items and print out the item in every loop only if the item is an integer and it is greater than 50.

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)