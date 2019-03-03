import psycopg2
import json

#TODO Support DB configuration reading from config text file!
# CONSTS
DEV = False
if DEV:
    DB_NAME = "barber_shop"
    DB_USER = "postgres"
    DB_PWD = ""
    DB_HOST = "localhost"
    DB_PORT = "5432"
else:
    DB_NAME = "sampledb"
    DB_USER = "userQWI"
    DB_PWD = "Ryb8Nb1qHlqgAhVR"
    DB_HOST = "postgresql-leya.1d35.starter-us-east-1.openshiftapps.com"
    DB_PORT = "5432"    
    
# Get DB connection
def get_db_conn():
    try:
        conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_USER, host = DB_HOST, port = DB_PORT)
        print "Opened database successfully"
        return conn
    except BaseException as e:
        print "Exception of DB connection creation: \n\t" + str(e)

def get_workers_json():
    conn = get_db_conn()
    if conn is None:
        return ""
    
    users = []
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name, surname, login, role, active from \"User\" where deleted = false")
        rows = cur.fetchall()
        for row in rows:
            user = {}
            user['id'] = row[0]
            user['name'] = row[1]
            user['surname'] = row[2]
            user['login'] = row[3]
            user['role'] = row[4]
            user['active'] = row[5]
            users.append(user)
        
        print "Operation done successfully";
    finally:
        conn.close()
        return json.dumps(users)