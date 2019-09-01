from flask import Flask, render_template, request, session
from vsearch import search4letter
from log_mysql_with import log_request as lr, view_the_log as vl
from decorator_checker import check_logged_in
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError


app = Flask(__name__,)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Вот ваши результаты:'
    results = str(search4letter(phrase, letters))
    try:
        lr(request, results)
    except Exception as err:
        print('Ошибка при сохранении в базу: ', str(err))
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
def view_log() -> 'html':
    try:
        return vl()
    except ConnectionError as err:
        print('Ваша база данных подключена?: ', str(err))
    except CredentialsError as err:
        print('Ошибка логин/пароль. Error: ', str(err))
    except SQLError as err:
        print('Ваш запрос SQL правильный? Error:', str(err))
    except Exception as err:
        print('Ошибка типа: ', str(err))
    return render_template('viewlog.html',
                           the_title='!!! Не удалось подключиться к данным !!!',
                           the_row_titles=(),
                           the_data=(),)


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return render_template('viewlog.html',
                           the_title='Вы вошли в систему.',
                           the_row_titles=(),
                           the_data=(),)


@app.route('/logout')
def do_logout() -> str:
    try:
        session.pop('logged_in')
    except Exception:
        pass
    return render_template('viewlog.html',
                           the_title='Вы вышли из системы.',
                           the_row_titles=(),
                           the_data=(),)


app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':  # Вызов арр.run тепрерь производится только когда программа запускается непосредственно, а если импортируется как модуль, то рун не запускается
    app.run(debug=True)
