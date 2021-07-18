from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import ariadatabase
import clientdatabase
import time
import datetime
import time as tm
import math



def regist():
	if enuser.get()== 'morteza' and enpass.get()=='8811':
		btn1.config(state=NORMAL)
		btn2.config(state=NORMAL)
		
	elif enuser.get()=='morteza11'and enpass.get()=='881122':
		btn1.config(state=NORMAL)
		
	elif enuser.get()=='morteza12'and enpass.get()=='8811223':
		btn2.config(state=NORMAL)
	else:
		messagebox.showerror('REGISTRATION','INVALID USERNAME & PASSWORD!!!!')
		return
		
		
root=Tk()
root.geometry('300x300')
root.config(bg='gray')
titlespace=" "
root.title(50*titlespace+'REGISTRATION')
lbluser=Label(root,text='USER NAME : ',bg='gray')
lbluser.grid(row=0,column=0)
enuser=Entry(root)
enuser.grid(row=0,column=1)

lblpass=Label(root,text='PASSWORD : ',bg='gray')
lblpass.grid(row=1,column=0)
enpass=Entry(root)
enpass.grid(row=1,column=1)

def newwindow():
	root=Tk()
	titlespace=" "
	root.title(50*titlespace+"Aria Family Shoes")
	root.geometry("450x700")
	root.config(bg="green")

	mainframe=Frame(root)
	mainframe.grid()

	def adddata():
		ariadatabase.adddata(enname.get(),endays.get(),enpay1.get(),enjkol.get(),endaryafti.get(),enbaghi.get(),enadress.get(),enhesab.get())
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
		ariadatabase.deldata(selecteditem[0])
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
		for row in ariadatabase.viewdata():
			list.insert(END,row)
	
	def exit():
		exit=messagebox.askyesno('ARIA FAMILY SHOES','ARE YOU SURE?')
		if exit >0:
			root.destroy()
			return
	
	def update():
		ariadatabase.update(selecteditem[0],enname.get(),endays.get(),enpay1.get(),enjkol.get(),endaryafti.get(),enbaghi.get(),enadress.get(),enhesab.get())
		viewdata()

	def search():
		list.delete(0,END)
		for row in ariadatabase.search(enname.get(),endays.get(),enpay1.get(),enjkol.get(),endaryafti.get(),enbaghi.get(),enadress.get(),enhesab.get()):
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
	
	
def newwindow1():
	root=Tk()
	root.title('                         CLIENT DATABASE MANAGEMENT SYSTEM')
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
		#if user.get()=="" or password.get()=="" or email.get()=="" or gender.get()=="" or address.get()=="" or hour.get()=="" or payhour.get()=="" or payment.get()=="":
			#messagebox.showerror('client management system','NOTICE : \nYOU MUST INCLUDE ALL FIELDS!')
			#return

		clientdatabase.adddata(enuser.get(),enpassword.get(),enemail.get(),engender.get(),enaddress.get(),enhour.get(),enpayhour.get(),enpayment.get())
		list.delete(0,END)
		list.insert(END,(enuser.get(),enpassword.get(),enemail.get(),engender.get(),enaddress.get(),enhour.get(),enpayhour.get(),enpayment.get()))
	
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
		messagebox.showinfo('client management system',f'The client updated\n{enuser.get().upper()}\n{enpassword.get()}\n{enemail.get()}\n{engender.get().upper()}\n{enaddress.get()}\n{enhour.get()}\n{enpayhour.get()}\n{enpayment.get()}')
	
	
	
	
	def search():
				list.delete(0,END)
				for row in clientdatabase.search(enuser.get(),enpassword.get(),enemail.get(),engender.get(),enaddress.get(),enhour.get(),enpayhour.get(),enpayment.get()):
					list.insert(END,row)
				
				
	def cal():
		if enhour.get()=="" or enpayhour.get()=="":
			messagebox.showerror('client management system','NOTICE :\nYOU MUST INCLUDE HOURES AND PAY FOR HOURES\nTO USE THIS BUTTON   FOR   CALCULATE   PAYMENT!')
			return
		c=float(enhour.get())*float(enpayhour.get())
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
	hour=IntVar()
	payhour=IntVar()
	payment=IntVar()
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

	btnsear=Button(frame21,text='sear',command=search,bg='skyblue')
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

	
	
btn=Button(root,text='REGISTRATION',command=regist,width=30)
btn.grid(row=2,column=0,columnspan=2,pady=20)

btn1=Button(root,text='ARIA SHOES',command=newwindow,state=DISABLED,width=30)
btn1.grid(row=3,column=0,columnspan=2,pady=10)

btn2=Button(root,text='CLIENT MANAGEMENT SYSTEM',command=newwindow1,state=DISABLED,width=30)
btn2.grid(row=4,column=0,columnspan=2,pady=10)
def unlogin():
	enuser.delete(0,END)
	enpass.delete(0,END)
	btn1.config(state=DISABLED)
	btn2.config(state=DISABLED)
btnunlogin=Button(root,text='UN LOGIN',width=30,command=unlogin)
btnunlogin.grid(row=5,column=0,columnspan=2,pady=10)
btn3=Button(root,text='EXIT',command=exit,width=30)
btn3.grid(row=6,column=0,columnspan=2,pady=10)


	






root.mainloop()