from flask import Flask

def init_app(name=__name__):
    app = Flask(name)
    return app

def routers(app):
    @app.route('/')
    def hello_world():
        return 'Hello, World!'