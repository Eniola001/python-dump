try:
    num = int(input("Enter a number: "))
    print("You entered", num)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Enter a whole number dammit!!!")
else:
    print("No error caught! Womp womp :(")
finally:
    print("Finished.")

# Multi line Comments
poem = '''Roses are red,
Violets are blue,
Python is fun,
And easy too.'''

# Formatted Strings
print(f"{num * poem}")
