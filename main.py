import math
from Tkinter import*
from tkMessageBox import*
root=Tk()
root.title('Scientific Calculator v1.0')


def add_num(x):
    e1.insert(16,x)
def result(y):
    e1.delete(0,END)
    e1.insert(16,y)

def factorial(x):
    f=1
    while x>0:
        f=f*x
        x=x-1
    return f

    
    
e1=Entry(root,width=16,font="Arial 30 bold",bg="GREY",justify="right")
e1.grid(row=0,column=0,columnspan=5)
pi=3.14

Button(root,text='7',width=10,height=5,bg="WHITE",command=lambda:add_num('7')).grid(row=1,column=0,sticky=E+W+N+S)
Button(root,text='8',width=10,height=5,bg="WHITE",command=lambda:add_num('8')).grid(row=1,column=1,sticky=E+W+N+S)
Button(root,text='9',width=10,height=5,bg="WHITE",command=lambda:add_num('9')).grid(row=1,column=2,sticky=E+W+N+S)

Button(root,text='sq. root',width=10,height=5,bg="ORANGE",command=lambda:result(((float)(e1.get()))**0.5)).grid(row=1,column=4,sticky=E+W+N+S)
Button(root,text='C',width=10,height=5,bg="ORANGE",command=lambda:e1.delete(0,END)).grid(row=1,column=3,sticky=E+W+N+S)

Button(root,text='4',width=10,height=5,bg="WHITE",command=lambda:add_num('4')).grid(row=2,column=0,sticky=E+W+N+S)
Button(root,text='5',width=10,height=5,bg="WHITE",command=lambda:add_num('5')).grid(row=2,column=1,sticky=E+W+N+S)
Button(root,text='6',width=10,height=5,bg="WHITE",command=lambda:add_num('6')).grid(row=2,column=2,sticky=E+W+N+S)
Button(root,text='+',width=10,height=5,bg="ORANGE",command=lambda:add_num('+')).grid(row=2,column=3,sticky=E+W+N+S)
Button(root,text='cube root',width=10,height=5,bg="ORANGE",command=lambda:result(((float)(e1.get()))**0.3333333333333)).grid(row=2,column=4,sticky=E+W+N+S)

Button(root,text='1',width=10,height=5,bg="WHITE",command=lambda:add_num('1')).grid(row=3,column=0,sticky=E+W+N+S)
Button(root,text='2',width=10,height=5,bg="WHITE",command=lambda:add_num('2')).grid(row=3,column=1,sticky=E+W+N+S)
Button(root,text='3',width=10,height=5,bg="WHITE",command=lambda:add_num('3')).grid(row=3,column=2,sticky=E+W+N+S)
Button(root,text='-',width=10,height=5,bg="ORANGE",command=lambda:add_num('-')).grid(row=3,column=3,sticky=E+W+N+S)
Button(root,text='square',width=10,height=5,bg="ORANGE",command=lambda:result(((float)(e1.get()))**2)).grid(row=3,column=4,sticky=E+W+N+S)

Button(root,text='0',width=10,height=5,bg="WHITE",command=lambda:add_num('0')).grid(row=4,column=0,sticky=E+W+N+S)
Button(root,text='.',width=10,height=5,bg="WHITE",command=lambda:add_num('.')).grid(row=4,column=1,sticky=E+W+N+S)
Button(root,text='=',width=10,height=5,bg="WHITE",command=lambda:result(((float)(eval(e1.get()))))).grid(row=4,column=2,sticky=E+W+N+S)
Button(root,text='*',width=10,height=5,bg="ORANGE",command=lambda:add_num('*')).grid(row=4,column=3,sticky=E+W+N+S)
Button(root,text='cube',width=10,height=5,bg="ORANGE",command=lambda:result(((float)(e1.get()))**3)).grid(row=4,column=4,sticky=E+W+N+S)

Button(root,text='pi',width=10,height=5,bg="WHITE",command=lambda:add_num((str)(math.pi))).grid(row=5,column=0,sticky=E+W+N+S)
Button(root,text='n!',width=10,height=5,bg="WHITE",command=lambda:result(factorial((int)(e1.get())))).grid(row=5,column=1,sticky=E+W+N+S)
Button(root,text='sin',width=10,height=5,bg="WHITE",command=lambda:result(math.sin((float)(e1.get())))).grid(row=5,column=2,sticky=E+W+N+S)
Button(root,text='cos',width=10,height=5,bg="ORANGE",command=lambda:result(math.cos((float)(e1.get())))).grid(row=5,column=3,sticky=E+W+N+S)
Button(root,text='tan',width=10,height=5,bg="ORANGE",command=lambda:result(math.tan((float)(e1.get())))).grid(row=5,column=4,sticky=E+W+N+S)

Button(root,text='ln(x)',width=10,height=5,bg="WHITE",command=lambda:result(math.log((float)(e1.get())))).grid(row=6,column=0,sticky=E+W+N+S)
Button(root,text='/',width=10,height=5,bg="WHITE",command=lambda:add_num('/')).grid(row=6,column=1,sticky=E+W+N+S)
Button(root,text='e^x',width=10,height=5,bg="WHITE",command=lambda:result(math.pi**(float)(e1.get()))).grid(row=6,column=2,sticky=E+W+N+S)
Button(root,text='1/x',width=10,height=5,bg="ORANGE",command=lambda:result(1/(float)(e1.get()))).grid(row=6,column=3,sticky=E+W+N+S)
Button(root,text='x/100',width=10,height=5,bg="ORANGE",command=lambda:result(((float)(e1.get()))/100)).grid(row=6,column=4,sticky=E+W+N+S)

root.mainloop()
