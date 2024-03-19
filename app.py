from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

clientes_cadastrados = {}  # Definição da variável global para armazenar os clientes cadastrados

class ItemMenu:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Definição de outras classes e lógica de negócio aqui...

menu = [
    ItemMenu("Hamburguer", 10.0),
    ItemMenu("Batata Frita", 5.0),
    ItemMenu("Refrigerante", 3.0)
]

class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        
class Cozinha:
    def __init__(self):
        self.pedidos_em_espera = []

    def receber_pedido(self, pedido):
        self.pedidos_em_espera.append(pedido)
        
@app.route('/')
def show_menu():
    return render_template('menu.html', menu=menu)

cozinha = Cozinha()

@app.route('/fazer_pedido', methods=['POST'])
def fazer_pedido():
    nome_cliente = request.form['nome']
    endereco_cliente = request.form['endereco']
    telefone_cliente = request.form['telefone']
    itens_pedido = request.form.getlist('itens')
    
    # Conectar ao banco de dados
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    # Verificar se o cliente já está cadastrado
    cursor.execute("SELECT id FROM clientes WHERE telefone=?", (telefone_cliente,))
    cliente_existente = cursor.fetchone()
    
    if not cliente_existente:
        # Se o cliente não existir, inserir no banco de dados
        cursor.execute("INSERT INTO clientes (nome, endereco, telefone) VALUES (?, ?, ?)",
                       (nome_cliente, endereco_cliente, telefone_cliente))
        conn.commit()
    
    # Fechar a conexão com o banco de dados
    conn.close()
    
    pedido = Pedido(Cliente)
    
    for item_id in itens_pedido:
        item = menu[int(item_id)]
        pedido.adicionar_item(item)
    
    cozinha.receber_pedido(pedido)
    
    return redirect(url_for('show_menu'))





    
    # Aqui você precisa definir a lógica para receber o pedido na cozinha
    # Se você tiver uma classe "Cozinha" e um método "receber_pedido", você precisará ajustar isso
    
    return redirect(url_for('show_menu'))

if __name__ == '__main__':
    app.run(debug=True)
