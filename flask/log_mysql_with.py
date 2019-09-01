from DBcm import UseDatabase
from time import sleep
from flask import Flask, render_template

app=Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB', }

def log_request(req: 'flask_request', res: str) -> None:
    '''журналирует веб запрос и возвращаемые результаты'''
    sleep (10)
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res, ))


def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select id, ts, phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('ID', 'Time', 'Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)




