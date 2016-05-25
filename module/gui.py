import sys, os, time
from Tkinter import *
from ttk import Frame, Button, Style
import numpy as np
import functions as hfunc
import classes as hclass
import mathematics as hmath
from gui_functions import *
from gui_tetra import *
from gui_umbrella import *

####################################################################################################
## GUI for Initialization
####################################################################################################

class Intro(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()
		self.select_config()
	
	def initUI(self):
		self.parent.title("OPTICAL LATTICE")
		self.style= Style()
		self.style.theme_use("default")
		self.pack(fill=BOTH, expand=1)
	
	def select_config(self):

		def run_standard():
			root = Tk()
			standard = Standard(root)
			root.mainloop()

		def run_umbrella():
			root = Tk()
			umbrella = Umbrella(root)
			root.mainloop()

		ref1 = Label(self)
		ref2 = Label(self)
		ref3 = Label(self)
		ref4 = Label(self)
		owner = Label(self, text="Developer: Hoseong Asher Lee")
		univ = Label(self, text="Miami University, Oxford")
		git = Label(self, text="https://github.com/ohpyupi/optlattices")
		

		label = Label(self, text=" CHOOSE YOUR LASER CONFIGURATION")
		standard = Button(self, text="Standard Tetrahedron", command=run_standard)
		umbrella = Button(self, text="Umbrella", command=run_umbrella)
		quit = Button(self, text="Quit", command=self.quit)

		label.grid(row=0, column=0)	
		ref1.grid(row=1, column=0)
		standard.grid(row=2, column=0)
		ref2.grid(row=3, column=0)
		umbrella.grid(row=4, column=0)

		ref3.grid(row=5, column=0)
		quit.grid(row=6, column=0)
		ref4.grid(row=7)
		owner.grid(row=8)
		univ.grid(row=9)
		git.grid(row=10)

		


