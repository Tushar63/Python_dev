from tkinter import *
from random import randint


window=Tk()
def game_begin():
    window=Toplevel()
    window.title("Game")
    window.configure(bg="")
    game_name=Label(window,width=40,height=3,text="The Game Of Chances",font=("arial",40,"bold"),bg="black",fg="yellow")
    game_name.grid(row=0,column=0)

    global player_name
    player_name=Label(window,width=10,height=1,text="Player Name",font=("arial",20,"bold")).grid(row=2,column=0)
    global p1
    p1=Entry(window,highlightthickness=5).place(x=750,y=195)
    global button_start
    button_start=Button(window,width=16,height=3,text="START",font=("arial",15,"bold"),bg="blue",fg="white",command=lambda:game_started()).grid(row=3,column=0)


def last_window():
    window=Toplevel()
    global label_score
    label_score=Label(window,width=16,height=3,text="Player Score:",font=("arial",20,"bold"),bg="white",fg="black").grid(row=0,column=1)
    global score
    score=Label(window,width=10,height=3,text=player_score['text'],font=("arial",20,"bold"),bg="white",fg="black").grid(row=0,column=3)
    global exit_button
    exit_button=Button(window,width=20,height=4,text="EXIT",font=("arial",20,"bold"),bg="red",fg="white",command=window.quit).grid(row=2,column=1)
    global new_button
    new_button=Button(window,width=20,height=4,text="START NEW GAME",font=("arial",20,"bold"),bg="red",fg="white",command=lambda:game_begin()).grid(row=2,column=3)




def game_started():
    window=Toplevel()
    window.title("Game Rock paper and scissor")
    window.configure(background="white")

    global button_rock
    button_rock=Button(window,width=16,height=3,text="Rock",font=("arial",20,"bold"),bg="red",fg="black",command=lambda:choice_update("rock")).grid(row=6,column=1)
    global button_paper
    button_paper=Button(window,width=16,height=3,text="Paper",font=("arial",20,"bold"),bg="red",fg="black",command=lambda:choice_update("paper")).grid(row=6,column=2)
    global button_scissor
    button_scissor=Button(window,width=16,height=3,text="Scissor",font=("arial",20,"bold"),bg="red",fg="black",command=lambda:choice_update("scissor")).grid(row=6,column=3)
    global button_spock
    button_spock=Button(window,width=16,height=3,text="Spock",font=("arial",20,"bold"),bg="red",fg="black",command=lambda:choice_update("spock")).grid(row=6,column=4)
    global button_lizard
    button_lizard=Button(window,width=16,height=3,text="Lizard",font=("arial",20,"bold"),bg="red",fg="black",command=lambda:choice_update("lizard")).grid(row=6,column=5)

    label_player=Label(window,width=16,height=3,background="white",text="PLAYER",font=("arial",20,"bold"))
    label_computer=Label(window,width=16,height=3,background="white",text="COMPUTER",font=("arial",20,"bold"))
    label_computer.grid(row=1,column=1)
    label_player.grid(row=1,column=5)



    global l1
    l1= Label(window, text="", font= ('Helvetica 30 bold'), fg="khaki3",bg="black")
    l1.grid(row=3,column=2)

    #Label for VS
    l2= Label(window, text="VS", font= ('Helvetica 30 bold'), fg="khaki3",bg="black")
    l2.grid(row=3,column=3)

    global l3
    l3= Label(window, text="", font= ('Helvetica 30 bold'), fg="khaki3",bg="black")
    l3.grid(row=3,column=4)



    global computer_score
    global player_score
    computer_score=Label(window,text=0,font=("arial",60,"bold"),fg="brown")
    player_score=Label(window,text=0,font=("arial",60,"bold"),fg="brown")
    computer_score.grid(row=5,column=1)
    player_score.grid(row=5,column=5)

    global final_msg
    final_msg=Label(window,font=("arial",40,"bold"),bg="black",fg="white")
    final_msg.grid(row=8,column=3)
    
    


def msg_update(a):
    final_msg['text']=a

def computer_update():
    final=int(computer_score['text'])
    final+=1
    if final==3:
        last_window()
    computer_score["text"]=str(final)

def player_update():
    final=int(player_score['text'])
    final+=1
    player_score["text"]=str(final)


def winner_check(p,c):
    if p==c:
        msg_update("Its a tie")

    elif p=="rock":
        if c=="paper" or c=="spock":
            msg_update("computer wins")
            computer_update()
        else:
            msg_update("player wins")
            player_update()

    elif p=="paper":
        if c=="lizard" or c=="scissor":
            msg_update("computer wins")
            computer_update()
        else:
            msg_update("player wins")
            player_update()

    elif p=="scissor":
        if c=="spock" or c=="rock":
            msg_update("computer wins")
            computer_update()
        else:
            msg_update("player wins")
            player_update()

    elif p=="lizard":
        if c=="scissor" or c=="rock":
            msg_update("computer wins")
            computer_update()
        else:
            msg_update("player wins")
            player_update()

    elif p=="spock":
        if c=="paper" or c=="lizard":
            msg_update("computer wins")
            computer_update()
        else:
            msg_update("player wins")
            player_update()

    else:
        pass

to_select=["rock","paper","scissor","lizard","spock"]

def choice_update(a):
    choice_computer=to_select[randint(0,4)]
    l1.configure(text=choice_computer)
    l3.configure(text=a)
    winner_check(a,choice_computer)





game_begin()





window.mainloop()