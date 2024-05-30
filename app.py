import sys
sys.path.append("src")
sys.path.append("templates")
from flask import Flask

from view.web import vista_usuario

app = Flask(__name__)

app.register_blueprint(vista_usuario.blueprint)

if __name__ == '__main__':
    app.run()
