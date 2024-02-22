import tkinter

top = tkinter.Tk()

quitButton = tkinter.Button(top, text="Keluar!", command=top.destroy)

quitButton.grid()

tkinter.mainloop()