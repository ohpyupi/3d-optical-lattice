import sys, os, time
from Tkinter import *
from ttk import Frame, Button, Style
import numpy as np
import functions as hfunc
import classes as hclass
import mathematics as hmath
from gui_functions import *

####################################################################################################
## GUI for Umbrella Case
####################################################################################################

class Umbrella(Frame):
  
	def __init__(self, parent):
		Frame.__init__(self, parent)   
		self.parent = parent
		self.initUI()
		self.column_0()    

	def initUI(self):
		self.parent.title("UMBRELLA (LIN VERSUS LIN)")
		self.style = Style()
		self.style.theme_use("default")
		self.pack(fill=BOTH, expand=1)
	
	
	def column_0(self):

####################################################################################################
# Functions 
####################################################################################################
		def custom_config():
			a = np.zeros(4, complex)

			e1 = np.zeros(3, complex)
			e2 = np.zeros(3, complex)
			e3 = np.zeros(3, complex)
			e4 = np.zeros(3, complex)

			e1[0] = custom_return(d1.get(), float(theta_x.get()), float(theta_y.get()))
			e1[1] = custom_return(d2.get(), float(theta_x.get()), float(theta_y.get()))
			e1[2] = custom_return(d3.get(), float(theta_x.get()), float(theta_y.get()))

			e2[0] = custom_return(d4.get(), float(theta_x.get()), float(theta_y.get()))
			e2[1] = custom_return(d5.get(), float(theta_x.get()), float(theta_y.get()))
			e2[2] = custom_return(d6.get(), float(theta_x.get()), float(theta_y.get()))

			e3[0] = custom_return(d7.get(), float(theta_x.get()), float(theta_y.get()))
			e3[1] = custom_return(d8.get(), float(theta_x.get()), float(theta_y.get()))
			e3[2] = custom_return(d9.get(), float(theta_x.get()), float(theta_y.get()))

			e4[0] = custom_return(d10.get(), float(theta_x.get()), float(theta_y.get()))
			e4[1] = custom_return(d11.get(), float(theta_x.get()), float(theta_y.get()))
			e4[2] = custom_return(d12.get(), float(theta_x.get()), float(theta_y.get()))

			a = [e1, e2, e3, e4]
			return a
		
		def get_dipole():
			dx =  hfunc.dipole(f_return(f_list.get()))[0]
			dy =  hfunc.dipole(f_return(f_list.get()))[1]
			dz =  hfunc.dipole(f_return(f_list.get()))[2]
			dxs = np.array_str(dx)
			dys = np.array_str(dy)
			dzs = np.array_str(dz)
			content = "D_x = " + dxs + "\n\n" +  "D_y = " + dys + "\n\n" + "D_z = " + dzs
			root = Tk()
			root.title("Dipole moment operator")
			msg = Message(root, text=content)
			msg.config(font=('times', 10))
			msg.pack()
			mainloop()
	
		def get_pol():
			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())

			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			e1 = np.array_str(ham.e1)
			e2 = np.array_str(ham.e2)
			e3 = np.array_str(ham.e3)
			e4 = np.array_str(ham.e4)
			content = "e_1 = " + e1 + "\n" +  "e_2 = " + e2 + "\n" + "e_3 = " + e3 + "\n" + "e_4 = " + e4
			root = Tk()
			root.title("Polarization vectors")
			msg = Message(root, text=content)
			msg.config(font=('times', 10))
			msg.pack()
			mainloop()

		def get_wave():
			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())

			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			k1 = np.array_str(ham.k1)
			k2 = np.array_str(ham.k2)
			k3 = np.array_str(ham.k3)
			k4 = np.array_str(ham.k4)
			content = "k_1 = " + k1 + "\n" +  "k_2 = " + k2 + "\n" + "k_3 = " + k3 + "\n" + "k_4 = " + k4
			root = Tk()
			root.title("Wave vectors")
			msg = Message(root, text=content)
			msg.config(font=('times', 10))
			msg.pack()
			mainloop()

		def get_vib():
			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]


			ham = hclass.Hamiltonian(f, laser_config)
			w_x, w_y = vib_xy = ham.vib_xy(scale2, step)
			w_z = vib_xz = ham.vib_xz(scale2, step)[1]

			w_x, w_y, w_z = str(w_x), str(w_y), str(w_z)

			content = "w_x = " + w_x + "\n" +  "w_y = " + w_y + "\n" + "w_z = " + w_z
			root = Tk()
			root.title("Vibrational frequencies")
			msg = Message(root, text=content)
			msg.config(font=('times', 10))
			msg.pack()
			mainloop()


		def plot_xy():
			time_i = time.time()	

			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			plot = hclass.Plotting(ham)
 			time_f = time.time()

			return plot.plot_xy(scale2, step)

		def plot_xz():
			time_i = time.time()	

			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			plot = hclass.Plotting(ham)
 			time_f = time.time()

			return plot.plot_xz(scale2, step)

		def plot_yz():
			time_i = time.time()	

			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			plot = hclass.Plotting(ham)
 			time_f = time.time()

			return plot.plot_yz(scale2, step)

		def plot_double_xyxz():
			time_i = time.time()	

			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			plot = hclass.Plotting(ham)
 			time_f = time.time()

			return plot.plot_double_xyxz(scale2, step)
		
		def plot_double_xyyz():
			time_i = time.time()	

			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			plot = hclass.Plotting(ham)
 			time_f = time.time()

			return plot.plot_double_xyyz(scale2, step)

		def plot_double_yzxz():
			time_i = time.time()	

			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			plot = hclass.Plotting(ham)
 			time_f = time.time()

			return plot.plot_double_yzxz(scale2, step)


		def save_xy():

			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			plot = hclass.Plotting(ham)

			starting_var = float(starting.get())
			ending_var = float(ending.get())
			num_slice_var = int(num_slice.get())
			
			for i in range(0, num_slice_var):
				j = starting_var + 1.0*i*(ending_var-starting_var)/num_slice_var
				plot.xy_contour_save(scale2, step, j, "figures/umbrella/xy/%d" %i)

		def save_yz():

			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			plot = hclass.Plotting(ham)

			starting_var = float(starting.get())
			ending_var = float(ending.get())
			num_slice_var = int(num_slice.get())
			
			for i in range(0, num_slice_var):
				i = starting_var + 1.0*i*ending_var/num_slice_var
				plot.yz_contour_save(scale2, step, i, "figures/umbrella/yz/%d" % int((i-starting_var)*num_slice_var))

		def save_xz():

			f = f_return(f_list.get())
			m = float(mu.get())
			confignick = polconfig_return(polconfig_list.get())
			scale2 = float(scale.get())
			step = resol_return(resol_list.get())
	
			if confignick == "umstandard":
				laser_config = [confignick, m]
			elif confignick == "umcustom":
				config = custom_config()
				laser_config = [confignick, m, config]

			ham = hclass.Hamiltonian(f, laser_config)
			plot = hclass.Plotting(ham)

			starting_var = float(starting.get())
			ending_var = float(ending.get())
			num_slice_var = int(num_slice.get())
			
			for i in range(0, num_slice_var):
				i = starting_var + 1.0*i*ending_var/num_slice_var
				plot.xz_contour_save(scale2, step, i, "figures/tetrahedron/xz/%d" % int((i-starting_var)*num_slice_var))


