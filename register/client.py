from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import time
import time as tm
import datetime
import clientdatabase



root=Tk()
#if we want to remove the title bar
root.overrideredirect(1)
#root.title('                         CLIENT DATABASE MANAGEMENT SYSTEM')
root.geometry('450x730')
root.config(bg='skyblue')

def exit():
	exit=messagebox.askyesno('client management system','NOTICE :\nFIRST BE SURE YOU SAVED YOUR WORK!\nARE YOU SURE YOU WANT TO EXIT?')
	if exit>0:
		root.destroy()
		return
		
def clear():
	enuser.delete(0,END)
	enpassword.delete(0,END)
	enemail.delete(0,END)
	engender.delete(0,END)
	enaddress.delete(0,END)
	enhour.delete(0,END)
	enpayhour.delete(0,END)
	enpayment.delete(0,END)

def adddata():
	if user.get()=="" or password.get()=="" or email.get()=="" or gender.get()=="" or address.get()=="" or hour.get()=="" or payhour.get()=="" or payment.get()=="":
		messagebox.showerror('client management system','NOTICE : \nYOU MUST INCLUDE ALL FIELDS!')
		return

	clientdatabase.adddata(user.get(),password.get(),email.get(),gender.get(),address.get(),hour.get(),payhour.get(),payment.get())
	list.delete(0,END)
	list.insert(END,(user.get(),password.get(),email.get(),gender.get(),address.get(),hour.get(),payhour.get(),payment.get()))
	
def viewdata():
	list.delete(0,END)
	for row in clientdatabase.viewdata():
		list.insert(END,row)
		
		
def selectitem(event):
	global selecteditem
	index=list.curselection()[0]
	selecteditem=list.get(index)
	enuser.delete(0,END)
	enuser.insert(END,selecteditem[1])
	enpassword.delete(0,END)
	enpassword.insert(END,selecteditem[2])
	enemail.delete(0,END)
	enemail.insert(END,selecteditem[3])
	engender.delete(0,END)
	engender.insert(END,selecteditem[4])
	enaddress.delete(0,END)
	enaddress.insert(END,selecteditem[5])
	enhour.delete(0,END)
	enhour.insert(END,selecteditem[6])
	enpayhour.delete(0,END)
	enpayhour.insert(END,selecteditem[7])
	enpayment.delete(0,END)
	enpayment.insert(END,selecteditem[8])
	
	
def deldata():
	e=messagebox.askyesno('client management system','ARE YOU SURE YOU WANT TO DELETE THIS CLIENT?\nALL DATA FOR THIS CLIENT WILL BE GONE!!')
	if e>0:
		
		clientdatabase.deldata(selecteditem[0])
		enuser.delete(0,END)
		enpassword.delete(0,END)
		enemail.delete(0,END)
		engender.delete(0,END)
		enaddress.delete(0,END)
		enhour.delete(0,END)
		enpayhour.delete(0,END)
		enpayment.delete(0,END)
	else:
		return
	viewdata()
	

def update():
	clientdatabase.update(selecteditem[0],enuser.get(),enpassword.get(),enemail.get(),engender.get(),enaddress.get(),enhour.get(),enpayhour.get(),enpayment.get())
	viewdata()
	messagebox.showinfo('client management system',f'The client updated\n{user.get().upper()}\n{password.get()}\n{email.get()}\n{gender.get().upper()}\n{address.get()}\n{hour.get()}\n{payhour.get()}\n{payment.get()}')
	
	
	
	
def search():
			list.delete(0,END)
			for row in clientdatabase.search(user.get(),password.get(),email.get(),gender.get(),address.get(),hour.get(),payhour.get(),payment.get()):
				list.insert(END,row)
				
				
def cal():
	if enhour.get()=="" or enpayhour.get()=="":
		messagebox.showerror('client management system','NOTICE :\nYOU MUST INCLUDE HOURES AND PAY FOR HOURES\nTO USE THIS BUTTON   FOR   CALCULATE   PAYMENT!')
		return
	c=float(hour.get())*float(payhour.get())
	enpayment.delete(0,END)
	#enpayment.config(state=ENABLED)
	enpayment.insert(END,c)
	#enpayment.config(state=DISABLED)
#========================================

