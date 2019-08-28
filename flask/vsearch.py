def search4letter(phrase: str, letters: str = 'aeiouy'):
    s = set(phrase).intersection(set(letters))
    p = ''
    for i in s:
        p += str(i) + ' '
    return p
