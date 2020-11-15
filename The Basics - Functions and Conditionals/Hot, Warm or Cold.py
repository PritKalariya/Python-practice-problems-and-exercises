# Write a function that:
# 1. Takes a temperature as parameter
# 2. Returns 'Hot' if the temp is greater than 25
# 3. Returns 'Warm' if the temp is between 15 and 25, including 15 and 25
# 4. Return 'Cold' if temp is less than 15

def meter(temp):
    if temp > 25:
        return "Hot"
    elif temp >=15 and temp <=25:
        return "Warm"
    else:
        return "Cold"
        
print(meter(10))
print(meter(20))
print(meter(30))