import tkinter as tki
import socket
import sys

MSGDELIM = b'\n'
DELIM = b';'
FIELDSEP = b','
MAX_MSG_SIZE = 1048

class Gui:
    def __init__(self,parent):
        self._parent = parent
        menu = tki.Menu(parent)
        self._parent.config(menu=menu)
        helpmenu = tki.Menu(menu)
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


        toolbarFrame.pack(side=tki.TOP)

        # creating the canvas and left users window
        self._left_window = tki.Frame(self._parent, height=150, width=10)
        self._left_window.pack(side=tki.LEFT)
        scroll_bar = tki.Scrollbar(self._left_window)
        scroll_bar.pack(side=tki.LEFT, fill=tki.Y)
        self.text = tki.Text(self._left_window, width=30)
        self.text.pack()
        self._canvas_window = tki.Frame(self._parent)
        self._canvas = tki.Canvas(self._canvas_window, height=500, width=500,
                                  bg="black")

        self._canvas.pack(side=tki.RIGHT)
        self._canvas_window.pack(side=tki.RIGHT)
        msg_list=self.myreceiver()
        self.msgs_handler(msg_list)

    def myreceiver(self):
        '''receives a msg/msgs decodes it and returns a list of separated
        msgs '''
        print('hi')
        msg_list=[]
        try:
            s.settimeout(5)
            data=s.recv(MAX_MSG_SIZE)
            msg_list=data.split(MSGDELIM)
            for i in msg_list:
                i=i.decode()
            print(msg_list)
            return msg_list
        except:
            return msg_list


    def msgs_handler(self,msg_list):
        ''''''
        for msg in msg_list:
            msg=msg.decode()
            if 'users' in msg:
                sep_msg=msg.split(';')
                self.update_users(sep_msg[1])

    def update_users(self,users_string):
        users_list=users_string.split(',')
        for user in users_list:
            self.text.insert(tki.INSERT, user+'\n')




if __name__ == '__main__':
    ############################################## connecting to server
    if len(sys.argv) < 5:
        print('Usage : python client.py <host> <port> <user_name> '
              '<group_name>')
    host = sys.argv[1]
    port = int(sys.argv[2])
    user_name=bytes(sys.argv[3],'ascii')
    group_name=bytes(sys.argv[4],'ascii')
    s=socket.socket()
    s.connect((host,port))
    s.sendall(b'join'+DELIM+user_name+DELIM+group_name+MSGDELIM)
    ###############################################

#s=socket.socket()
#s.connect(('localhost',5678))
#s.sendall(b'join;rubi;gddd')
    root = tki.Tk()
    game=Gui(root)
    root.mainloop()

