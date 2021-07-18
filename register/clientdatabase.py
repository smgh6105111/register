import sqlite3

def dataentry():
    con=sqlite3.connect('clientdata4.db')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS clientdata4(id INTEGER PRIMARY KEY, user text, password text,email text,gender text,address text,hour text,payhour text, payment text) ')
    con.commit()
    con.close()
    
def adddata(user,password,email,gender,address,hour,payhour,payment):
    con=sqlite3.connect('clientdata4.db')
    cur=con.cursor()
    cur.execute('INSERT INTO clientdata4 VALUES(NULL,?,?,?,?,?,?,?,?)',(user,password,email,gender,address,hour,payhour,payment))
    con.commit()
    con.close() 
    
        
def viewdata():
        con=sqlite3.connect('clientdata4.db')
        cur=con.cursor()
        cur.execute('SELECT * FROM clientdata4')
        rows=cur.fetchall()
        con.close()
        return rows
    
        
def deldata(id):
		con=sqlite3.connect('clientdata4.db')
		cur=con.cursor()
		cur.execute("DELETE FROM clientdata4 WHERE id=?",(id,))
		con.commit()
		con.close()
		
		    
def update(id,enuser="",enpassword="",enemail="",engender="",enaddress="",enhour="",enpayhour="",enpayment=""):
		con=sqlite3.connect('clientdata4.db')
		cur=con.cursor()
		cur.execute("UPDATE clientdata4 SET user=?, password=?,email=?,gender=?,address=?,hour=?,payhour=?,payment=? WHERE id=?",(enuser,enpassword,enemail,engender,enaddress,enhour,enpayhour,enpayment,id))
		con.commit()
		con.close()    
    
    
def search(enuser="",enpassword="",enemail="",engender="",enaddress="",enhour="",enpayhour="",enpayment=""):
	con=sqlite3.connect('clientdata4.db')
	cur=con.cursor()
	cur.execute("SELECT * FROM clientdata4 WHERE user=? or password=? or email=? or gender=? or address=? or hour=? or payhour=? or payment=?",(enuser,enpassword,enemail,engender,enaddress,enhour,enpayhour,enpayment))
	rows=cur.fetchall()
	con.close()
	return rows
dataentry()