def compare_string(string1, string2):
    if sorted(string1) != sorted(string2) and len(string1) != len(string2):
        return False
    return True


def swap_sting(string1, string2):
    letter = string1.replace(string1[2],string2[2])
    letter2 = string2.replace(string2[2],string1[2])

    return letter2 + " " +letter

