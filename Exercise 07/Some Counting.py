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
# Count up from 0 to 50, one step at a time
print("Counting up from 0 to 50:")
for i in range(0, 51):  # Start at 0 and go up to 50 (inclusive)
    print(i)  # Print each number as we go

# Count down from 50 to 0, one step at a time
print("\nCounting down from 50 to 0:")
for i in range(50, -1, -1):  # Start at 50 and go down to 0
    print(i)  # Print each number as we go

# Count up from 30 to 50, one step at a time
print("\nCounting up from 30 to 50:")
for i in range(30, 51):  # Start at 30 and go up to 50 (inclusive)
    print(i)  # Print each number as we go

# Count down from 50 to 10, two steps at a time
print("\nCounting down from 50 to 10 in decrements of 2:")
for i in range(50, 9, -2):  # Start at 50 and go down to 10, decreasing by 2 each time
    print(i)  # Print each number as we go

# Count up from 100 to 200, five steps at a time
print("\nCounting up from 100 to 200 in increments of 5:")
for i in range(100, 201, 5):  # Start at 100 and go up to 200 (inclusive), increasing by 5 each time
    print(i)  # Print each number as we go
