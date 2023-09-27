import psycopg2

# Update connection string information

host = "db2-project-aws-tera.czc7o1hghaix.us-east-2.rds.amazonaws.com"
dbname = "postgres"
user = "postgres"
password = "project0000"
sslmode = "require"

# Construct connection string

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("call public.prc_pjt_selecionar_pedido(1,null, null, null, null, null, null, null, null)")

rows = cursor.fetchall()

for row in rows:
    pedidos = {
        	"int_pedido": str(row[0]), 
	        "str_produto": str(row[1]),
	        "str_produto_descricao": str(row[2]),
	        "str_marca": str(row[3]),
	        "str_imagem": str(row[4]),
	        "dec_valor": str(row[5]),
	        "dec_desconto": str(row[6]),
	        "str_status": str(row[7])
    }

# Clean up

conn.commit()
cursor.close()
conn.close()



class PedidoModel():
    def selectPedidoId(id):
        return pedidos
    



