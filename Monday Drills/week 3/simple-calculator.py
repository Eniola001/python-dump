# SIMPLE-CALCULATOR
total = 0
running = True
memory = [total]

def convert(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s

while running:
    operation = input("Enter a operation: ").split()
    operator = operation[0]
    
    if operator not in ("+", "-", "*", "/", "quit", "undo"):
        print("Invalid operator.")
    elif operator == "+":
        total += convert(operation[1])
        memory.append(total)
        print(f"Result: {total}")
    elif operator == "-":
        total -= convert(operation[1])
        memory.append(total)
        print(f"Result: {total}")
    elif operator == "*":
        total *= convert(operation[1])
        memory.append(total)
        print(f"Result: {total}")
    elif operator == "/":
        if operation[1] == "0":
            print("Cannot divide by zero.")
        else:
            total /= convert(operation[1])
            memory.append(total)
            print(f"Result: {total}")        
    elif operator == "undo":
        if len(memory) > 1:
            memory.pop()
            total = memory[-1]
            print(f"Result: {total}")
        else:
            print("Nothing to undo.")
    elif operator == "quit":
        break
    
    
