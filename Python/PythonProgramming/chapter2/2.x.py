from tkinter.filedialog import askopenfile

filename = askopenfile()
print(filename.read())