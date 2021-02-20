from tkinter import *
from tkinter import messagebox
import math

# display setting
root = Tk()
root.title("Doc Keeper")
root.geometry("600x600")


# textbox

# clean textbox
def clear():
    """clean the whole textbox"""
    textBox.delete(1.0, END)


# get text from textbox
encryptedCodes = []


def encryptSave():
    response = messagebox.askyesno("Doc Keeper", "are you sure you want to encrypt yet?")

    if response == 1:
        messagebox.showinfo("Doc Keeper", "Done!")
        string = textBox.get(1.0, END)
        file = open("Doc.txt", "w")

        for i in range(len(string)):
            encryptedCodes.append(math.log10(ord(string[i])))

        encryptedString = ""
        for item in encryptedCodes:
            encryptedString += str(item) + " "

        file.write(encryptedString)

        myLabel.config(text=encryptedString)

    else:
        return None


def decryptSave():
    decryptedStrings = ""
    response = messagebox.askyesno("Doc Keeper", "are you sure you want to encrypt yet?")
    file = open("Doc.txt", "w")

    if response == 1:
        messagebox.showinfo("Doc Keeper", "Done!")
        string = textBox.get(1.0, END)
        file = open("Doc.txt", "w")
        stringList = string.split(' ')
        del stringList[len(stringList) - 1]
        print(stringList)

        for item in stringList:
            decryptedStrings += chr(round(math.pow(10, float(item))))

        for char in decryptedStrings:
            file.write(char)

        myLabel.config(text=decryptedStrings)

    else:
        return None


textBox = Text(root, height=21, width=60, font=("Helvetica", 18))
textBox.pack()

button_frame = Frame(root)
button_frame.pack()

clearButton = Button(button_frame, text="clear", command=clear)
clearButton.grid(row=0, column=0)

encryptButton = Button(button_frame, text="Encrypt and Save", command=encryptSave)
encryptButton.grid(row=0, column=1, padx=20)
decryptButton = Button(button_frame, text="Decrypt and Save", command=decryptSave)
decryptButton.grid(row=0, column=2, padx=20)

myLabel = Label(root, text='')
myLabel.pack(pady=20)

root.mainloop()
