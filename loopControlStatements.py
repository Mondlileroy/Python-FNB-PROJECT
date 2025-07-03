#loop control statements

fruits = ["apple", "banana", "cherry", "date", ]

for fruit in fruits:
    if fruit == "banana":
        break # Exit the loop when "banana" is found
    print(fruit)
    
for fruit in fruits:
    if fruit == "banana":
        continue # Skip the rest of the loop when "banana" is found
    print(fruit)
    
    for fruit in fruits:
        if fruit == "banana":
            pass # Do nothing when "banana" is found
        print(fruit)
        
    
    count = 0
while count < 5:
    print(count)
    count += 1 # Increment the count by 1
    if count == 3:
        break # Exit the loop when count is 3
    print("Count is now 3, exiting loop.")