####################################################################################################
# Interfaces
####################################################################################################

		Label(self, text="VARIABLES").grid(row=0, column=0)
		f = Label(self, text="Transition").grid(row=1, column=0)
		mu = Label(self, text="mu").grid(row=2, column=0)
		laserconfig = Label(self, text="Laser Configurations").grid(row=3, column=0)
		polconfig = Label(self, text="Polarization Configurations").grid(row=4, column=0)
		scale = Label(self, text="Scale").grid(row=5, column=0)
		resol = Label(self, text="Resolution").grid(row=6, column=0)

####################################################################################################
# Input -- column 1
####################################################################################################

		f_list = StringVar(self)
		f_list.set("1/2 to 3/2")
		resol_list = StringVar(self)
		resol_list.set("medium")
		laserconfig_list = StringVar(self)
		laserconfig_list.set("Umbrella")
		polconfig_list = StringVar(self)
		polconfig_list.set("standard")

		Label(self, text="USER INPUTS").grid(row=0, column=1)	
		f = OptionMenu(self, f_list, "1/2 to 3/2", "1 to 2", "2 to 3", "3 to 4", "4 to 5")
		mu = Entry(self)
		laserconfig = OptionMenu(self, laserconfig_list, "Umbrella")
		polconfig = OptionMenu(self, polconfig_list, "standard")
		scale = Entry(self)
		resol = OptionMenu(self, resol_list, "low", "medium", "high")

		mu.insert(10,"30.0")
		scale.insert(10,"1.0")
	
		f.grid(row=1, column=1)
		mu.grid(row=2, column=1)
		laserconfig.grid(row=3, column=1)
		polconfig.grid(row=4, column=1)
		scale.grid(row=5, column=1)
		resol.grid(row=6, column=1)

