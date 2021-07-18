from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import time as tk
import Ariadatabase


root=Tk()
titlespace=" "
root.title(50*titlespace+"Aria Family Shoes")
root.geometry("450x700")
root.config(bg="green")

mainframe=Frame(root)
mainframe.grid()

def adddata():
	Ariadatabase.adddata(enname.get(),endays.get(),enpay1.get(),enjkol.get(),endaryafti.get(),enbaghi.get(),enadress.get(),enhesab.get())
	list.delete(0,END)
	list.insert(END,(enname.get(),endays.get(),enpay1.get(),enjkol.get(),endaryafti.get(),enbaghi.get(),enadress.get(),enhesab.get()))
	
	
def selectitem(event):
	global selecteditem
	index=list.curselection()[0]
	selecteditem=list.get(index)
	enname.delete(0,END)
	enname.insert(END,selecteditem[1])
	endays.delete(0,END)
	endays.insert(END,selecteditem[2])
	enpay1.delete(0,END)
	enpay1.insert(END,selecteditem[3])
	enjkol.delete(0,END)
	enjkol.insert(END,selecteditem[4])
	endaryafti.delete(0,END)
	endaryafti.insert(END,selecteditem[5])
	enbaghi.delete(0,END)
	enbaghi.insert(END,selecteditem[6])
	enadress.delete(0,END)
	enadress.insert(END,selecteditem[7])
	enhesab.delete(0,END)
	enhesab.insert(END,selecteditem[8])
	
def deldata():
	Ariadatabase.deldata(selecteditem[0])
	enname.delete(0,END)
	endays.delete(0,END)
	enpay1.delete(0,END)
	enjkol.delete(0,END)
	endaryafti.delete(0,END)
	enbaghi.delete(0,END)
	enadress.delete(0,END)
	enhesab.delete(0,END)
	viewdata()
	
def viewdata():
	list.delete(0,END)
	for row in Ariadatabase.viewdata():
		list.insert(END,row)
	
def exit():
	exit=messagebox.askyesno('ARIA FAMILY SHOES','ARE YOU SURE?')
	if exit >0:
		root.destroy()
		return
	
def update():
	Ariadatabase.update(selecteditem[0],enname.get(),endays.get(),enpay1.get(),enjkol.get(),endaryafti.get(),enbaghi.get(),enadress.get(),enhesab.get())
	viewdata()

def search():
	list.delete(0,END)
	for row in Ariadatabase.search(enname.get(),endays.get(),enpay1.get(),enjkol.get(),endaryafti.get(),enbaghi.get(),enadress.get(),enhesab.get()):
		list.insert(END,row)

def cal():
	enjkol.delete(0,END)
	enbaghi.delete(0,END)
	g=int(endays.get())*int(enpay1.get())
	enjkol.insert(END,g)
	d=int(endaryafti.get())
	f=g-d
	enbaghi.insert(END,f)
	
f1=LabelFrame(mainframe,width=450,height=200,bd=5,bg='green')
f1.grid()
lbltitle=Label(f1,text='        Aria Family Shoes       ',font=('arial',22,'bold'),bg='green')
lbltitle.grid()

f2=LabelFrame(mainframe,width=450,height=200,bd=5)
f2.grid()

lblname=Label(f2,text='NAME')
lblname.grid(row=0,column=0)
enname=Entry(f2)
enname.grid(row=0,column=1)

lbldays=Label(f2,text='DAYS')
lbldays.grid(row=0,column=3)
endays=Entry(f2)
endays.grid(row=0,column=4)

lblpay1=Label(f2,text='PAY1')
lblpay1.grid(row=1,column=0)
enpay1=Entry(f2)
enpay1.grid(row=1,column=1,pady=5)

lbljkol=Label(f2,text='JKOL')
lbljkol.grid(row=1,column=3)
enjkol=Entry(f2)
enjkol.grid(row=1,column=4)

lbldaryafti=Label(f2,text='DARYAFTI')
lbldaryafti.grid(row=2,column=0)
endaryafti=Entry(f2)
endaryafti.grid(row=2,column=1)

lblbaghi=Label(f2,text='BAGHI')
lblbaghi.grid(row=2,column=3)
enbaghi=Entry(f2)
enbaghi.grid(row=2,column=4)

lbladress=Label(f2,text='ADRESS')
lbladress.grid(row=3,column=0)
enadress=Entry(f2)
enadress.grid(row=3,column=1)

lblhesab=Label(f2,text='HESAB')
lblhesab.grid(row=3,column=3)
enhesab=Entry(f2)
enhesab.grid(row=3,column=4,pady=5)

f3=LabelFrame(mainframe,width=450,height=50,bd=5)
f3.grid()

f4=LabelFrame(mainframe,width=450,height=200,bd=5)
f4.grid()
#====list

scroll=ttk.Scrollbar(f4)
scroll.pack(side=RIGHT,fill=Y)


scroll2=ttk.Scrollbar(f4,orient='horizontal')
scroll2.pack(side='bottom',fill=X)

list=Listbox(f4,width=50,height=25,yscrollcommand=scroll.set,xscrollcommand=scroll2.set,exportselection=0)
list.pack(fill='both')
list.bind('<<ListboxSelect>>',selectitem)

#===btn
btnadd=Button(f3,text='ADD',command=adddata)
btnadd.grid(row=0,column=0)
btnexit=Button(f3,text='EXIT',command=exit)
btnexit.grid(row=0,column=6)
btnview=Button(f3,text='VIEW',command=viewdata)
btnview.grid(row=0,column=1)
btndel=Button(f3,text='DEL',command=deldata)
btndel.grid(row=0,column=2)
btnupdate=Button(f3,text='UPTD',command=update)
btnupdate.grid(row=0,column=3)
btnsearch=Button(f3,text='sear',command=search)
btnsearch.grid(row=0,column=4)
btncal=Button(f3,text='cal',command=cal)
btncal.grid(row=0,column=5)
scroll.config(command=list.yview)
scroll2.config(command=list.xview)
#list.insert(END,"NAME\t,HOURS\t,PAY1")



root.mainloop()