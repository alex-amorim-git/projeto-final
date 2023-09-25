from flask import jsonify, request
from models.ProdutoModel import ProdutoModel

def listar_produtos():
    all_produtos = ProdutoModel.selectAll()
    return jsonify(all_produtos)


