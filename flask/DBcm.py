import mysql.connector


class UseDatabase:

    def __init__(self, config: dict):
        self.configuration = config

    def __enter__(self) -> 'cursor':
        # установить соединение
        self.conn = mysql.connector.connect(**self.configuration)
        # создать курсор для отправки команд на сервер и получения результатов
        return self.conn.cursor()

    def __exit__(self, exec_type, exc_value, exc_trace):
        # принудительно записать данные в таблицу
        self.conn.commit()
        # убрать за собой по окончании
        self.conn.cursor().close()
        self.conn.close()
