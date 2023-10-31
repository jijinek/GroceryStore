import mysql.connector 
__cnx=None

def get_sql_connection():
    print("opening my sql connnection")
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='rootroot',
                                  host='127.0.0.1', database='grocery_store')
    return __cnx
     