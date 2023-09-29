from flask import Flask, request, redirect

app = Flask(__name__)

# Импортируем необходимые модули для работы с базой данных
from flask_sqlalchemy import SQLAlchemy

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Модель данных для страниц
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Page {self.id}>'

# Создаем таблицу в базе данных (если она еще не создана)


# Главная страница
@app.route('/')
def index():
    return 'Welcome to the Flask app!'

# Страница просмотра и удаления
@app.route('/look')
def look():
    page_id = request.args.get('look')
    page = Page.query.get(page_id)

    if page:
        return f'''
            <h1>Page {page.id}</h1>
            <p>{page.text}</p>
            <form method="POST" action="/delete">
                <input type="hidden" name="page_id" value="{page.id}">
                <input type="submit" value="Delete">
            </form>
        '''
    else:
        return 'Page not found'

# Страница добавления
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        text = request.form.get('text')

        # Получаем минимальное доступное id для новой страницы
        min_id = db.session.query(db.func.min(Page.id)).scalar()
        page_id = min_id - 1 if min_id > 0 else 1

        # Создаем новую страницу
        page = Page(id=page_id, text=text)
        db.session.add(page)
        db.session.commit()

        # Перенаправляем на страницу просмотра новой страницы
        return redirect(f'/look?look={page_id}')
    
    return '''
        <form method="POST" action="/add">
            <textarea name="text"></textarea><br>
            <input type="submit" value="Add">
        </form>
    '''

# Страница удаления
@app.route('/delete', methods=['POST'])
def delete():
    page_id = request.form.get('page_id')
    page = Page.query.get(page_id)

    if page:
        db.session.delete(page)
        db.session.commit()
        return 'Page deleted'
    else:
        return 'Page not found'

if __name__ == '__main__':
    app.run()
