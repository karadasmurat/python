def greet():
   print("Hello world!")

# Conditional Guard
# Only runs when the file is executed directly, not when imported as a module greet()
if __name__ == "__main__":
    greet()
    print("Hi, this is Module 11!")