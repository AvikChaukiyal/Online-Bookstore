import os
import mysql.connector 

conn =  mysql.connector.connect(
        host="localhost",
        database="flask_db",
        user='root',
        password='avik1234')


cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS books;')

cur.execute('''
            CREATE TABLE books (
                                 id serial PRIMARY KEY,
                                 title varchar (150) NOT NULL,
                                 author varchar (150) NOT NULL,
                                 pages_num integer NOT NULL,
                                 review varchar(150),
                                 date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                 );
            '''
                                 )

conn.commit()

cur.close()
conn.close()

