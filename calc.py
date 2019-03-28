from tkinter import *
from math import *
f = 0
ravno = 0
deystvie = 0
d = 0
znach_deystviya = 0
pm=0
corsqr = 0
m = 0
memor = 0

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"



def memoryplys():
    global m
    global memor
    m = m + float(text.get(1.0, END))
    memor = 1

def memoryminus():
    global m
    global memor
    m = m - float(text.get(1.0, END))
    memor = 1

def memorydelete():
    global m
    m = 0

def memoryshow():
    global m
    global f
    text.delete(1.0, END)
    text.insert(1.0, m)
    f = m

def steret():
    text.delete(1.0)

def coren():
    corsqr = sqrt( float(text.get(1.0, END)))
    text.delete(1.0, END)
    text.insert(1.0, corsqr)

def procent():
    proc = (f/100)*(float(text.get(1.0, END)))
    text.delete(1.0, END)
    text.insert(1.0, proc)

def plusminus():
    global pm
    global f
    f = int(text.get(1.0, END))
    if f != 0:
        f = f *(-1)
        text.delete(1.0, END)
        text.insert(1.0, f)

def vibor():
    global znach_deystviya
    if znach_deystviya == "-":
        raznost()
    elif znach_deystviya == "/":
        delit()
    elif znach_deystviya == "X":
        umnojit()
    elif znach_deystviya == "+":
        summa()

def summa():
    global f
    f += float(text.get(1.0, END))
    text.delete(1.0, END)
    text.insert(2.0, f)

def raznost():
    global f
    f -= float(text.get(1.0, END))
    text.delete(1.0, END)
    text.insert(2.0, f)

def umnojit():
    global f
    f = f * float(text.get(1.0, END))
    text.delete(1.0, END)
    text.insert(2.0, f)

def delit():
    global f
    f = f / float(text.get(1.0, END))
    f = float(toFixed(f, 3))
    text.delete(1.0, END)
    text.insert(2.0, f)


def insert(sis):
    global deystvie
    global f
    global ravno
    global deystvie
    global znach_deystviya
    global memor

    if sis == "+":
        if f == 0 or ravno == 1:
            f = float(text.get(1.0, END))
        else:
            vibor()
        ravno = 0
        deystvie = 1
        znach_deystviya = sis
    elif sis == "-":
        if f == 0 or ravno == 1:
            f = float(text.get(1.0, END))
        else:
            vibor()
        ravno = 0
        deystvie = 1
        znach_deystviya = sis
    elif sis == "X":
        if f == 0 or ravno == 1:
            f = float(text.get(1.0, END))
        else:
            vibor()
        ravno = 0
        deystvie = 1
        znach_deystviya = sis
    elif sis == "/":
        if f == 0 or ravno == 1:
            f = float(text.get(1.0, END))
        else:
            vibor()
        ravno = 0
        deystvie = 1
        znach_deystviya = sis
    else:
        if ravno == 1:
            text.delete(1.0, END)
            s = sis
            text.insert(2.0, s)
            ravno = 0
            d = 0
            f = 0
            znach_deystviya = 0
        else:
            if deystvie == 0:
                if int(text.get(1.0, END)) == 0:
                    text.delete(1.0, END)
                if memor == 1:
                    text.delete(1.0, END)
                    memor = 0
                s = sis
                text.insert(2.0, s)
            else:
                text.delete(1.0, END)
                s = sis
                text.insert(2.0, s)
                deystvie = 0

def rezult():
    global f
    global ravno
    global d
    global znach_deystviya

    if znach_deystviya == "+":
        if ravno == 1:
            text.delete(1.0, END)
            f = f + d
            text.insert(1.0, f)
        else:
            d = float(text.get(1.0, END))
            f = f + d
            text.delete(1.0, END)
            text.insert(1.0, f)
        ravno = 1
    elif znach_deystviya == "-":
        if ravno == 1:
            text.delete(1.0, END)
            f = f - d
            text.insert(1.0, f)
        else:
            d = float(text.get(1.0, END))
            f = f - d
            text.delete(1.0, END)
            text.insert(1.0, f)
        ravno = 1
    elif znach_deystviya == "X":
        if ravno == 1:
            text.delete(1.0, END)
            f = f * d
            text.insert(1.0, f)
        else:
            d = float(text.get(1.0, END))
            f = f * d
            text.delete(1.0, END)
            text.insert(1.0, f)
        ravno = 1
    elif znach_deystviya == "/":
        if ravno == 1:
            text.delete(1.0, END)
            f = f / d
            f = float(toFixed(f, 3))
            text.insert(1.0, f)
        else:
            d = float(text.get(1.0, END))
            f = f / d
            f = float(toFixed(f, 3))
            text.delete(1.0, END)
            text.insert(1.0, f)
        ravno = 1


