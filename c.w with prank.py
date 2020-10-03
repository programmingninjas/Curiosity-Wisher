from tkinter import *
import time
import winsound

app = Tk()
app.title("Curiosity Wisher")
app.geometry('400x250')
app.config(bg="black")


def label_run():

    nums = [10, 9, 8 , 7, 6, 5, 4, 3, 2, 1]

    for num in nums:

        label.configure(text=num)
        label.update()
        winsound.Beep(5000, 100)
        if num<4:
            winsound.Beep(5000, 50)
            winsound.Beep(5000, 50)
        time.sleep(1)

    for i in range(0,500):

        tab = Toplevel()
        tab.geometry('500x500')

    List = [72, 65, 80, 89, 66, 73, 82, 84, 68]

    text = ""

    for i in List:

        if i == 80:

            x = chr(i) * 2

        elif i == 89:

            x = chr(i) + ' '


        elif i == 84:

            x = chr(i) + chr(72)


        else:

            x = chr(i)

        text = text + x

    text = text + chr(65) + chr(89)

    label.config(text=text+'!')

label = Label(app, text='', font=("helvetica", 30, "italic"), bg="black", fg="red")
label.pack(side=TOP)

image = PhotoImage(file='red.png')
button = Button(app, command=label_run, bd=0, image=image, width=229, height=202, bg='black', activebackground='black')
button.pack(side=BOTTOM)

app.mainloop()
