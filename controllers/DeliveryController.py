from flask import jsonify, request
from models.DeliveryModel import DeliveryModel

def listar_entregas():
    all_deliveries = DeliveryModel.selectAll()
    return jsonify(all_deliveries)

def adicionar_entregas():
    if request.is_jason:
        
        delivery = request.get_json()
        DeliveryModel.insert(delivery)
        return delivery, 201
    
    return {"erro": "A requisicao deve estar no formato JSON"}, 415

def entregas_por_codigo_rastreio(codigo):
    tracking_delivery = DeliveryModel.select_by_tracking_code(codigo)
    if len(tracking_delivery) == 0:
        return {'erro': 'Recurso não encontrado'}, 404
    return jsonify(tracking_delivery[0])

def entregas_por_cliente(documento):
    tracking_delivery = DeliveryModel.select_by_document(documento)
    if len(tracking_delivery) == 0:
        return {'erro': 'Recurso não encontrado'}, 404
    return jsonify(tracking_delivery[0])