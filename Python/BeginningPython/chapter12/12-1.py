import tkinter

count = 0
def click():
    global count
    count += 1
    print('I was clicked by {} time(s)'.format(count))

def callback(event):
    print(event.x, event.y)

top = tkinter.Tk()
btn = tkinter.Button()
btn.pack(side='left')
btn['text'] = 'Click me!'
btn['command'] = click
top.bind('<Button-1>', callback)
tkinter.mainloop()