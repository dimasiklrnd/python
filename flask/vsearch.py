def search4letter(phrase: str, letters: str):
    s = sorted(set(phrase).intersection(set(letters)))
    p = ''
    for i in s:
        p += str(i) + ' '
    return p
