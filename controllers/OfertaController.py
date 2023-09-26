from flask import jsonify, request
from models.OfertaModel import OfertaModel

def listar_ofertas():
    all_ofertas = OfertaModel.selectAll()
    return jsonify(all_ofertas)


