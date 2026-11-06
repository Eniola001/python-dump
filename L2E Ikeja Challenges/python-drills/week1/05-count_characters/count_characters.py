def count_characters(text):
    letters, numbers, spaces, special = 0, 0, 0, 0

    for char in text:
        if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            letters += 1
        elif char in "0123456789":
            numbers += 1
        elif char in " ":
            spaces += 1
        elif char in "!@#$%^&*()_-+=[].?,<>/\\}{`~''":
            special += 1

    dict = {"letters": letters, "numbers": numbers, "spaces": spaces, "special": special}

    return dict