from flask import Flask, render_template
from routes.DeliveryRoutes import delivery_routes

app = Flask(__name__, static_folder='templates')
app.register_blueprint(delivery_routes, url_prefix = '/entregas')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/principal')
def principal():
  return render_template('index.html')

@app.route('/carrinho')
def carrinho():
  return render_template('carrinho.html')

@app.route('/cadastro')
def cadastro():
  return render_template('cadastro.html')

@app.route('/ofertas')
def ofertas():
  return render_template('ofertas.html')

@app.route('/acessorios')
def acessorios():
  return render_template('acessorios.html')

@app.route('/sobre')
def sobre():
  return render_template('sobre.html')

@app.route('/contato')
def contato():
  return render_template('contato.html')

if __name__ == '__main__':
    app.run()