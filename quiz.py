# Create the gui x
# Add a picture. x
# Now add a label saying: Thank you god- TyGod x
# Create the canvases- in different colors to make it more vibrant -x
# Create the label on the canvases. x
# Create the options x
# Create the submit button x
# Add a function to the options buttons x
# Make it so that the function does not count the click as a point. - when wrong answer x
# Make it so that the function does count the click as a point - When the answer is correct x
# Determine the amount of points x
# Create a function for the submit button. x
# The submit button will mainly display the result of the quiz. x



import tkinter as tk
from tkinter.constants import DISABLED
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = tk.Tk()
root.title("Welcome to my TyGod Quiz")
root.geometry("300x400")
root.wm_attributes("-transparentcolor", 'grey' )
root.configure(bg="grey")

# Load the Image
# Add it to the ImageTk PhotoImage
# Assign it to a tk label image function
# And place it
load = Image.open("E:\Most used\G&D\Discord1\Yehova pic.jpg")
Imagetkp = ImageTk.PhotoImage(load)
ImagetkL = tk.Label(root, image=Imagetkp)
Imagetkp.Image = Imagetkp
ImagetkL.place(x=0, y=0)
load.close()


# StringVar
stringvar = tk.StringVar(root)

# Setting score
score = 0

# Disabling buttons
def DisableButton():
    Q1_opt1.config(state=DISABLED)
    Q1_opt2.config(state=DISABLED)
    Q1_opt3.config(state=DISABLED)
    Q1_opt4.config(state=DISABLED)


# Getting and displaying result

def GetDecision():
    if stringvar.get()  == "True":
        global score
        score += 1
        messagebox.showinfo("Congrats", message="You are correct. Score is {}".format(score))
        
    else:
        score -= 1
        messagebox.showerror("Wrong", message="You are wrong. Score is {}".format(score))
        

# Game rules in a label
tyGodL = tk.Label(root, text="Game rules: 1 attempt -TyGod Quiz", font=("Quizzical Pitch", 25), bg="powderblue", fg="blue")
tyGodL.pack(anchor="center")

# Information about the Game
My_message_Label = tk.Label(root, text= "This is a quiz mainly about God. This is not my perspective of God, but the Holy Bible's perspective" 
"\n Please check out jw.org/en/bible-teachings/questions/ for more information", font="Arial", fg= "black", bg="powderblue")
My_message_Label.place(x=0, y= 2)

# Max points in a Label
Max_points = tk.Label(root, text="6 pts available", font=("Quizzical Pitch", 15), bg="powderblue", fg="blue")
Max_points.place(x=600, y=190)

Worst_score = tk.Label(root, text="Worst score -6 pts", font=("Quizzical Pitch", 15), bg="powderblue", fg="blue")
Worst_score.place(x=600, y=230)

# First canvas - made rectangle shape
Canvas1 = tk.Canvas(root, bg="blue", height=90, width=400)
Canvas1.place(x=130, y=90)

# First Label on top of the canvas
# Install the font Quizzical Pitch
Q1_Label = tk.Label(root, text="What is God's name in English?", font=("Quizzical Pitch", 25), bg = "blue", fg="white")
Q1_Label.place(x=135, y=125)    

# First four options buttons

Q1_opt1 = Radiobutton(root, text="Mosah", variable=stringvar, value="False",  command=lambda: [GetDecision(), DisableButton()])
Q1_opt2 = Radiobutton(root, text="YHVH", variable=stringvar, value="False2",  command=lambda: [GetDecision(), DisableButton()])
Q1_opt3 = Radiobutton(root, text="YHWH", variable=stringvar, value="False3",  command=lambda: [GetDecision(), DisableButton()])
Q1_opt4 = Radiobutton(root, text="Jehova", variable=stringvar, value="True", command=lambda: [GetDecision(), DisableButton()])


# First four options - placing all 4 options  
Q1_opt1.place(x=180, y=190)
Q1_opt2.place(x=260, y=190)
Q1_opt3.place(x=340, y=190)
Q1_opt4.place(x=420, y=190)


# 2nd canvas - made rectangular shape
Canvas2 = tk.Canvas(root, bg="red", height=90, width=400)
Canvas2.place(x=132, y=250)

# 2nd Question Label on top of Canvas
Q2_Label = tk.Label(root, text="Does God exist?", font=("Quizzical Pitch", 30), bg = "red", fg="white")
Q2_Label.place(x=137, y=290)

