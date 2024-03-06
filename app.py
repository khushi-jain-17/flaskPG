import psycopg2
from flask import Flask, render_template, request, redirect, url_for, jsonify  

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database="flask_pg", host="localhost", user="postgres", password="1234", port="5432")
    return conn


@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(''' SELECT * FROM courses ORDER BY id''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/create', methods=['POST'])
def create():
    conn = db_conn()
    cur = conn.cursor()
    data=request.json
    name=data.get("name")
    fee=data.get("fee")
    duration=data.get("duration")
    
    # name = request.form['name']
    # fee = request.form['fee']
    # duration = request.form['duration']
    
    cur.execute('''INSERT INTO courses (name,fee,duration) VALUES(%s,%s,%s)''',(name,fee,duration))
    conn.commit()
    cur.close()
    conn.close()
    # return redirect(url_for('index'))
    return jsonify(data)

@app.route('/update', methods=['POST'])
def update():
    conn = db_conn()
    cur = conn.cursor()
    
    name = request.form['name']
    fee = request.form['fee']
    duration = request.form['duration']
    id = request.form['id']
    
    cur.execute(
        '''UPDATE courses SET name=%s, fee=%s, duration=%s WHERE id=%s''', (name, fee, duration, id,)
    )
    
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    conn = db_conn()
    cur = conn.cursor()
    
    id = request.form['id']
    
    cur.execute('''DELETE FROM courses where id=%s''',(id,))
    
    conn.commit()
    cur.close()
    conn.close()
    
    return redirect(url_for('index'))

    
    
    