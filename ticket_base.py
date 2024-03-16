import sqlite3
def tb():
    conn=sqlite3.connect('reservation.db')
    cursor=conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tickets(
            ticket_id TEXT PRIMARY KEY,
            movie_name TEXT,
            ticket_qn INTEGER,
            ticket_price INTEGER)''')
    conn.commit()
    conn.close()
def insert_tc():
    conn=sqlite3.connect('Reservation.db')
    cursor=conn.cursor()
    tickets_data=[
        ('T1','Potrait of a lady on fire',100,50),
        ('T2','Handmaiden',100,60),
        ('T3','Call me by your name',100,70),
        ('T4','Royal Blue',100,40),
        ('T5','Sasaki To Miyano',100,80)
        ]
    cursor.executemany('INSERT OR IGNORE INTO Tickets(ticket_id,movie_name,ticket_qn,ticket_price) VALUES(?,?,?,?)', tickets_data)
    conn.commit()
    conn.close()
def get_tc():
    conn=sqlite3.connect('Reservation.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM Tickets')
    tickets=cursor.fetchall()
    conn.close()
    return tickets
def upd_qn(tid,reserved_qn):
    conn=sqlite3.connect('Reservation.db')
    cursor=conn.cursor()
    cursor.execute('UPDATE Tickets SET ticket_qn=ticket_qn-? WHERE ticket_id=?',(reserved_qn,tid))
    conn.commit()
    conn.close()
tb()
insert_tc()




