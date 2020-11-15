# Write a function that: 
# 1. Takes a temperature as parameter
# 2. Returns 'Warm' if the temp is greater than 7
# 3. Returns 'Cold' if the temp is equal or less than 7
  
def meter(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"
        
print(meter(10))
print(meter(5))