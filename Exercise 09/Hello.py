'''
Exercise 9: Hello - 10 Marks
Fill in the blanks in the code below so that the function hello() prints “Hello”
to the console.

def hello():
____ # Fill in this blank to print "Hello" to the console
def main():
____ # Fill in this blank to call the hello() function
if __name__ == "__main__":
main()

'''

def hello():
    print("Hello")  # Print "Hello" to the console

def main():
    hello()  # Call the hello() function to print the greeting

# This checks if the script is being run directly (not imported)
if __name__ == "__main__":
    main()  # Call main() only if the script is run directly
