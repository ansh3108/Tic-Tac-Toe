from tkinter import *
import tkinter.messagebox
from random import *
import random
from turtle import pen
def single_playe():
    tK = Tk()
    tk.title("Tic Tac Toe Singleplayer")
    global bclick, flag, player2_name, player1_name, playerb, pa,list1,,fg,flag1,pm,pe
    pe=StringVar()
    playerb=StringVar()
    p1=StringVar()
    list1=(1,2,3,4,5,6,7,8,9)
    fg=0
    flag0

    player1_name = Entry(tk, textvariable=p1, bd=5) 
    player1_name.grid(row=1, column=1, columnspan=8)  