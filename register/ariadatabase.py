import sqlite3


def dataentry():
	con=sqlite3.connect('ariadataform.db')
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS ariadataform  (id INTEGER PRIMARY KEY,enname text, endays text,enpay1 text,enjkol text,endaryafti text,enbaghi text,enadress text,enhesab text)")
	con.commit()
	con.close()
	
	
def  adddata(enname,endays,enpay1,enjkol,endaryafti,enbaghi,enadress,enhesab):
	con=sqlite3.connect('ariadataform.db')
	cur=con.cursor()
	cur.execute("INSERT INTO ariadataform VALUES(NULL,?,?,?,?,?,?,?,?)",(enname,endays,enpay1,enjkol,endaryafti,enbaghi,enadress,enhesab))
	con.commit()
	con.close()
	
	
def viewdata():
	con=sqlite3.connect('ariadataform.db')
	cur=con.cursor()
	cur.execute("SELECT * FROM ariadataform")
	rows=cur.fetchall()
	con.close()
	return rows
	
def deldata(id):
		con=sqlite3.connect('ariadataform.db')
		cur=con.cursor()
		cur.execute("DELETE FROM ariadataform WHERE id=?",(id,))
		con.commit()
		con.close()
		
def update(id,enname="",endays="",enpay1="",enjkol="",endaryafti="",enbaghi="",enadress="",enhesab=""):
		con=sqlite3.connect('ariadataform.db')
		cur=con.cursor()
		cur.execute("UPDATE ariadataform SET enname=?, endays=?,enpay1=?,enjkol=?,endaryafti=?,enbaghi=?,enadress=?,enhesab=? WHERE id=?",(enname,endays,enpay1,enjkol,endaryafti,enbaghi,enadress,enhesab,id))
		con.commit()
		con.close()
def search(enname="",endays="",enpay1="",enjkol="",endaryafti="",enbaghi="",enadress="",enhesab=""):
	con=sqlite3.connect('ariadatabase.db')
	cur=con.cursor()
	cur.execute("SELECT * FROM ariadataform WHERE enname=?,endays=?,enpay1=?,enjkol=?,endaryafti=?,enbaghi=?,enadress=?,enhesab=?",(enname,endays,enpay1,enjkol,endaryafti,enbaghi,enadress,enhesab))
	rows=cur.fetchall()
	con.close()
	return rows

		
				
						
										
dataentry()	