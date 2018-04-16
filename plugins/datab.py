import mysql.connector

def datab_init():
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    return cursor

def datab_create(msg, cursor):
    cursor.execute("SELECT table_name FROM information_schema.TABLES WHERE table_name ='%s';" %(msg['chat']['title']))
    if cursor.fetchall()[0][0] == msg['chat']['title'] or msg['chat']['type'] != 'supergroup':
        return
    else:
        cursor.ecxecute("cursor.execute('create table %s (id varchar(20) primary key, name varchar(20)), text varchat(256)')" %(msg['chat']['title']))
if __name__ =='__main__':
    datab_init()
