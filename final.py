import random
import tkinter as tk
import sys

root=tk.Tk()

def choose():
    tv= ['The Sopranos','Game of Thrones','The Wire','Dexter','Breaking Bad','The Walking Dead','Boardwalk Empire ','Rome','Mad Men','Sons of Anarchy','The West Wing','Weeds','Suits','Lost','Homeland','Legacies','Gossip Girl','13 Reasons Why','Chambers','Pretty Little Liars','The Society','Stranger Things','Chilling Adventures of Sabrina']
    li=random.choice(tv)
    return li.lower()

def jumble(word):
    a=word.split(' ')
    b=[]
    for x in a:
        w=random.sample(x,k=len(x))
        b.append(' ')
        b=b+w
    jumble=''.join(b)
    return jumble

def play():
    global a
    rw=choose()
    jw=jumble(rw)
    print("The jumbled word is:\n",jw)
    label2['text']='The Jumbled word is:'+' '+jw
    a=rw

sc=0
def check_ans(entry):
    global sc
    if(not entry):
        label1['text']=''
    elif(entry==a):
        label1['text']='Correct Answer!'
        sc=sc+1
    else:
        label1['text']='The Correct Ansers is:'+' '+str(a)
        
def check_score(entry):
    global a
    global sc
    if(entry==a):
        label1['text']='Your Current Score is:'+' '+str(sc)
    else:
        label1['text']='Your Current Score is:'+' '+str(sc)

def ex():
    root.destroy()

root.title("THE GAME OF JUMBLED WORDS")

HEIGHT=800
WIDTH=800

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH,bg='#33FFC6')
canvas.pack()

frame1=tk.Frame(root,bg='#FF3399',bd=7)
frame1.place(relx=0.5,rely=0.1,relwidth=0.6,relheight=0.1,anchor='n')

entry=tk.Entry(frame1,font=('MV Boli',18))
entry.place(relwidth=0.65,relheight=1)

button1=tk.Button(frame1,text='Enter',font=40,command=lambda:check_ans(entry.get()))
button1.place(relx=0.7,relheight=1,relwidth=0.3)

frame2=tk.Frame(root,bg='#FF3399',bd=7)
frame2.place(relx=0.5,rely=0.25,relwidth=0.3,relheight=0.1,anchor='n')

button2=tk.Button(frame2,text="PLAY",font=40,command=lambda:play())
button2.place(relheight=1,relwidth=1)


frame3=tk.Frame(root,bg='#FF3399',bd=7)
frame3.place(relx=0.5,rely=0.4,relwidth=0.6,relheight=0.2,anchor='n')

label1=tk.Label(frame3,bg='white',font=('MV Boli',18))
label1.place(relwidth=1,relheight=1)

frame4=tk.Frame(root,bg='#FF3399',bd=7)
frame4.place(relx=0.5,rely=0.8,relwidth=0.6,relheight=0.1,anchor='n')

button3=tk.Button(frame4,text="NEXT",font=40,command=lambda:play())
button3.place(relheight=1,relwidth=0.3)

button4=tk.Button(frame4,text="SCORE",font=40,command=lambda:check_score(entry.get()))
button4.place(relx=0.35,relheight=1,relwidth=0.3)

button5=tk.Button(frame4,text="QUIT",font=40,command=lambda:ex())
button5.place(relx=0.7,relheight=1,relwidth=0.3)

frame5=tk.Frame(root,bg='#FF3399',bd=7)
frame5.place(relx=0.5,rely=0.65,relwidth=0.6,relheight=0.1,anchor='n')

label2=tk.Label(frame5,bg='white',font=('MV Boli',16))
label2.place(relwidth=1,relheight=1)

play()

root.mainloop()
