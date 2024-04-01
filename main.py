from flask import Flask
import functions

# внутри main.py создаем все необходимые 
# объкты для запуска

def start_project():
    app=functions.init_app()
    functions.routers(app=app)
    app.run(host='0.0.0.0', port=8080)

# инициализационный скрипт
if __name__ == "__main__":
    start_project()
    