from flask import Flask, render_template
from routes.DeliveryRoutes import delivery_routes
from routes.ProdutoRoutes import produto_routes
from routes.OfertaRoutes import oferta_routes

app = Flask(__name__, static_folder='templates')
app.register_blueprint(delivery_routes, url_prefix = '/entregas')
app.register_blueprint(produto_routes, url_prefix = '/lista_produtos')
app.register_blueprint(oferta_routes, url_prefix = '/lista_ofertas')


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

@app.route('/login')
def login():
  return render_template('login.html')

@app.route("/logon/", methods=['POST'])
def logon():
    #ogon code
    logon_message = "Moving Forward..."
    return render_template('index.html', logon_message=logon_message)

if __name__ == '__main__':
    app.run()