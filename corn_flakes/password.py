import re


def check_email_validation(email):
    pattern = r'[a-zA-Z0-9]+@[a-zA-Z0]+\.[a-zA-Z]'
    if re.fullmatch(pattern, email):
        return True
    else:
        return False


