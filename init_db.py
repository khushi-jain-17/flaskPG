import psycopg2

conn = psycopg2.connect(database="flask_pg", host="localhost", user="postgres", password="1234", port="5432")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS courses(id serial PRIMARY KEY, name varchar(100),fee integer,duration integer); ''')

cur.execute('''INSERT INTO COURSES(name, fee, duration) VALUES('python',7000,60),('java',5000,30),('react',3500,30); ''')
conn.commit()
cur.close()
conn.close()
