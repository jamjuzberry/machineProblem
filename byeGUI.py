#CMSC11 >:'(

import random
import time
import millionaire
import numpy as np
import csv
import pandas as pd
import sys

global i
global money
global file

choice = 1
Money = ['1,000','2,000','4,000','8,000','15,000','30,000','40,000','50,000','80,000','100,000','200,000','300,000','600,000','800,000','1,000,000']

MoneyInt = [0,1000,2000,4000,8000,15000,30000,40000,50000,80000,100000,200000,300000,600000,800000,1000000,0]

AnswerList = ["A","B","C","D", "Correct"]

while(True):
    print ('1 - Play \n')
    print ('2 - Highscores \n')
    print ('3 - Quit \n')
    answer = input ('Choose a number: ')
    if (answer == 1):
        Play
    elif (answer == 2):
        Highscores
    else: sys.exit()


def Play:
    #counters
    CurrentEarnings = 0
    Highscore = 0
    LifelineFifty = 0
    LifelineFriend = 0
    Lives = 2
    i = 1
    j = 1
    #inserting name
    answer = input ('Insert Name: \n')
    print ('Hello, {answer}')
    #easyLevel
    print("Easy Level \n Good Luck, {answer}")
    time.sleep(2)
    easyQuestions = list(open("easyLevel.txt", encoding = "utf8"))
    while 0 < i <= 5:
        f = easyQuestions.pop(random.randint(0,len(easyQuestions)-1))
    Lines = f.split('[')
    Question = lines[0]
    Answers = lines[1].strip("\n").split(',')
    millionaire.displayQuestion(i, Money, Question, Answers, j)
    answerdict = {'A' : answers[0],'B' : answers[1],'C' : answers[2],'D' : answers[3],}

def Highscores():
    #inserting name
    answer = input ('Insert Name: \n')
    print ('Hello, {answer}')
    #csv
    f = None
    df = pd.read_csv('questionBank.csv')
    print(df)

while(True):
    print ('WHO WANTS TO BE A BILLIONAIRE? \n')
    print ('1 - Play \n')
    print ('2 - Highscores \n')
    print ('3 - Quit \n')
    answer = input ('Choose a number: ')
    if answer == 1:
        Play()
    elif answer == 2:
        Highscores
    else: sys.exit()
