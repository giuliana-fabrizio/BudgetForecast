from queries.db_connexion import *

def getRevenues():
    db = get_db()
    return db.execute('select * from revenue;').fetchall()