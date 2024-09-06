def separate_letters(letters):
    new_letter = {}
    for letter in letters:
        new_letter[letter.lower()] = letters.count(letter).lower()
    return new_letter


def get_character_count(letters: str):
    return None
