# импорт драйвера базы данных
import mysql.connector

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

# послать запрос серверу, подставив значения для всех аргументов (в кортеже)
cursor.execute(_SQL, ('galaxy', 'xyz', '127.0.0.1', 'Opera', "{'x', 'y'}"))

# принудительно записать данные в таблицу
conn.commit()

# получить только что записанные данные из таблицы и отобразить их строку за строкой
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)

# убрать за собой по окончании
cursor.close()
conn.close()
