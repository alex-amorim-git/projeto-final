from flask import Blueprint
from controllers.DeliveryController import listar_entregas, adicionar_entregas, entregas_por_cliente, entregas_por_codigo_rastreio

delivery_routes = Blueprint('delivery_routes', __name__)
delivery_routes.route('/', methods=["GET"])(listar_entregas)
delivery_routes.route('/', methods=["POST"])(adicionar_entregas)
delivery_routes.route('/cliente/<documento>', methods=["GET"])(entregas_por_cliente)
delivery_routes.route('/<codigo>', methods=["GET"])(entregas_por_codigo_rastreio)