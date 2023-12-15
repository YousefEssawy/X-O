import tkinter,random
from tkinter import *
from tkinter import messagebox
 
root = Tk()
root.title("Tic Tac Toe Game")

clicked = True
count = 0
x_score = 0
o_score = 0


def show_score():
    x_lable.config(text=f"X: {x_score}")
    o_lable.config(text=f"O: {o_score}")

#Disable all buttons
def disable_all_buttons():
    button =[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for buttons in button:
        buttons["state"] = DISABLED
    
#Check for a winner
def check_winner():
    global x_score, o_score
    winning_combinations = [
        [b1, b2, b3], [b4, b5, b6], [b7, b8, b9],  # Rows
        [b1, b4, b7], [b2, b5, b8], [b3, b6, b9],  # Columns
        [b1, b5, b9], [b3, b5, b7]                 # Diagonals
    ]

    for combo in winning_combinations:
        if all(button["text"] == "X" for button in combo):
            for button in combo:
                button["bg"] = "Green"
            #messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
            result_lable.config(text="X Wins!")
            x_score += 1
            disable_all_buttons()
            show_score()
            return True
        elif all(button["text"] == "O" for button in combo):
            for button in combo:
                button["bg"] = "Green"
            #messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins!")
            result_lable.config(text="O Wins!")
            o_score += 1
            disable_all_buttons()
            show_score()
            return True
        
    #Check if tie
    if count == 9:
        button =[b1,b2,b3,b4,b5,b6,b7,b8,b9]
        #messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No one wins!")
        result_lable.config(text="It's A Tie!")
        for buttons in button:  
            buttons["bg"] = "red"
        disable_all_buttons()


# Button clicked function
def b_click(b):
    global clicked, count
    
    if b["text"] == " " and clicked:
        b["text"] = "X"
        clicked = False
        count += 1
        if not check_winner():
            computer_move()

# Computer move function
def computer_move():
    global clicked, count
    
    empty_buttons = [button for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9] if button["text"] == " "]

    if empty_buttons:
        computer_choice = random.choice(empty_buttons)
        computer_choice["text"] = "O"
        clicked = True
        count += 1
        check_winner()

#Reset Game
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,clicked,count
    clicked = True
    count = 0
    result_lable.config(text=" ")

    #Buttons
    b1 = Button(root, text=" ", font=("helvetica", 20), height=3 , width= 6, bg= "SystemButtonFace" , command= lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("helvetica", 20), height=3 , width= 6, bg= "SystemButtonFace" , command= lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("helvetica", 20), height=3 , width= 6, bg= "SystemButtonFace" , command= lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("helvetica", 20), height=3 , width= 6, bg= "SystemButtonFace" , command= lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("helvetica", 20), height=3 , width= 6, bg= "SystemButtonFace" , command= lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("helvetica", 20), height=3 , width= 6, bg= "SystemButtonFace" , command= lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("helvetica", 20), height=3 , width= 6, bg= "SystemButtonFace" , command= lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("helvetica", 20), height=3 , width= 6, bg= "SystemButtonFace" , command= lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("helvetica", 20), height=3 , width= 6, bg= "SystemButtonFace" , command= lambda: b_click(b9))

    #Buttom grid
    b1.grid(row=3, column=0)
    b2.grid(row=3, column=1)
    b3.grid(row=3, column=2)

    b4.grid(row=4, column=0)
    b5.grid(row=4, column=1)
    b6.grid(row=4, column=2)

    b7.grid(row=5, column=0)
    b8.grid(row=5, column=1)
    b9.grid(row=5, column=2)


#Score lable
score_lable = Label(root, text="Score", font=("helvetica", 18))
result_lable = Label(root, text=" ", font=("helvetica", 15))
x_lable = Label(root, text="X : 0", font=("helvetica", 20))
o_lable = Label(root, text="PC : 0", font=("helvetica", 20))

#Score Grid
x_lable.grid(row=0, column=0)
score_lable.grid(row=0,column=1)
o_lable.grid(row=0, column=2)
result_lable.grid(row=1, column=1)


#Restart button
restart = Button(root,text="Restart", command= reset, font=("helvetica", 15))
restart.grid(row= 2,column=1)

reset()
root.mainloop()


#--------------------------------------------------------------------------------------------------------#



#Check to see if someone won
# def checkifwon():
#     global winner
#     winner = False

#     if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
#       b1["bg"] = "Green"
#       b2["bg"] = "Green"
#       b3["bg"] = "Green"
#       winner = True
#       messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
#       disable_all_buttons()
#     elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
#       b4["bg"] = "Green"
#       b5["bg"] = "Green"
#       b6["bg"] = "Green"
#       winner = True
#       messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
#       disable_all_buttons()
#     elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
#       b7["bg"] = "Green"
#       b8["bg"] = "Green"
#       b9["bg"] = "Green"
#       winner = True
#       messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
#       disable_all_buttons()

#     elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
#       b1["bg"] = "Green"
#       b4["bg"] = "Green"
#       b7["bg"] = "Green"
#       winner = True
#       messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
#       disable_all_buttons()
#     elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
#       b2["bg"] = "Green"
#       b5["bg"] = "Green"
#       b8["bg"] = "Green"
#       winner = True
#       messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
#       disable_all_buttons()
#     elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
#       b3["bg"] = "Green"
#       b6["bg"] = "Green"
#       b9["bg"] = "Green"
#       winner = True
#       messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
#       disable_all_buttons()
    
#     elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
#       b1["bg"] = "Green"
#       b5["bg"] = "Green"
#       b9["bg"] = "Green"
#       winner = True
#       messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
#       disable_all_buttons()
#     elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
#       b3["bg"] = "Green"
#       b5["bg"] = "Green"
#       b7["bg"] = "Green"
#       winner = True
#       messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
#       disable_all_buttons()

#Button clicked function
# def b_click(b):
#     global clicked, count
    
#     if b["text"] == " " and clicked == True:
#        b["text"] = "X"
#        clicked = False
#        count += 1
#        check_winner()
#     elif b["text"] == " " and clicked == False:
#        b["text"] = "O"
#        clicked = True
#        count += 1
#        check_winner()
#     else:
#        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick anthor box...")