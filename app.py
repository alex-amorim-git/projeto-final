from flask import Flask, render_template
from routes.DeliveryRoutes import delivery_routes

app = Flask(__name__, static_folder='templates')
app.register_blueprint(delivery_routes, url_prefix = '/entregas')

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
    app.run()