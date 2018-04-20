import mysql.connector

def datab_init():
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    return cursor

def datab_create(msg, cursor):
    cursor.execute("SELECT table_name FROM information_schema.TABLES WHERE table_name ='%s';" %(msg['chat']['title']))
    if cursor.fetchall()[0][0] == msg['chat']['title'] or msg['chat']['type'] != 'supergroup':
        return
    else:;
        cursor.ecxecute("cursor.execute('create table %s (username varchar, first_name varchat, tg id text varchat')" %(msg['chat']['title']))

def datab_add(msg, cursor):
    cursor.execute('insert into %s (username, first_name, tg_id, text) values (%s, %s)', ['1', 'Michael'])
if __name__ =='__main__':
    datab_init()
