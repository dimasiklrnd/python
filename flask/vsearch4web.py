from flask import Flask, render_template, request, escape, session
from vsearch import search4letter
import mysql.connector
from log_mysql_with import log_request as lr
from decorator_checker import check_logged_in
from DBcm import UseDatabase


app = Flask(__name__,)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Вот ваши результаты:'
    results = str(search4letter(phrase, letters))
    try:
        lr(request, results)
    except Exception as err:
        print('Ошибка типа: ', err)
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
@check_logged_in
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)




@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'Вы вошли в систему.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'Вы вышли из системы.'


app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':  # Вызов арр.run тепрерь производится только когда программа запускается непосредственно, а если импортируется как модуль, то рун не запускается
    app.run(debug=True)
