from DBcm import UseDatabase
from flask import Flask, render_template

app=Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB', }

def log_request(req: 'flask_request', res: str) -> None:
    '''журналирует веб запрос и возвращаемые результаты'''

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




