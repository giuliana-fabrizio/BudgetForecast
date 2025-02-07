from queries.db_connexion import *

def getUser(email, password):
    db = get_db()
    return db.execute(
        'select * from customer where mail like ? and password like ?',
        [email, password]
    ).fetchone()