user=StringVar()
password=StringVar()
email=StringVar()
gender=StringVar()
address=StringVar()
hour=StringVar()
payhour=StringVar()
payment=StringVar()
#======================================
mainframe=Frame(root,bg='skyblue')
mainframe.grid()
frame1=LabelFrame(mainframe,bd=5)
frame1.grid()
lbltitle=Label(frame1,text='CLIENT DATABASE MANAGEMENT SYSTEM',font='arial 12 bold')
lbltitle.grid(row=0,column=0,columnspan=2,padx=8)
lbltime=Label(frame1,text="",font='arial 10 bold')
lbltime.grid(row=1,column=1)
def displaytime():
	currenttime=tm.strftime('%H:%M:%S %p')
	lbltime['text']=currenttime
	root.after(200,displaytime)

lbldate=Label(frame1,text="",font='arial 10 bold')
lbldate.grid(row=1,column=0)
def displaydate():
	localtime=time.asctime(time.localtime(time.time()))
	lbldate['text']=localtime

#======================================
frame2=LabelFrame(mainframe,bd=5,text='client info',bg='skyblue')
frame2.grid()

lbluser=Label(frame2,text='USER NAME',bg='skyblue')
lbluser.grid(row=0,column=0)

lbluser=Label(frame2,text='PASSWORD',bg='skyblue')
lbluser.grid(row=1,column=0)

lbluser=Label(frame2,text='E MAIL',bg='skyblue')
lbluser.grid(row=2,column=0)

lbluser=Label(frame2,text='GENDER',bg='skyblue')
lbluser.grid(row=3,column=0)

lbluser=Label(frame2,text='ADDRESS',bg='skyblue')
lbluser.grid(row=4,column=0)

lbluser=Label(frame2,text='HOUR',bg='skyblue')
lbluser.grid(row=5,column=0)

lbluser=Label(frame2,text='PAY HOUR',bg='skyblue')
lbluser.grid(row=6,column=0)

lbluser=Label(frame2,text='PAYMENT',bg='skyblue')
lbluser.grid(row=7,column=0,padx=18)


#======================================
enuser=Entry(frame2,textvariable=user,width=40)
enuser.grid(row=0,column=1,pady=2)
enpassword=Entry(frame2,textvariable=password,width=40)
enpassword.grid(row=1,column=1,pady=2)
enemail=Entry(frame2,textvariable=email,width=40)
enemail.grid(row=2,column=1,pady=2)
engender=Entry(frame2,textvariable=gender,width=40)
engender.grid(row=3,column=1,pady=2)
enaddress=Entry(frame2,textvariable=address,width=40)
enaddress.grid(row=4,column=1,pady=2)
enhour=Entry(frame2,textvariable=hour,width=40)
enhour.grid(row=5,column=1,pady=2)
enpayhour=Entry(frame2,textvariable=payhour,width=40)
enpayhour.grid(row=6,column=1,pady=2)
enpayment=Entry(frame2,textvariable=payment,width=40)
enpayment.grid(row=7,column=1,columnspan=4,pady=2)

frame21=LabelFrame(mainframe,bd=5,text='buttons')
frame21.grid()
btncal=Button(frame21,text='cal',command=cal,bg='skyblue')
btncal.grid(row=8,column=0)

btnadd=Button(frame21,text='add',command=adddata,bg='skyblue')
btnadd.grid(row=8,column=1)

btnview=Button(frame21,text='view',command=viewdata,bg='skyblue')
btnview.grid(row=8,column=2)

btndel=Button(frame21,text='del',command=deldata,bg='skyblue')
btndel.grid(row=8,column=3)

btnuptd=Button(frame21,text='uptd',command=update,bg='skyblue')
btnuptd.grid(row=8,column=4)

btnclr=Button(frame21,text='clr',command=clear,bg='skyblue')
btnclr.grid(row=8,column=5)

btnsear=Button(frame21,text='sear',command=search,bg='skyblue',highlightbackground='blue')
btnsear.grid(row=8,column=6)

btnexit=Button(frame21,text='exit',command=exit,bg='skyblue')
btnexit.grid(row=8,column=7)
#====================================
frame3=LabelFrame(mainframe,bd=5,text='view client',bg='skyblue')
frame3.grid()

scroll=ttk.Scrollbar(frame3)
scroll.pack(side=RIGHT,fill=Y)


scroll2=ttk.Scrollbar(frame3,orient='horizontal')
scroll2.pack(side='bottom',fill=X)

list=Listbox(frame3,width=50,height=20,yscrollcommand=scroll.set,xscrollcommand=scroll2.set,exportselection=0,selectmode='multiple')
list.pack(fill='both')
scroll.config(command=list.yview)
scroll2.config(command=list.xview)
list.bind('<<ListboxSelect>>',selectitem)



displaytime()
displaydate()
root.mainloop()