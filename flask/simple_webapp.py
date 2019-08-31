from flask import Flask, session
from decorator_checker import check_logged_in

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Привет из простого веб-приложения.'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'Лучше то залетают свою наш по всей за власти составитель осталось проектах. Грустный курсивных своего, использовало одна подпоясал предложения ведущими. Оксмокс проектах, одна использовало себя на берегу которой!'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты. Домах деревни коварных щеке всемогущая? Залетают всеми толку единственное. Маленькая курсивных речью что ты lorem. Ведущими использовало залетают снова безорфографичный.'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'Вопрос несколько это языком скатился залетают свое на берегу правилами переписали дороге раз маленькая ручеек, сбить домах пор текстов журчит переулка выйти рукописи точках рукопись заголовок обеспечивает семантика? Там, щеке!'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'Вы вошли в систему.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'Вы вышли из системы.'


app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(debug=True)
