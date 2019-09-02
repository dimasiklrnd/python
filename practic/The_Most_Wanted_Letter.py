'''Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.

Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".

Вх. данные: Текст для анализа, как строка.

Вых. данные: Наиболее частая буква, как строка.'''

from collections import Counter

def checkio(text: str) -> str:
    text = text.lower()
    forbidden = ('.', '?', '!', ':', ';', '-', '—', ' ', ',')

    text1 = "".join(
        symbol for symbol in text if symbol not in forbidden and not symbol.isdigit())

    text_list = [i for i in text1]

    text_list.sort()

    c = Counter(text_list)

    val = [v for v in c.values()]
    m = max(val)
    for i in text_list:
        if c[i] == m:
            return(i)


if __name__ == '__main__':
    print("Example:")
    print(checkio("12345,12345,12345 S 12345,12345"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
