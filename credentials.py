import pyodbc

def credenciais_banco():
# Configuração da conexão com o banco de dados
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'Server=187.121.151.19;' 
        'Database=DB_BASE;'
        'UID=user_allnexus;'
        'PWD=uKl041xn8HIw0WF;'
        'TrustServerCertificate=yes;'
    )
    return conn

# def credenciais_banco():
# # Configuração da conexão com o banco de dados
#     conn = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};'
#         'Server=187.121.151.19;' 
#         'Database=DB_BASE;'
#         'UID=user_allnexus;'
#         'PWD=uKl041xn8HIw0WF;'
#     )
#     return conn