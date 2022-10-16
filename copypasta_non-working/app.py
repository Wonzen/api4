from flask import Flask

from copypasta.routes import users_api

app = Flask(__name__)


@app.route('/')
def post_users():
    pass


if __name__ == '__main__':
    app.register_blueprint(users_api.main, url_prefix='/api/user_api')
    app.run()
