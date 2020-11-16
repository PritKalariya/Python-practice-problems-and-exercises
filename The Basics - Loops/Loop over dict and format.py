# Write a code to print the following output
# John Smith: +37682929928
# Marry Simpsons: +423998200919

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, values in phone_numbers.items():
    print(f"{key}: {values}")