import tkinter as tk
from tkinter import *
from gtts import gTTS
from playsound import playsound
#create mathematical functions



def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(a,b):
    L = a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L = L+1
def hcf(a,b):
    H = a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H = H-1

#Extract the numbers from the given any type of message
def extract_from_text(text):
    l = []
    for i in text.split(" "):
        try:
            l.append(float(i))
        except ValueError:
            pass
    return l

#calculate value
def calculate_value():
    text = input.get()
    speech = gTTS(text=text, lang="en")
    speech.save(r"E:\python_workspace\Tkinter Projects\Smart Calculator\speech.mp3")
    playsound(r"E:\python_workspace\Tkinter Projects\Smart Calculator\speech.mp3")
    for word in text.split(" "):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                #calling the mathematical functions
                #after extracting
                #here match the key and takes first two values from list
                r = operations[word.upper()](l[0],l[1])
                #delete all previous values from list
                list.delete(0,END)
                #and then insert new values in list for current operation
                list.insert(END,r)
            except:
                # if given input not match anything in operations
                list.delete(0,END)
                list.insert(END,"Something went wrong \n please enter again")
            finally:
                break
                #if given input not match anything in operations
        elif word.upper() not in operations.keys():
            list.delete(0, END)
            list.insert(END, "Something went wrong \n please enter again")




#here dictionary used key value pair
#where keys=word and value=function related to maths
#this keys perform operation according to given user inputs
operations = {"ADD":add,"ADDITION":add,"SUM":add,"PLUS":add,"+":add,
              "SUB":sub, "SUBSTRACT":sub, "MINUS":sub, "DIFFERENCE":sub,"-":sub,
              "LCM":lcm,
              "HCF":hcf,
              "PRODUCT":mul,"MUL":mul,"MULTIPLY":mul,"MULTIPLICATION":mul,"*":mul,
              "DIVIDE":div, "DIVISION":div, "DIV":div,"/":div,
              "MOD":mod, "MODULUS":mod, "REMANDER":mod,"%":mod
              }
#create instance of tk
win = tk.Tk()

#icon
win.iconbitmap('calculator.ico')

#define size of UI
win.geometry("500x300")

win.title("Smart Calculator")

#create lable
l1  = Label(win,text = "Welcome to Smart Calculator",width = 30)
l1.place(x=150,y=10)

l2  = Label(win,text = "My name is Jay",width = 30)
l2.place(x=145,y=30)

l3  = Label(win,text = "What can i help you?",width = 30)
l3.place(x=140,y=130)

#take User Input
#StringVar take string data from user
user_input = StringVar()

#Entry is used to take input from user in textbox
input  = Entry(win,width = 30,textvariable = user_input)
input.place(x = 160, y = 160)

#create button
b1 = Button(win, text = "Calculate", command  = calculate_value)
b1.place(x=215,y=190)

list = Listbox(win,width = 30, height = 3)
list.place(x = 150,y=230)
win.mainloop()