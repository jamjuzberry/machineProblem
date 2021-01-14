#!/usr/bin/env python
# -*- coding: utf8 -*-

# unified interface introduced in branch issues/framework

import sys
import tkinter
from tkinter import messagebox
from tkinter import font

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tkinter.Tk):

    def __init__(self, *args, **kwargs):
    
        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, YourName, Highscores, EasyLevel, ModerateLevel, HardLevel, FirstQuestion, SecondQuestion, Correct, Lifeline, CallAFriend, Message, YouLose, Continue, Congratulations):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        if cont == EasyLevel:
            self.after(500, lambda:self.show_frame(FirstQuestion))
        if cont == ModerateLevel:
            self.after(500, lambda:self.show_frame(FirstQuestion))
        if cont == HardLevel:
            self.after(500, lambda:self.show_frame(FirstQuestion))


class StartPage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        
        #ラベル
        Static1 = tkinter.Label(self, text=u'Who Wants to Be A Millionaire.', font=font.Font(size=75))
        Static1.pack()

        button1 = tkinter.Button(self, text=u'PLAY', height=3, width=20, font=LARGE_FONT, command=lambda: controller.show_frame(YourName))
        button1.pack()


        button2 = tkinter.Button(self, text=u'HIGHSCORES', height=3, width=20, font=LARGE_FONT, command=lambda: controller.show_frame(Highscores))
        button2.pack()


        button3 = tkinter.Button(self, text=u'QUIT GAME', height=3, width=20, font=LARGE_FONT, command=controller.quit)
        button3.pack()

        #ラベル
        Static2 = tkinter.Label(self, text=u'v0.0.0.1', font=font.Font(size=12))
        Static2.place(relx=0, rely=0.95)

class YourName(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="What's Your Name?", font=font.Font(size=75))
        label.pack()
        
        #エントリー
        EditBox = tkinter.Entry(self, width=50)
        EditBox.insert(tkinter.END,"Insert Name")
        EditBox.pack()
        
        button1 = tkinter.Button(self, height=3, width=20, font=LARGE_FONT, text="Start Game", command=lambda: controller.show_frame(EasyLevel))
        button1.pack()
        
        button2 = tkinter.Button(self, height=3, width=20, font=LARGE_FONT, text="Cancel", command=lambda: controller.show_frame(StartPage))
        button2.pack()
        
        
class Highscores(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="HIGHSCORES", font=font.Font(size=37))
        label.pack()
        
        button1 = tkinter.Button(self, height=3, width=20, font=LARGE_FONT, text="Back to Game", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
class EasyLevel(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="EASY \n LEVEL", font=font.Font(size=100))
        label.pack()
        
class ModerateLevel(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="MODERATE \n LEVEL", font=font.Font(size=100))
        label.pack()

class HardLevel(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="HARD \n LEVEL", font=font.Font(size=100))
        label.pack()
        
class FirstQuestion(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        button1=tkinter.Button(self, width=10, text="QUIT", command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0, rely=0)

        button2=tkinter.Button(self, height=5, width=20, text="ANSWER", command=lambda: controller.show_frame(Correct))
        button2.pack()
        
        button3=tkinter.Button(self, height=5, width=20, text="USE LIFELINE", command=lambda: controller.show_frame(Lifeline))
        button3.pack()
        
class SecondQuestion(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        button1=tkinter.Button(self, width=10, text="QUIT", command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0, rely=0)

        button2=tkinter.Button(self, height=5, width=20, text="ANSWER", command=lambda: controller.show_frame(Correct))
        button2.pack()
        
        button3=tkinter.Button(self, height=5, width=20, text="USE LIFELINE", command=lambda: controller.show_frame(Lifeline))
        button3.pack()

        button4=tkinter.Button(self, height=5, width=20, text="WALK AWAY", command=lambda: controller.show_frame(Congratulations))
        button4.pack()


class Correct(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label1=tkinter.Label(self, text="CORRECT!", font=font.Font(size=100))
        label1.pack()
        
        label2=tkinter.Label(self, text="YOU EARNED", font=font.Font(size=75))
        label2.pack()

        label3=tkinter.Label(self, text="P ", font=font.Font(size=100))
        label3.pack()

class Lifeline(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="LIFELINE", font=font.Font(size=75))
        label.pack()
        
        button1=tkinter.Button(self, height=5, width=20, text="CALL A FRIEND", command=lambda: controller.show_frame(CallAFriend))
        button1.pack()
 
        button2=tkinter.Button(self, height=5, width=20, text="50/50", command=lambda: controller.show_frame(FirstQuestion))
        button2.pack()

class CallAFriend(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label1=tkinter.Label(self, text="CALL A FRIEND", font=font.Font(size=100))
        label1.pack()

        label2=tkinter.Label(self, text="WISE FRIEND", font=font.Font(size=50))
        label2.pack()

        label3=tkinter.Label(self, text="UNSURE FRIEND", font=font.Font(size=50))
        label3.pack()
        
        label4=tkinter.Label(self, text="ARROGANT FRIEND", font=font.Font(size=50))
        label4.pack()

        button1=tkinter.Button(self, height=5, width=20, text="___ FRIEND", command=lambda: controller.show_frame(Message))
        button1.pack()
        
class Message(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="A MESSAGE FROM YOUR ___ FRIEND", font=font.Font(size=50))
        label.pack()
        
        button1=tkinter.Button(self, height=5, width=20, text="BACK TO QUESTION", command=lambda: controller.show_frame(FirstQuestion))
        button1.pack()

class YouLose(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label1=tkinter.Label(self, text="YOU LOSE!", font=font.Font(size=100))
        label1.pack()
        
        label2=tkinter.Label(self, text="EARNINGS: ", font=font.Font(size=75))
        label2.pack()

        label3=tkinter.Label(self, text="P ", font=font.Font(size=100))
        label3.pack()

        button1=tkinter.Button(self, height=5, width=20, text="HOME", command=lambda: controller.show_frame(StartPage))
        button1.pack()

class Continue(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        button1=tkinter.Button(self, height=5, width=20, text="CONTINUE", command=lambda: controller.show_frame(SecondQuestion))
        button1.pack()
 
        button2=tkinter.Button(self, height=5, width=20, text="WALK AWAY", command=lambda: controller.show_frame(Congratulations))
        button2.pack()


class Congratulations(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label1=tkinter.Label(self, text="CONGRATULATIONS!", font=font.Font(size=100))
        label1.pack()
        
        label2=tkinter.Label(self, text="YOU EARNED: ", font=font.Font(size=75))
        label2.pack()
        
        label3=tkinter.Label(self, text="P ", font=font.Font(size=100))
        label3.pack()

        button1=tkinter.Button(self, height=5, width=20, text="HOME", command=lambda: controller.show_frame(StartPage))
        button1.pack()

root = SeaofBTCapp()
root.title(u"Who Wants to Be A Millionaire.")
root.geometry("1280x720")
root.mainloop()
