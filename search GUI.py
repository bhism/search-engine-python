# design and devloped by webfun
# youtube channel --webfun
# email webbhalu@gmail.com
#for any kind of help please contact on 9096141591

from tkinter import *
import wikipedia
def get_me():
    entry_value = entry.get()
    answer_value = wikipedia.summary(entry_value)
    answer.delete(1.0,END)
    answer.insert(INSERT, answer_value)

root =Tk()
topframe = Frame(root)
entry = Entry(topframe)
entry.pack( )
button = Button(topframe , text = "search",command = get_me)
button.pack()
topframe.pack(side=TOP)
bottomframe =Frame(root)

scroll =Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill =Y)
answer = Text(bottomframe, width = 30 , height=10, yscrollcommand = scroll.set, wrap = WORD)
answer.pack()

bottomframe.pack()
root.mainloop()
