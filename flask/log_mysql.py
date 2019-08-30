# импортируем коннектор для майэскюэл
import mysql.connector


def log_request(req: 'flask_request', res: str) -> None:
    '''журналирует веб запрос и возвращаемые результаты'''

    # определить параметры соединения
    dbconfig = {'host': '127.0.0.1',
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

    # послать запрос серверу, подставив значения для всех аргументов (в кортеже) .
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