# 2nd option buttons
Q2_opt1 = Radiobutton(root, text="Yes, I think", variable=stringvar, value='False5', command=lambda: [GetDecision2(), DisableButton2()])
Q2_opt2 = Radiobutton(root, text="No", variable=stringvar, value='False6', command=lambda: [GetDecision2(), DisableButton2()])
Q2_opt3 = Radiobutton(root, text="Not certain", variable=stringvar, value='False7', command=lambda: [GetDecision2(), DisableButton2()])
Q2_opt4 = Radiobutton(root, text="Yes, \n it is written in 1.John 5:20", variable=stringvar, value='True2', command=lambda: [GetDecision2(), DisableButton2()])


# 2nd options placement
Q2_opt1.place(x=130, y=345)
Q2_opt2.place(x=220, y=345)
Q2_opt3.place(x=270, y=345)
Q2_opt4.place(x=370, y=345)

# Disabling buttons
def DisableButton2():
    Q2_opt1.config(state=DISABLED)
    Q2_opt2.config(state=DISABLED)
    Q2_opt3.config(state=DISABLED)
    Q2_opt4.config(state=DISABLED)



# Getting and displaying result
def GetDecision2():
    if stringvar.get()  == "True2":
        global score
        score += 1
        messagebox.showinfo("Congrats", message="You are correct. Score is {}".format(score))
        
    else:
        score -= 1
        messagebox.showerror("Wrong", message="You are wrong. Score is {}".format(score))
      



# 3rd Canvas, - made in rectangular shapes
Canvas3 = tk.Canvas(root, bg = "powderblue", height=90, width=400)
Canvas3.place(x=132, y=460)

# 3rd Label on top of Canvas
Q3_Label = tk.Label(root, text="Who created the entire Universe?", font=("Quizzical Pitch", 22), bg="powderblue", fg="White" )
Q3_Label.place(x=137, y=500)

# Third - four options buttons
Q3_opt1 = Radiobutton(root, text="Maybe some God?", variable= stringvar, value='False8', command=lambda: [GetDecision3(), DisableButton3()])
Q3_opt2 = Radiobutton(root, text="Scientists", variable=stringvar, value='False9', command=lambda: [GetDecision3(), DisableButton3()])
Q3_opt3 = Radiobutton(root, text="The Big Bang Theory", variable=stringvar, value='False10', command=lambda: [GetDecision3(), DisableButton3()])
Q3_opt4 = Radiobutton(root, text="It is Jehova \n -since it says in Hebrews 3:4", variable=stringvar, value='True3', command=lambda: [GetDecision3(), DisableButton3()])

# 3rd options placement
Q3_opt1.place(x=132, y=560)
Q3_opt2.place(x=255, y=560)
Q3_opt3.place(x=332, y=560)
Q3_opt4.place(x=472, y=560)


# Diabling buttons
def DisableButton3():
    Q3_opt1.config(state=DISABLED)
    Q3_opt2.config(state=DISABLED)
    Q3_opt3.config(state=DISABLED)
    Q3_opt4.config(state=DISABLED)


# Getting and displaying result
def GetDecision3():
    if stringvar.get()  == "True3":
        global score
        score += 1
        messagebox.showinfo("Congrats", message="You are correct. Score is {}".format(score))
        
    else:
        score -= 1
        messagebox.showerror("Wrong", message="You are wrong. Score is {}".format(score))
        


 

# 4th canvas - made rectungalar shape
Canvas4 = tk.Canvas(root, bg= "powderblue", height=90, width=400)
Canvas4.place(x=798, y=90)

# 4th Question Label on top of Canvas
Q4_Label = tk.Label(root, text="Has anyone ever seen God?", font=("Quizzical Pitch", 27), bg="powderblue", fg="white")
Q4_Label.place(x=802, y=114)

# 4th options buttons
Q4_opt1 = Radiobutton(root, text="No.\nIt says that in Exodus 33:20", variable=stringvar, value="True4", command=lambda: [GetDecision4(), DisableButton4()])
Q4_opt2 = Radiobutton(root, text="Yes, my mom", variable=stringvar, value="False11", command=lambda: [GetDecision4(), DisableButton4()])
Q4_opt3 = Radiobutton(root, text="Moses", variable=stringvar, value="False12", command=lambda: [GetDecision4(), DisableButton4()])
Q4_opt4 = Radiobutton(root, text="Abraham", variable=stringvar, value="False13", command=lambda:[GetDecision4(), DisableButton4()])

# 4th options placement
Q4_opt1.place(x=800, y=190)
Q4_opt2.place(x=965, y=190)
Q4_opt3.place(x=1063, y=190)
Q4_opt4.place(x=1123, y=190)


