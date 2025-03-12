#Camel Case 4

import sys
import re

def split_camel_case(s):
    """Splits camelCase or PascalCase and converts to lowercase with spaces."""
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s).lower()

def to_camel_case(s, capitalize_first=False, is_method=False):
    """Converts a spaced string to camelCase or PascalCase."""
    words = s.split()
    if capitalize_first:
        words = [word.capitalize() for word in words]
    else:
        words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    
    result = "".join(words)
    return result + "()" if is_method else result

# Read input from stdin
for line in sys.stdin:
    parts = line.strip().split(" ", 1)  # Split once at the first space
    if len(parts) < 2:
        continue  # Skip invalid input

    command, text = parts
    op_type, case_type = command[0], command[2]  # Extract operation and type

    if op_type == 'S':  # Split
        print(split_camel_case(text))

    elif op_type == 'C':  # Combine
        capitalize_first = (case_type == 'C')  # PascalCase for classes
        is_method = (case_type == 'M')  # Append '()' for methods
        print(to_camel_case(text, capitalize_first, is_method))


#another silution
while True:
    try:
        x = input().strip()  # Read input and remove extra spaces
    except EOFError:
        break  # Stop loop if EOF is reached

    if not x:
        break  # Stop if input is empty

    # Your existing code goes here...
    if x[0] == 'S':
        x = list(x)  # Convert string to list for modification

        if x[2] == 'M':
            i = 5
            while i < len(x):
                if x[i].isupper():
                    x[i] = x[i].lower()
                    x.insert(i, ' ')
                    i += 1  # Skip the inserted space
                i += 1
            x = x[:-2]  # Remove the last two characters

        elif x[2] == 'V':
            i = 5
            while i < len(x):
                if x[i].isupper():
                    x[i] = x[i].lower()
                    x.insert(i, ' ')
                    i += 1
                i += 1

        elif x[2] == 'C':
            x[4] = x[4].lower()
            i = 5
            while i < len(x):
                if x[i].isupper():
                    x[i] = x[i].lower()
                    x.insert(i, ' ')
                    i += 1
                i += 1

        print("".join(x[4:]))  # Convert list back to string and print

    elif x[0] == 'C':
        x = list(x)  # Convert string to list for modification

        if x[2] == 'M':
            i = 5
            while i < len(x):
                if x[i] == ' ':
                    x = x[:i] + [x[i+1].upper()] + x[i+2:]  # Convert to list
                i += 1
            x += ['(', ')']  # Add '()' to the end

        elif x[2] == 'V':
            i = 5
            while i < len(x):
                if x[i] == ' ':
                    x = x[:i] + [x[i+1].upper()] + x[i+2:]  # Convert to list
                i += 1

        elif x[2] == 'C':
            x[4] = x[4].upper()
            i = 5
            while i < len(x):
                if x[i] == ' ':
                    x = x[:i] + [x[i+1].upper()] + x[i+2:]  # Convert to list
                i += 1

        print("".join(x[4:]))  # Convert list back to string and print
