from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import logging


# logging setting
logging.basicConfig(filename='log.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# display setting
root = Tk()
root.title("Doc Keeper")
root.geometry("650x620")

# a note book
Notebook = ttk.Notebook(root)
Notebook.pack()

mainFrame = Frame(Notebook, width=500, height=500)
algoFrame = Frame(Notebook, width=500, height=500)

mainFrame.pack(fill="both", expand=1)
algoFrame.pack(fill="both", expand=1)

Notebook.add(mainFrame, text="main menu")
Notebook.add(algoFrame, text="algos.")


# textbox
# clean textbox
def clear():
    """clean the whole textbox"""
    textBox.delete(1.0, END)
    logging.info("cleared the text box")


# get text from textbox
encryptedCodes = []

algoLevel = 2


def encryptSave():
    logging.info("encrypted")
    response = messagebox.askyesno("Doc Keeper", "are you sure you want to encrypt yet?")
    if response == 1:
        messagebox.showinfo("Doc Keeper", "Done!")
        string = textBox.get(1.0, END)
        file = open("Doc.txt", "w")

        if ifTrueRSA.get():
            for i in range(len(string)):
                encryptedCodes.append(ord(string[i]) * 3 + 1)

        if ifTrueAES.get():
            for i in range(len(string)):
                encryptedCodes.append(1 + 3 * math.log10(ord(string[i])))

        if ifTrueDES.get():
            for i in range(len(string)):
                encryptedCodes.append(31 + 3 * math.sinh(-7 + 13 * math.log(ord(string[i]), 13)))

        encryptedString = ""
        for item in encryptedCodes:
            encryptedString += str(item) + " "

        file.write(encryptedString)

    else:
        return None


def decryptSave():
    logging.info("decrypted")
    decryptedStrings = ""
    response = messagebox.askyesno("Doc Keeper", "are you sure you want to decrypt yet?")
    file = open("Doc.txt", "w")

    if response == 1:
        messagebox.showinfo("Doc Keeper", "Done!")
        string = textBox.get(1.0, END)
        file = open("Doc.txt", "w")
        stringList = string.split(' ')
        del stringList[len(stringList) - 1]

        if ifTrueRSA.get():
            for item in stringList:
                decryptedStrings += chr(round(float(int(item) - 1) / 3.0))

        if ifTrueAES.get():
            for item in stringList:
                temp = round(math.pow(10, ((float(item) - 1.0) / 3.0)))
                decryptedStrings += chr(temp)

        if ifTrueDES.get():
            for item in stringList:
                temp = round(math.pow(13, (float(math.asinh((float(item) - 31.0) / 3.0) + 7.0) / 13.0)))
                decryptedStrings += chr(int(temp))

        for char in decryptedStrings:
            file.write(char)

    else:
        return None


textBox = Text(mainFrame, height=21, width=60, font=("Helvetica", 18))
textBox.pack()

button_frame = Frame(mainFrame)
button_frame.pack()

clearButton = Button(button_frame, text="clear", command=clear)
clearButton.grid(row=0, column=0)

encryptButton = Button(button_frame, text="Encrypt and Save", command=encryptSave)
encryptButton.grid(row=0, column=1, padx=20)
decryptButton = Button(button_frame, text="Decrypt and Save", command=decryptSave)
decryptButton.grid(row=0, column=2, padx=20)

# implementing algo. frame
ifTrueAES = IntVar()
ifTrueDES = IntVar()
ifTrueRSA = IntVar()


def reset23():
    logging.info("switched the algorithm to AES")
    checkBox2.deselect()
    checkBox3.deselect()


def reset21():
    logging.info("switched the algorithm to RSA")
    checkBox2.deselect()
    checkBox1.deselect()


def reset31():
    logging.info("switched the algorithm to DES")
    checkBox3.deselect()
    checkBox1.deselect()


checkBox1 = Checkbutton(algoFrame, text="AES(security level: 2)", command=reset23, variable=ifTrueAES)
checkBox2 = Checkbutton(algoFrame, text="DES(security level: 3)", command=reset31, variable=ifTrueDES)
checkBox3 = Checkbutton(algoFrame, text="RSA(security level: 1)", command=reset21, variable=ifTrueRSA)
checkBox1.select()

checkBox2.pack()
checkBox1.pack()
checkBox3.pack()

root.mainloop()
