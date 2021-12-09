from imc import database, views
from flask import Flask

app = Flask('__name__')

database.init_app(app)
views.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        database.db.create_all()

    app.run(debug=False)