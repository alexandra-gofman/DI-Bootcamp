def check_letter(a:str, b:str):
    if b in a:
        return True
    else:
        return False

print(check_letter("apple", "a"))  # Output: True
print(check_letter("banana", "z"))  # Output: False