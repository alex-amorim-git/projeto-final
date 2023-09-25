from flask import Blueprint
from controllers.ProdutoController import listar_produtos

produto_routes = Blueprint('produto_routes', __name__)
produto_routes.route('/', methods=["GET"])(listar_produtos)

