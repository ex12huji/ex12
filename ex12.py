import tkinter as tki

class Gui:
    def __init__(self,parent):
        self._parent = parent

        menu = tki.Menu(parent)
        self._parent.config(menu=menu)

        helpmenu = tki.Menu(menu)##Fגיכגיעכיעכ
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='How to play', command=None)
        helpmenu.add_command(label='About', command=None)
        helpmenu.add_separator()
        helpmenu.add_command(label='Exit', command=self._parent.quit)


        # creating the Help toolbar
        toolbarFrame = tki.Frame(self._parent)

        lineButton = tki.Button(toolbarFrame, text='Line', command=None)
        lineButton.pack(side=tki.RIGHT, padx=2, pady=2)
        circleButton = tki.Button(toolbarFrame, text='Circle', command=None)
        circleButton.pack(side=tki.RIGHT, padx=2, pady=2)
        triangleButton = tki.Button(toolbarFrame, text='Triangle',
                                    command=None)
        triangleButton.pack(side=tki.RIGHT, padx=2, pady=2)
        rectangleButton = tki.Button(toolbarFrame, text='Rectangle',
                                     command=None)
        rectangleButton.pack(side=tki.RIGHT, padx=2, pady=2)


        toolbarFrame.pack(side=tki.RIGHT)

        # creating the canvas and left users window
        self._left_window = tki.Frame(self._parent, height=150, width=100)
        self._left_window.pack(side=tki.LEFT)
        scroll_bar = tki.Scrollbar(self._left_window)
        scroll_bar.pack(side=tki.LEFT, fill=tki.Y)
        text = tki.Text(self._left_window)
        text.insert(tki.INSERT, "test string\ntest")
        text.pack()
        self._canvas = tki.Canvas(self._parent, height=500, width=300)
        self._canvas.pack(side=tki.RIGHT)

root = tki.Tk()
Gui(root)
root.mainloop()

