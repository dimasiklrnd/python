import mysql.connector

class UseDatabase:

    def __init__(self, config: dict):
        self.configuration = config

    def __enter__(self) -> 'cursor':
        # установить соединение
        self.conn = mysql.connector.connect(**self.configuration)
        # создать курсор для отправки команд на сервер и получения результатов
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exec_type, exc_value, exc_trace):
        # принудительно записать данные в таблицу
        self.conn.commit()
        # убрать за собой по окончании
        self.cursor.close()
        self.conn.close()
