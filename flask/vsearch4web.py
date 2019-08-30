from flask import Flask, render_template, request, escape
from vsearch import search4letter
from log_mysql import log_request

app = Flask(__name__,)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Вот ваши результаты:'
    results = str(search4letter(phrase, letters))
    log_request(request, results)
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


@app.route('/viewlog')
def view_the_log() -> str:
    contents = []
    with open('flask/vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    # Если передать функции escape строку cодержащую какие-либо специальные символы HTML, она заменит их
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':  # Вызов арр.run тепрерь производится только когда программа запускается непосредственно, а если импортируется как модуль, то рун не запускается
    app.run(debug=True)
