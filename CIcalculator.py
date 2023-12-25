from tkinter import*
from math import*
 
def clear_all():
    p_f.delete(0,END)
    r_f.delete(0,END)
    t_f.delete(0,END)
    p_f.focus_set()
    Result.set("")
def calculate_ci():
    p=int(p_f.get())
    r=float(r_f.get())
    t=int(t_f.get())
    CI=p*(pow((1+r/100),t))-p
    CI=round(CI,2)
    Result.set(CI)
root=Tk()
root.configure(background='light green')
root.geometry("500x300")
root.title("compound intrest calculator")
Result=StringVar()

label1=Label(root,text="principle amt(rs):",fg='black')
label2=Label(root,text="Rate(%):",fg='black')
label3=Label(root,text="Time(years):",fg='black')
label4=Label(root,text="Compound Int:",fg='black')
label1.grid(row=1,column=0,padx=10,pady=10)
label2.grid(row=2,column=0,padx=10,pady=10)
label3.grid(row=3,column=0,padx=10,pady=10)
label4.grid(row=5,column=0,padx=10,pady=10)

p_f=Entry(root)
r_f=Entry(root)
t_f=Entry(root)
p_f.grid(row=1,column=1,padx=1,pady=10)
r_f.grid(row=2,column=1,padx=1,pady=10)
t_f.grid(row=3,column=1,padx=1,pady=10)

CInterest=Label(root,text=" ",textvariable=Result,fg='black',bg='red')
CInterest.grid(row=5,column=1)
button1=Button(root,text='submit',bg='blue',command=calculate_ci)
button2=Button(root,text='clear',bg='blue',command=clear_all)
button1.grid(row=4,column=1)
button2.grid(row=4,column=2)
root.mainloop()