from flask import Flask
from routes.DeliveryRoutes import delivery_routes

app = Flask(__name__)
app.register_blueprint(delivery_routes, url_prefix = '/entregas')

if __name__ == '__main__':
    app.run()