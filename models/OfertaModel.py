#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:project0000@db-project-aws-tera.czc7o1hghaix.us-east-2.rds.amazonaws.com/postgres'
#app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 

#db = SQLAlchemy(app)

import psycopg2

# Update connection string information

host = "db-project-aws-tera.czc7o1hghaix.us-east-2.rds.amazonaws.com"
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
cursor.execute("call public.prc_pjt_selecionar_oferta(null, null, null, null, null, null)")

rows = cursor.fetchall()

for row in rows:
    ofertas = {
        "str_produto": str(row[0]),
	    "str_produto_descricao": str(row[1]),
	    "str_marca": str(row[2]),
	    "str_imagem": str(row[3]),
	    "dec_valor": str(row[4]),
	    "dec_desconto": str(row[5])
    }


# Clean up

conn.commit()
cursor.close()
conn.close()



class OfertaModel():
    def selectAll():
        return ofertas
    

