import sqlite3

# Conectar ao banco de dados (ou criá-lo se não existir)
conn = sqlite3.connect('clientes.db')

# Criar um cursor
cursor = conn.cursor()

# Criar a tabela de clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
''')

# Salvar as alterações
conn.commit()

# Fechar a conexão
conn.close()
