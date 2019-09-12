from flask import Flask, jsonify, request , render_template
import uuid
from flask_cors import CORS


# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__,
            static_folder = "./dist/",
            template_folder = "./dist")

app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

contador =   1 

@app.route("/")
def hello():
    return render_template("index.html")

# sanity check route

@app.route('/ping', methods=['GET'])
def ping_pong():
    global contador
    contador = contador + 1 
    mensagem = 'pong => {} '.format(contador)
    return jsonify(mensagem)


if __name__ == '__main__':
    app.run()