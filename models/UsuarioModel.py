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
user = 'alex12345@gmail.com'
password = '12345'

cursor.execute("call public.prc_pjt_selecionar_usuario",[user,password])

rows = cursor.fetchall()

for row in rows:
    usuario = {
        "int_Usuario": int(row[0]),
	    "str_Nome": str(row[1])
    }


# Clean up

conn.commit()
cursor.close()
conn.close()



class UsuarioModel():
    def selectUsuario(str_Email, str_Senha):
        return usuario
    

