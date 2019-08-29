from flask import Flask, render_template, request, escape
from vsearch import search4letter
import mysql.connector

app = Flask(__name__,)


def log_request(req: 'flask_request', res: str) -> None:
    # определить параметры соединения
    dbconfig = { 'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB', }
    # установить соединение
    conn = mysql.connector.connect(**dbconfig)
    # создать курсор для отправки команд на сервер и получения результатов
    cursor = conn.cursor()
    # присвоить строку запроса переменной
    _SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
    # послать запрос серверу, подставив значения для всех аргументов (в кортеже)
    cursor.execute(_SQL, (req.form['phrase'],
                    req.form['letters'],
                    req.remote_addr,
                    req.user_agent.browser,
                    res,))
    # принудительно записать данные в таблицу
    conn.commit()
    # убрать за собой по окончании
    cursor.close()
    conn.close()

    """with open('flask/vsearch.log', 'a') as log:
        # Ч тобы узнать, что содержит тот или иной объект, нужно передать его встроенной функции dir, которая вернет список методов и атрибутов этого объекта
        print(req.form, req.remote_addr, req.user_agent,
              res, file=log, sep='|')"""


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
