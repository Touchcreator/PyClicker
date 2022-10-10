from tkinter import *
import pyautogui, time
root = Tk()
root.title("PyClicker")
root.geometry("1000x350")


clickAmountHelp = Label(root, text="The amount you want to click:")
clickAmountHelp.grid(row=0, column=0)
clickAmount = Entry(root)
clickAmount.grid(row=0, column=1, padx=10, pady=20)
clickAmount.place(relx=0.25, rely=0.25, anchor=CENTER)
clickAmountHelp.place(relx=0.10, rely=0.25, anchor=CENTER)

clickWaitHelp = Label(root, text="The amount of time you wait until clicking:")
clickWaitHelp.grid(row=0, column=2)
clickWait = Entry(root)
clickWait.grid(row=0, column=3, padx=10, pady=20)
clickWait.place(relx=0.75, rely=0.25, anchor=CENTER)
clickWaitHelp.place(relx=0.55, rely=0.25, anchor=CENTER)


def autoClick():
    time.sleep(int(clickWait.get()))
    pyautogui.click(clicks=int(clickAmount.get()), interval=0.001)

clickButton = Button(root, text="Start Clicking!", command=autoClick)
clickButton.place(relx=0.5, rely=0.75, anchor=N)

root.mainloop()