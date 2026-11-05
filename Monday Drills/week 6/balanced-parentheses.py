# Problem
# Determine whether a string contains balanced brackets.
# Every opening bracket must have a matching closing bracket of the same type in the correct order.
# Handle round (), square [], and curly {} brackets.

# Examples
# Input: "(a + b) * [c - d]" → Balanced
# Input: "(a + b)]" → Not balanced (mismatched type)
# Input: "((a + b)" → Not balanced (unclosed)
# Input: "[(a + b) * {c - d}]" → Balanced
# Input: "([)]" → Not balanced (wrong order)

string = input("Input: ")

def is_balanced(string):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in '([{':
            stack.append(char)

        elif char in ')]}':
            if not stack:
                return "Not balanced (mismatched type)"

            if stack[-1] != pairs[char]:
                if char in pairs and pairs[char] in stack:
                    return "Not balanced (wrong order)"
                else:
                    return "Not balanced (mismatched type)"

            stack.pop()

    if stack:
        return "Not balanced (unclosed)"
    else:
        return "Balanced"

print(is_balanced(string))

# Examples
# print(is_balanced("(a + b) * [c - d]")) # Balanced
# print(is_balanced("(a + b)]")) # Not balanced (mismatched type)
# print(is_balanced("((a + b)")) # Not balanced (unclosed)
# print(is_balanced("[(a + b) * {c - d}]")) # Balanced
# print(is_balanced("([)]")) # Not balanced (wrong order)

# Easier way of solving:
# def is_balanced(string):
#     stack = []

#     for char in string:
#         if char in "([{":
#             stack.append(char)

#         elif char in ")]}":
#             if not stack:
#                 return "Not balanced (mismatched type)"

#             opening = stack.pop()

#             if (opening == '(' and char != ')') or \
#                (opening == '[' and char != ']') or \
#                (opening == '{' and char != '}'):
#                 return "Not balanced (mismatched type or wrong order)"

#     if stack:
#         return "Not balanced (unclosed)"
#     else:
#         return "Balanced"