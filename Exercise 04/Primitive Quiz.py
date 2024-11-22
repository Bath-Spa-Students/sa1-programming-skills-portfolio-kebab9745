'''
Exercise 4: Primitive Quiz - 30 Marks
In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.

Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong.

Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question.

'''
# Ask the user a question about the capital of France
answer = input("What is the capital of France? ")  # Prompt the user to enter an answer

# Check if the answer is correct
if answer.lower() == "Paris":  # Convert the answer to lowercase and compare it to "paris"
    print("Correct!")  # Print "Correct!" if the answer is right
else:
    print("Wrong answer.")  # Print "Wrong answer" if the answer is incorrect

