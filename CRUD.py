import MySQLdb

def conexao():
    try:
        conn=MySQLdb.connect(user='root', db='items', password='98923', host='localhost')
        return conn
    except MySQLdb.Error():
        print('ERROR')

def listar():
    conn=conexao()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM produtos;')
    resul=cursor.fetchall()
    for c in resul:
        print(c)
    cursor.close()
    conn.close()


def atualizar():
    conn=conexao()
    cursor=conn.cursor()
    id=int(input('ID : '))
    nome=input('NOME : ')
    preco=int(input('PREÇO : '))
    estoque=int(input('ESTOQUE : '))
    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco='{preco}', estoque='{estoque}' WHERE ID='{id}';")
    conn.commit()
    if cursor.rowcount>0:
        print('SUCCESS')
    else:
        print('FAILED')
    cursor.close()
    conn.close()

def deletar():
    conn=conexao()
    cursor=conn.cursor()
    id=int(input('ID : '))
    cursor.execute(f'DELETE FROM produtos WHERE ID={id}')
    conn.commit()
    if cursor.rowcount>0:
        print('SUCCESS')
    else:
        print('FAILED')
    cursor.close()
    conn.close()

listar()