####################################################################################################
# Slide 
####################################################################################################

		Label(self, text="SLIDE IMAGES").grid(row=0, column=2)
		Label(self, text="Number of slices").grid(row=0, column=4)
		num_slice = Entry(self)

		Label(self, text="Range").grid(row=1, column=2)
		Label(self, text="../figures/umbrella/").grid(row=2, column=2)
		starting = Entry(self)	
		Label(self, text="to").grid(row=2, column=4)
		ending = Entry(self)

		num_slice.grid(row=0, column=5)
		starting.grid(row=1, column=3)
		ending.grid(row=1, column=5)


		starting.insert(10,"0.0")
		ending.insert(10,"1.0")
		num_slice.insert(10,"10")
	
		Button(self, text="SAVE XY SLIDES", command=save_xy).grid(row=2, column=3)
		Button(self, text="SAVE YZ SLIDES", command=save_yz).grid(row=2, column=4)
		Button(self, text="SAVE XZ SLIDES", command=save_xz).grid(row=2, column=5)

####################################################################################################
# Plotting
####################################################################################################

		Label(self, text="Plotting").grid(row=3, column=2)
		Label(self).grid(row=3, column=3)
		Label(self).grid(row=3, column=4)
		Label(self).grid(row=3, column=5)
		Button(self, text="Plot XY", command=plot_xy).grid(row=4, column=3)
		Button(self, text="Plot XZ", command=plot_xz).grid(row=4, column=4)
		Button(self, text="Plot YZ", command=plot_yz).grid(row=4, column=5)

		plot = Button(self, text='Plot XY&XZ', command=plot_double_xyxz).grid(row=5, column=3)
		plot = Button(self, text='Plot XY&YZ', command=plot_double_xyyz).grid(row=5, column=4)
		plot = Button(self, text='Plot YZ&XZ', command=plot_double_yzxz).grid(row=5, column=5)

####################################################################################################
# Command 
####################################################################################################

		Label(self, text="COMMAND").grid(row=9, column=0)

		dipole = Button(self, text='GET DIPOLE MOMENT', command=get_dipole).grid(row=11, column=0)
		vibfreq = Button(self, text='GET VIBRATIONAL FREQUENCY', command=get_vib).grid(row=11, column=1)
		pol = Button(self, text='GET POLARIZATIONS', command=get_pol).grid(row=12, column=0)
		wave = Button(self, text='GET WAVE VECTORS', command=get_wave).grid(row=12, column=1)

