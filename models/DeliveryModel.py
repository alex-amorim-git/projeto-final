deliveries = [{"id": 1, "nome_cliente": "Allan", "documento": "1234567890", "tipo_pessoa": "PF", 
    "cep": "88108230", "nro": "SN", "complemento": "", "status_entrega": "pendente",
    "codigo_rastreio": "XZ2537485ABC", "id_pedido": 1, "id_loja": "200"},
    {"id": 2, "nome_cliente": "Alex", "documento": "745628443", "tipo_pessoa": "PF", 
    "cep": "70534672", "nro": "28", "complemento": "APTO230", "status_entrega": "saiu para entrega",
    "codigo_rastreio": "XZ2946384ABC", "id_pedido": 2, "id_loja": "250"}]

def next_id():
    return max(delivery["id"] for delivery in deliveries) + 1

class DeliveryModel():
    def selectAll():
        return deliveries
    
    def select(id):
        entrega = [delivery for delivery in deliveries if delivery["id"] == id]
        return entrega
 
    def select_by_tracking_code(codigo_rastreio):
        entrega = [delivery for delivery in deliveries if delivery["codigo_rastreio"] == codigo_rastreio]
        return entrega   
   
    def insert(delivery):
        delivery["id"] = next_id()
        deliveries.append(delivery)

    def select_by_document(documento):
        entrega = [delivery for delivery in deliveries if delivery["documento"] == documento]
        return entrega          