from flask import Blueprint
from controllers.OfertaController import listar_ofertas

oferta_routes = Blueprint('oferta_routes', __name__)
oferta_routes.route('/', methods=["GET"])(listar_ofertas)

