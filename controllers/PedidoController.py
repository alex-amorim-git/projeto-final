from flask import jsonify, request
from models.PedidoModel import PedidoModel

def pedido_por_id(id):
    id_pedido = PedidoModel.selectPedidoId(id)
    if len(id_pedido) == 0:
        return {'erro': 'Não encontrado'}, 404
    return jsonify(id_pedido[0])