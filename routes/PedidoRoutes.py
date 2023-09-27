from flask import Blueprint
from controllers.PedidoController import pedido_por_id

pedido_routes = Blueprint('pedido_routes', __name__)
pedido_routes.route('/<id>', methods=["GET"])(pedido_por_id)