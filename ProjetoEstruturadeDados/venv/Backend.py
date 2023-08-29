import sqlite3 as sql

class TransationObject():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransationObject.conn = sql.connect(TransationObject.database)
        TransationObject.cur = TransationObject.conn.cursor()
        TransationObject.connected = True

    def disconnect(self):
        TransationObject.conn.close()
        TransationObject.connected = False

    def execute(self, sql, parms= None):
        if TransationObject.connected:
            if parms == None:
                TransationObject.cur.execute(sql)
            else:
                TransationObject.cur.execute(sql, parms)
            return True
        else:
            return False
        
    def fetchall(self):
        return TransationObject.cur.fetchall()
    
    def persist(self):
        if TransationObject.connected:
            TransationObject.conn.commit()
            return True
        else:
            return False
        
    def initDB(self):
        trans = TransationObject()
        trans.connect()  
        trans.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        trans.persist()
        trans.disconnect()

    def insert(self, nome, sobrenome, email, cpf):
        trans = TransationObject()
        trans.connect()
        trans.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        trans.persist()
        trans.disconnect()

    def view(self):
        trans = TransationObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.fetchall()
        trans.disconnect()
        return rows
    
    def search(self, nome = "", sobrenome = "", email = "", cpf = ""):
        trans = TransationObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email, cpf))
        rows = trans.fetchall()
        trans.disconnect()
        return rows
    
    def delete(self, id):
        trans = TransationObject()
        trans.connect()
        trans.execute("DELETE FROM clientes WHERE id=?", (id,))
        trans.persist()
        trans.disconnect()

    def update(self, id, nome, sobrenome, email, cpf):
        trans = TransationObject()
        trans.connect()
        trans.execute("UPDATE clientes SET nome =?, sobrenome =?, email =?, cpf =? WHERE id =?",(nome, sobrenome, email, cpf, id))
        trans.persist()
        trans.disconnect()

    initDB()