# Diabling buttons
def DisableButton4():
    Q4_opt1.config(state=DISABLED)
    Q4_opt2.config(state=DISABLED)
    Q4_opt3.config(state=DISABLED)
    Q4_opt4.config(state=DISABLED)


# Getting and displaying result
def GetDecision4():
    if stringvar.get()  == "True4":
        global score
        score += 1
        messagebox.showinfo("Congrats", message="You are correct. Score is {}".format(score))
        
    else:
        score -= 1
        messagebox.showerror("Wrong", message="You are wrong. Score is {}".format(score))





# 5th canvas - made rectungalar shape
Canvas5 = tk.Canvas(root, bg= "blue", height=90, width=400)
Canvas5.place(x=798, y=250)


# 5th Question Label on top of Canvas
Q5_Label = tk.Label(root, text="Will God forgive my sins?", font=("Quizzical Pitch", 27), bg="blue", fg="white")
Q5_Label.place(x=802, y=290)

# 5th options buttons
Q5_opt1 = Radiobutton(root, text="No", variable=stringvar, value="False14", command=lambda: [GetDecision5(), DisableButton5()])
Q5_opt2 = Radiobutton(root, text="Praying 10xdaily will", variable=stringvar, value="False15", command=lambda: [GetDecision5(), DisableButton5()])
Q5_opt3 = Radiobutton(root, text="Yes, \n but only briefly", variable=stringvar, value="False16", command=lambda:[GetDecision5(), DisableButton5()])
Q5_opt4 = Radiobutton(root, text="Yes, he will. \n See Psalm 86:5", variable=stringvar, value="True5", command=lambda: [GetDecision5(), DisableButton5()])

# 5th options placement
Q5_opt1.place(x=800, y=350)
Q5_opt2.place(x=845, y=350)
Q5_opt3.place(x=980, y=350)
Q5_opt4.place(x=1095, y=350)

# Disabling buttons
def DisableButton5():
    Q5_opt1.config(state=DISABLED)
    Q5_opt2.config(state=DISABLED)
    Q5_opt3.config(state=DISABLED)
    Q5_opt4.config(state=DISABLED)


# Getting and displaying result
def GetDecision5():
    if stringvar.get()  == "True5":
        global score
        score += 1
        messagebox.showinfo("Congrats", message="You are correct. Score is {}".format(score))

    
        
    else:
        score -= 1
        messagebox.showerror("Wrong", message="You are wrong. Score is {}".format(score))






# 6th Canvas, - made in rectangular shapes
Canvas6 = tk.Canvas(root, bg = "navy", height=90, width=400)
Canvas6.place(x=798, y=460)

# 6th Question Label on top of Canvas
Q6_Label = tk.Label(root, text="Is human suffering caused by God?", font=("Quizzical Pitch", 21), bg="navy", fg="white")
Q6_Label.place(x=802, y=495)

# 6th options buttons 
Q6_opt1 = Radiobutton(root, text = "Yes", variable=stringvar, value="False17", command=lambda: [GetDecision6(), DisableButton6()])
Q6_opt2 = Radiobutton(root, text = "Partly", variable=stringvar, value="False18", command=lambda: [GetDecision6(), DisableButton6()])
Q6_opt3 = Radiobutton(root, text = "It's caused by humans only", variable=stringvar, value="False19", command=lambda: [GetDecision6(), DisableButton6()])
Q6_opt4 = Radiobutton(root, text = "No.\n See James 1:13", variable=stringvar, value="True6", command=lambda:[GetDecision6(), DisableButton6()])

# 6th options Buttons placement
Q6_opt1.place(x=800, y=560)
Q6_opt2.place(x=845, y=560)
Q6_opt3.place(x=905, y=560)
Q6_opt4.place(x=1075, y=560)


# Diabling buttons
def DisableButton6():
    Q6_opt1.config(state=DISABLED)
    Q6_opt2.config(state=DISABLED)
    Q6_opt3.config(state=DISABLED)
    Q6_opt4.config(state=DISABLED)


# Getting and displaying result
def GetDecision6():
    if stringvar.get()  == "True6":
        global score
        score += 1
        messagebox.showinfo("Congrats", message="You are correct. Score is {}".format(score))
        
    else:
        score -= 1
        messagebox.showerror("Wrong", message="You are wrong. Score is {}".format(score))
        


# side win
"""
root.configure(bg= '#198CFF')
root.wm_attributes("-transparentcolor", '#198CFF' )
"""
# Point all radiobuttons to same var
# This will make only one can be selected aka only one can be True
# Then the rest is false
# StringVar in general just updates any widgets

# Format the score from which radiobutton the user chooses


root.mainloop()