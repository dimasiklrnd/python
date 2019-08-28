from flask import Flask, render_template, request
from vsearch import search4letter

app = Flask(__name__,)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Вот ваши результаты:'
    results = str(search4letter(phrase, letters))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Добро пожаловать на сайт search4letters!')


if __name__ == '__main__':  # Вызов арр.run тепрерь производится только когда программа запускается непосредственно, а если импортируется как модуль, то рун не запускается
    app.run(debug=True)
