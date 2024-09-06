def compare_string(string1, string2):
    if sorted(string1) != sorted(string2) and len(string1) != len(string2):
        return False
    return True

