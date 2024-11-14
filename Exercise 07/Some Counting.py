'''
Exercise 7: Some Counting - 20 Marks

Use your newly acquired knowledge of the for loop to complete the following
tasks.

Print all values to the console in each case. 
* Write a loop that counts up from 0 to 50 in increments of 1. 
* Write a loop that counts down from 50 to 0 in decrements of 1. 
* Write a loop that counts up from 30 to 50 in increments of 1. 
* Write a loop that counts down from 50 to 10 in decrements of 2. 
* Write a loop that counts up from 100 to 200 in increments of 5. 
You may include all loops in a single project

'''
# Loop that counts up from 0 to 50 in increments of 1
print("Counting up from 0 to 50:")
for i in range(0, 51):  # Starts at 0 and goes up to 50 (inclusive)
    print(i)  # Print each value of i

# Loop that counts down from 50 to 0 in decrements of 1
print("\nCounting down from 50 to 0:")
for i in range(50, -1, -1):  # Starts at 50, ends at 0, decreasing by 1 each time
    print(i)  # Print each value of i

# Loop that counts up from 30 to 50 in increments of 1
print("\nCounting up from 30 to 50:")
for i in range(30, 51):  # Starts at 30 and goes up to 50 (inclusive)
    print(i)  # Print each value of i

# Loop that counts down from 50 to 10 in decrements of 2
print("\nCounting down from 50 to 10 in decrements of 2:")
for i in range(50, 9, -2):  # Starts at 50, ends at 10, decreasing by 2 each time
    print(i)  # Print each value of i

# Loop that counts up from 100 to 200 in increments of 5
print("\nCounting up from 100 to 200 in increments of 5:")
for i in range(100, 201, 5):  # Starts at 100, goes up to 200 (inclusive), increasing by 5 each time
    print(i)  # Print each value of i
