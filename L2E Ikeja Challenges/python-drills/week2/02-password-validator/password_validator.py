def has_min_length(password):
    if len(password) < 8:
        return False
    else:
        return True

def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def has_lowercase(password):
    for char in password:
            if char.islower():
                return True
    return False

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_special(password):
    for char in password:
        if not char.isalnum() and char != " ":
            return True
    return False

def is_valid_password(password):
    if has_digit(password) and has_lowercase(password) and has_min_length(password) and has_special(password) and has_uppercase(password):
        return True
    else:
        return False

# bonus
def get_failed_requirements(password):
    failed = []
    if has_min_length(password) == False:
        failed.append("min_length")
    if has_uppercase(password) == False:
        failed.append("uppercase")
    if has_lowercase(password) == False:
        failed.append("lowercase")
    if has_digit(password) == False:
        failed.append("digit")
    if has_special(password) == False:
        failed.append("special")

    return failed