def ochistka():
    global f
    global ravno
    global d
    global znach_deystviya
    text.delete(1.0, END)
    f = 0
    ravno = 0
    d = 0
    znach_deystviya = 0
    text.insert(1.0, 0)


root = Tk()
root.configure(background='black')

f_1 = Frame()
f_2 = Frame()
f_3 = Frame()
f_4 = Frame()
f_5 = Frame()

text = Text(width=30, height=1)
text.configure(background='black', foreground='white')
text.insert(1.0, 0)
text.pack()


f_1['bg'] = '#000000'
f_2['bg'] = '#000000'
f_3['bg'] = '#000000'
f_4['bg'] = '#000000'
f_5['bg'] = '#000000'

Button(f_1, width=4, height=2, text="MRC",bg="Gray", fg="white", command=memorydelete).pack(side=LEFT, padx=2, pady=2)
Button(f_1, width=4, height=2, text="M-", bg="Gray", fg="white", command=memoryminus).pack(side=LEFT, padx=2, pady=2)
Button(f_1, width=4, height=2, text="M+", bg="Gray", fg="white", command=memoryplys).pack(side=LEFT, padx=2, pady=2)
Button(f_1, width=4, height=2, text="+/-", bg="Gray", fg="white", command=plusminus).pack(side=LEFT, padx=2, pady=2)
Button(f_1, width=4, height=2, text="sqr", bg="Gray", fg="white", command=coren).pack(side=LEFT, padx=2, pady=2)
Button(f_1, width=4, height=2, text=">", bg="Gray", fg="white", command=steret).pack(side=LEFT, padx=2, pady=2)

Button(f_2, width=4, height=2, text="OFF", bg="Gray", fg="white", command=root.destroy).pack(side=LEFT, padx=2, pady=2)
Button(f_2, width=4, height=2,  text="7", bg="black", fg="white", command=lambda s=7: insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_2, width=4, height=2,  text="8", bg="black", fg="white", command=lambda s=8: insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_2, width=4, height=2,  text="9", bg="black", fg="white", command=lambda s=9: insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_2, width=4, height=2, text="%", bg="Gray", fg="white", command=procent).pack(side=LEFT, padx=2, pady=2)
Button(f_2, width=4, height=2, text="MU",bg="Gray", fg="white", command=memoryshow).pack(side=LEFT, padx=2, pady=2)

Button(f_3, width=4, height=2, bg="Gray", fg="white",  text="AC", command=ochistka).pack(side=LEFT, padx=2, pady=2)
Button(f_3, width=4, height=2, bg="black", fg="white",  text="4", command=lambda s=4: insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_3, width=4, height=2, bg="black", fg="white",  text="5", command=lambda s=5: insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_3, width=4, height=2, bg="black", fg="white",  text="6", command=lambda s=6: insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_3, width=4, height=2, bg="Gray", fg="white",  text="X", command=lambda s="X": insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_3, width=4, height=2, bg="Gray", fg="white",  text="/", command=lambda s="/": insert(s)).pack(side=LEFT, padx=2, pady=2)

Button(f_4, width=4, height=2, bg="red", fg="white", text="CE", command=ochistka).pack(side=LEFT, padx=2, pady=2)
Button(f_4, width=4, height=2, bg="black", fg="white", text="1", command=lambda s=1: insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_4, width=4, height=2, bg="black", fg="white", text="2", command=lambda s=2: insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_4, width=4, height=2, bg="black", fg="white",  text="3", command=lambda s=3: insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_4, width=4, height=2, bg="Gray", fg="white").pack(side=LEFT, padx=2, pady=2)
Button(f_4, width=4, height=2, bg="Gray", fg="white",  text="-", command=lambda s="-": insert(s)).pack(side=LEFT, padx=2, pady=2)

Button(f_5, width=4, height=2, bg="red", fg="white",  text="C", command=ochistka).pack(side=LEFT, padx=2, pady=2)
Button(f_5, width=4, height=2, bg="black", fg="white",  text="0", command=lambda s="0": insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_5, width=4, height=2, bg="black", fg="white",  text="00", command=lambda s="00": insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_5, width=4, height=2, bg="black", fg="white",  text=".", command=lambda s=".": insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_5, width=4, height=2, bg="Gray", fg="white",  text="+", command=lambda s="+": insert(s)).pack(side=LEFT, padx=2, pady=2)
Button(f_5, width=4, height=2, bg="Gray", fg="white",  text="=", command=rezult).pack(side=LEFT, padx=2, pady=2)


f_1.pack()
f_2.pack()
f_3.pack()
f_4.pack()
f_5.pack()
root.mainloop()
