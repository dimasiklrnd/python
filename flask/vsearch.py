def search4letter(phrase: str, letters: str = 'aeiouy'):
    return set(phrase).intersection(set(letters))
