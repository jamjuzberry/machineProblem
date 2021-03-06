#!/usr/bin/env python
# -*- coding: utf8 -*-

# unified interface introduced in branch issues/framework

import sys
import tkinter
import pandas as pd
import csv
from tkinter import messagebox
from tkinter import font

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tki#Import of necessary libraries
import sys
import game
import pandas as pd

#File PAths
PATH_HS = "txts/hs.csv"
PATH_MECH = "txts/mech.txt"

#Global Vars
scorePlay = None
inGame = False
amtWinnings = [0,1000,2000,4000,8000,15000,30000,40000,50000,80000,100000,200000,300000,600000,800000,1000000]

def printMechanics():
    f = open(PATH_MECH,"r")
    content = f.read().split('\n')
    for i in content:
        print(i)
    return

def verifyInput(lis,inp):
    validInp = False
    for i in lis:
        if inp == i:
            validInp = True
            break
    return validInp

def addToHs(scoreFinal,name):
    f = open(PATH_HS,"r+")
    df = pd.read_csv(f,delimiter=",")
    df2 = pd.DataFrame({"Name":[str(name)],
                        "Score":[scoreFinal]
                        })
    dfNew = df.append(df2,ignore_index=True)
    dfSorted = dfNew.sort_values('Score',ascending=False)
    dfSorted = dfSorted.head(min(10,len(dfSorted.index)))
    dfSorted.to_csv(PATH_HS,index=False)
    return ( (dfSorted['Name'] == name) & (dfSorted['Score'] == scoreFinal) ).any()

def playGame():
    name = input("Please enter your name: ")
    print("\nWelcome to Who Wants to Be A Millionaire,",name+"!")
    wantMech = None
    readyPlayerOne = None
    arr = ['Y','y','N','n']
    while not verifyInput(arr,wantMech):
        wantMech = input("Do you want to read the mechanics of the game? (Y/y for yes, N/n for no): ")
        if not verifyInput(arr,wantMech):
            print("Invalid Input! Please try again!")
    if wantMech == 'Y' or wantMech == 'y':
        printMechanics()
    while not verifyInput(arr,readyPlayerOne):
        readyPlayerOne = input("\nAre you ready to become a millionaire? (Y/y for yes, N/n for no): ")
        if not verifyInput(arr,readyPlayerOne):
            print("Invalid Input! Please try again!")
    if readyPlayerOne == 'n' or readyPlayerOne == 'N':
        return
    global inGame
    global scorePlay
    print("----------------------------------------------------\n\t\t   LET'S PLAY!\n----------------------------------------------------")
    (scorePlay,multiplier) = game.startGame(name)
    print("----------------------------------------------------")
    if scorePlay == 15:
        print("CONGRATULATIONS %s! YOU JUST WON A MILLION PESOS!!!"%(name))
    elif scorePlay == 0:
        print("It's okay %s, better luck next time!"%(name))
    else:
        print("Congratulations %s! You have won Php %0.2f" % (name,amtWinnings[scorePlay]*multiplier))
    isInHighscore = addToHs(amtWinnings[scorePlay]*multiplier,name)
    if isInHighscore:
        print("You made it to the TOP 10 OF ALL TIME! NICELY DONE!\n----------------------------------------------------")
    teleport = None
    while not verifyInput(['1','2'],teleport):
        teleport = input("Do you want to:\n\t1. Go back to Main Menu\n\t2. Exit the game\nChoose (1,2): ")
        if not verifyInput(['1','2'],teleport):
            print("Invalid Input! Please try again!")
    if teleport == '1':
        return
    else:
        print("Thank you for playing!")
        sys.exit(0)
    

def viewHS():
    f = open(PATH_HS,"r")
    df = pd.read_csv(f,delimiter=",")
    f.close()
    sortedList = df.sort_values("Score",ascending=False)
    hsList = sortedList.values.tolist()
    if len(hsList) == 0:
        print("The highscores list is empty!")
        return
    numz = 1
    print("HIGHSCORES: \nRank\tName | Score")
    for i in range(0,len(hsList)):
        print("%d.)\t%s  | PHP %0.2F" % (numz,hsList[i][0],float(hsList[i][1])))
        numz += 1
    return
    
    
    
def main():
    global inGame
    inGame = False
    while not inGame:
        print("----------------------------------------------------\n     Welcome to Who Wants to Be A Millionaire!\n----------------------------------------------------")
        print("Choose anything:\n\t1 - Play Game\n\t2 - View the highscores\n\t3 - Quit Game")
        inp = None
        while not verifyInput(['1','2','3'],inp):
            inp = input("Enter your choice: ")
            print("----------------------------------------------------")
            if verifyInput(['1','2','3'],inp):
                inp = int(inp)
                validInp = True
                break
            else:
                print("Invalid input! Please try again!")
       #Choice is successful
        if inp == 1:
            playGame()
        elif inp == 2:
            #view scores
            viewHS()
        else:
            print("Thank you for playing!")
            sys.exit(0)
        
if __name__ == "__main__":
    main()
                
nter.Tk):

    def __init__(self, *args, **kwargs):
    
        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, YourName, Highscores, EasyLevel, ModerateLevel, HardLevel, FirstQuestion, SecondQuestion, Correct, Lifeline, CallAFriend, Message, YouLose, Continue, FinalAnswer, FinalQuestion, Congratulations):

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
        
        f = None
        df = pd.read_csv('questionBank.csv')

        #label=tkinter.Label(self, text="", font=font.Font(size=25))
        
        button1=tkinter.Button(self, width=10, text="QUIT", command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0, rely=0)

        button2=tkinter.Button(self, height=5, width=20, text="ANSWER", command=lambda: controller.show_frame(Correct))
        button2.pack()
        
        button3=tkinter.Button(self, height=5, width=20, text="USE LIFELINE", command=lambda: controller.show_frame(Lifeline))
        button3.pack()
        
class FinalQuestion(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        button1=tkinter.Button(self, width=10, text="QUIT", command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0, rely=0)

        button2=tkinter.Button(self, height=5, width=20, text="ANSWER", command=lambda: controller.show_frame(Correct))
        button2.pack()
        
        button3=tkinter.Button(self, height=5, width=20, text="WALK AWAY", command=lambda: controller.show_frame(Congratulations))
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
        
class FinalAnswer(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label1=tkinter.Label(self, text="IS THIS YOUR \n FINAL ANSWER?", font=font.Font(size=75))
        label1.pack()
        
        button1=tkinter.Button(self, height=5, width=20, text="YES", command=lambda: controller.show_frame(Correct))
        button1.pack()
 
        button2=tkinter.Button(self, height=5, width=20, text="NO", command=lambda: controller.show_frame(FirstQuestion))
        button2.pack()
        
root = SeaofBTCapp()

with open("questionBank.csv", newline="")as file:
    reader = csv.reader(file)

    r=0
    for col in reader:
        c=0
        for row in col:
            label=tkinter.Label(root, width=10, height=2, text=row, relief=tkinter.RIDGE)
            label.grid(row=r, column=c)
            c += 1
        r += 1


root.title(u"Who Wants to Be A Millionaire.")
root.geometry("1280x720")
root.mainloop()
