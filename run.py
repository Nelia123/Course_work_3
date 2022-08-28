from flask import Flask
from main.views import main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)

app.config['JSON_AS_ASCII'] = False # TO DO


@app.errorhandler(404)
def page_error_404(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере ошибка - {error}", 500


if __name__ == "__main__":
    app.run()