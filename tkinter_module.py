from tkinter import * #won't have to type tkinter befire using any function of this module
from PIL import Image, ImageTk

class Window(Frame):#Frame is imported from tkinter

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master=master
		self.init_window()

	def init_window(self):
		self.master.title("Simple")#setting a title of a window
		self.pack(fill=BOTH, expand=1)#says that we're filling up a window and we need resizing of the window
		
		menu=Menu(self.master)#Menu is built into tkinter
		self.master.config(menu=menu)

		file=Menu(menu)
		file.add_command(label='Exit', command=self.client_exit)
		menu.add_cascade(label='File', menu=file)

		edit=Menu(menu)
		edit.add_command(label='Show Image', command=self.showImage)
		edit.add_command(label='Show Text', command=self.showTxt)
		menu.add_cascade(label='Edit', menu=edit)

	def client_exit(self):
		exit() 

	def showImage(self):
		img=Image.open("715.jpg")#using Image from PIL
		render=ImageTk.PhotoImage(img)
		imglabel=Label(self, image=render)#labels are used to pack text or images
		imglabel.image=render
		imglabel.place(x=0, y=0)

	def showTxt(self):
		text=Label(self, text="Hey there good lookin!")
		text.pack()

root=Tk()
root.geometry("400x300")#setting the size of default window
app=Window(root)
root.mainloop()
