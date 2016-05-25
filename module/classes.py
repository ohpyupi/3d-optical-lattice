import sys, os, time
import numpy as np
import functions as hfunc
import configurations as hconfig
import mathematics as hmath

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

class Hamiltonian:

	def __init__(self, f, laser_configuration):

		# laser_configuration = ["inplane", [t_x, t_y]]
		# laser_configuration = ["outplane", [t_x, t_y]]
		# laser_configuration = ["stcustom", [t_x, t_y], polconfig]
		#	laser_configuration =	["umstandard", mu]
		# laser_congifuration = ["umcustom", mu, polconfig]
		self.f = float(f)
		self.dipole = hfunc.dipole(f)
		if laser_configuration[0] == "inplane":
			self.t_x = laser_configuration[1][0]
			self.t_y = laser_configuration[1][1]
			self.lasernick = "standard tetrahedron"
			self.laserconfig = hconfig.standard(self.t_x, self.t_y)
			self.polconfig = hconfig.stinplane(self.t_x, self.t_y)

		elif laser_configuration[0] == "outplane":
			self.t_x = laser_configuration[1][0]
			self.t_y = laser_configuration[1][1]
			self.lasernick = "standard tetrahedron"
			self.laserconfig = hconfig.standard(self.t_x, self.t_y)
			self.polconfig = hconfig.stoutplane(self.t_x, self.t_y)

		elif laser_configuration[0] == "stcustom":
			self.t_x = laser_configuration[1][0]
			self.t_y = laser_configuration[1][1]
			self.lasernick = "standard tetrahedron"
			self.laserconfig = hconfig.standard(self.t_x, self.t_y)
			self.polconfig = laser_configuration[2]

		elif laser_configuration[0] == "umstandard":
			self.mu = laser_configuration[1]
			self.lasernick = "umbrella"
			self.laserconfig = hconfig.umbrella(self.mu)
			self.polconfig = hconfig.umpol(self.mu)
		
		elif laser_configuration[0] == "umcustom":
			self.mu = laser_configuration[1]
			self.lasernick = "umbrella"
			self.laserconfig = hconfig.umbrella(self.mu)
			self.polconfig = laser_configuration[2]

		else:
			print "Error in Beamsplitting Class laser_configuration"

		self.e1 = self.polconfig[0]
		self.e2 = self.polconfig[1]
		self.e3 = self.polconfig[2]
		self.e4 = self.polconfig[3]
		self.k1 = self.laserconfig[0]
		self.k2 = self.laserconfig[1]
		self.k3 = self.laserconfig[2]
		self.k4 = self.laserconfig[3]

	def show_polarization(self):
		print "e_0 = (%2f, %2f, %2f)" % (self.e1[0], self.e1[1], self.e1[2])
		print "e_1 = (%2f, %2f, %2f)" % (self.e2[0], self.e2[1], self.e2[2])
		print "e_2 = (%2f, %2f, %2f)" % (self.e3[0], self.e3[1], self.e3[2])
		print "e_3 = (%2f, %2f, %2f)" % (self.e4[0], self.e4[1], self.e4[2])

	def show_wavevectors(self):
		print "k_0 = (%2f, %2f, %2f)" % (self.k1[0], self.k1[1], self.k1[2])
		print "k_1 = (%2f, %2f, %2f)" % (self.k2[0], self.k2[1], self.k2[2])
		print "k_2 = (%2f, %2f, %2f)" % (self.k3[0], self.k3[1], self.k3[2])
		print "k_3 = (%2f, %2f, %2f)" % (self.k4[0], self.k4[1], self.k4[2])

## Maximized light shift (Optical lattice)

	def xy_shift(self, scale, step):
		global z_min
		z_min = hfunc.z_opt(self.dipole, self.laserconfig, self.polconfig)
		shift = np.zeros((step+1, step+1), complex)
		
		for x in range(0, step+1):
			for y in range(0, step+1):
				xp = -scale + 2*scale/step*x
				yp = -scale + 2*scale/step*y
				shift[y][x] = hfunc.light_shift(xp, yp, z_min, self.dipole, self.laserconfig, self.polconfig)
  
		return shift.real

	def xz_shift(self, scale, step):
		global y_min
		y_min = hfunc.y_opt(self.dipole, self.laserconfig, self.polconfig)
		shift = np.zeros((step+1, step+1), complex)
		
		for x in range(0, step+1):
			for y in range(0, step+1):
				xp = -scale + 2*scale/step*x
				yp = -scale + 2*scale/step*y
				shift[y][x] = hfunc.light_shift(xp, y_min, yp, self.dipole, self.laserconfig, self.polconfig)

		return shift.real
	
	def yz_shift(self, scale, step):
		global x_min
		x_min = hfunc.x_opt(self.dipole, self.laserconfig, self.polconfig)
		shift = np.zeros((step+1, step+1), complex)
		
		for x in range(0, step+1):
			for y in range(0, step+1):
				xp = -scale + 2*scale/step*x
				yp = -scale + 2*scale/step*y
				shift[y][x] = hfunc.light_shift(x_min, xp, yp, self.dipole, self.laserconfig, self.polconfig)

		return shift.real

## Vibrational frequencies along Cartesian

	def vib_xy(self, scale, step):
		lattice = self.xy_shift(scale, step)

		index = np.where(lattice == lattice.min())

		index_x, index_y = index[1][0], index[0][0]
		xl, yl = lattice[index_y, :], lattice[:, index_x]
		ddx, ddy = np.gradient(np.gradient(xl)), np.gradient(np.gradient(yl))

		return ddx[index_x], ddy[index_y]

	def vib_xz(self, scale, step):
		lattice = self.xz_shift(scale, step)

		index = np.where(lattice == lattice.min())

		index_x, index_y = index[1][0], index[0][0]
		xl, yl = lattice[index_y, :], lattice[:, index_x]
		ddx, ddy = np.gradient(np.gradient(xl)), np.gradient(np.gradient(yl))

		return ddx[index_x], ddy[index_y]

	def vib_yz(self, scale, step):
		lattice = self.yz_shift(scale, step)

		index = np.where(lattice == lattice.min())

		index_x, index_y = index[1][0], index[0][0]
		xl, yl = lattice[index_y, :], lattice[:, index_x]
		ddx, ddy = np.gradient(np.gradient(xl)), np.gradient(np.gradient(yl))

		return ddx[index_x], ddy[index_y]

## General calculation

	def xy_shift_general(self, scale, step, z):
		shift = np.zeros((step+1, step+1), complex)
		
		for x in range(0, step+1):
			for y in range(0, step+1):
				xp = -scale + 2*scale/step*x
				yp = -scale + 2*scale/step*y
				shift[y][x] = hfunc.light_shift(xp, yp, z, self.dipole, self.laserconfig, self.polconfig)
  
		return shift.real

	def xz_shift_general(self, scale, step, z):
		shift = np.zeros((step+1, step+1), complex)
		
		for x in range(0, step+1):
			for y in range(0, step+1):
				xp = -scale + 2*scale/step*x
				yp = -scale + 2*scale/step*y
				shift[y][x] = hfunc.light_shift(xp, z, yp, self.dipole, self.laserconfig, self.polconfig)
  
		return shift.real

	def yz_shift_general(self, scale, step, z):
		shift = np.zeros((step+1, step+1), complex)
		
		for x in range(0, step+1):
			for y in range(0, step+1):
				xp = -scale + 2*scale/step*x
				yp = -scale + 2*scale/step*y
				shift[y][x] = hfunc.light_shift(z, xp, yp, self.dipole, self.laserconfig, self.polconfig)
  
		return shift.real

class Plotting:

	def __init__(self, ham):
		self.hamiltonian = ham

## Draw

	def xy_contour_draw(self, scale, step):

		X = np.arange(-scale, scale + 2*scale/step, 2*scale/step)
		Y = np.arange(-scale, scale + 2*scale/step, 2*scale/step)

		z = self.hamiltonian.xy_shift(scale, step)

		ax = plt.pcolor(X, Y, z, cmap='RdBu_r')	
		plt.colorbar()
		plt.xlabel(r'$X/lambda$')
		plt.ylabel(r'$Y/lambda$')
		plt.title('XY plane with Z = %.02f' %z_min)
		plt.axis([-scale, scale, -scale, scale])

		return ax

	def xz_contour_draw(self, scale, step):
	
		X = np.arange(-scale, scale + 2*scale/step, 2*scale/step)
		Y = np.arange(-scale, scale + 2*scale/step, 2*scale/step)

		z = self.hamiltonian.xz_shift(scale, step)

		ax = plt.pcolor(X, Y, z, cmap='RdBu_r')	
		plt.colorbar()
		plt.xlabel(r'$X/lambda$')
		plt.ylabel(r'$Z/lambda$')
		plt.title('XZ plane with Y = %.02f' %y_min)
		plt.axis([-scale, scale, -scale, scale])

		return ax

	def yz_contour_draw(self, scale, step):
	
		X = np.arange(-scale, scale + 2*scale/step, 2*scale/step)
		Y = np.arange(-scale, scale + 2*scale/step, 2*scale/step)

		z = self.hamiltonian.yz_shift(scale, step)

		ax = plt.pcolor(X, Y, z, cmap='RdBu_r')	
		plt.colorbar()
		plt.xlabel(r'$Y/lambda$')
		plt.ylabel(r'$Z/lambda$')
		plt.title('YZ plane with X = %.02f' %x_min)
		plt.axis([-scale, scale, -scale, scale])

		return ax

## Plot

### single plots

	def plot_xy(self, scale, step):
		time_i = time.time()

		fig = plt.figure()
		self.xy_contour_draw(scale, step)
		plt.title('XY plane with Z_min = %.02f' %z_min)

		time_f = time.time()
		t_con = time_f - time_i

		if hasattr(self.hamiltonian, "t_x") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Standard Tetrahedron laser configuration.\n Parameters: theta_x = %.02f, and theta_y = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.t_x, self.hamiltonian.t_y, t_con), fontsize=15)

		elif hasattr(self.hamiltonian, "mu") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Umbrella-like laser configuration.\n Parameters: mu = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.mu, t_con), fontsize=15)

		plt.show()

	def plot_xz(self, scale, step):
		time_i = time.time()

		fig = plt.figure()
		self.xz_contour_draw(scale, step)
		plt.title('XZ plane with Y_min = %.02f' %y_min)

		time_f = time.time()
		t_con = time_f - time_i

		if hasattr(self.hamiltonian, "t_x") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Standard Tetrahedron laser configuration.\n Parameters: theta_x = %.02f, and theta_y = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.t_x, self.hamiltonian.t_y, t_con), fontsize=15)

		elif hasattr(self.hamiltonian, "mu") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Umbrella-like laser configuration.\n Parameters: mu = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.mu, t_con), fontsize=15)

		plt.show()

	def plot_yz(self, scale, step):
		time_i = time.time()

		fig = plt.figure()
		self.yz_contour_draw(scale, step)
		plt.title('YZ plane with X_min = %.02f' %x_min)

		time_f = time.time()
		t_con = time_f - time_i

		if hasattr(self.hamiltonian, "t_x") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Standard Tetrahedron laser configuration.\n Parameters: theta_x = %.02f, and theta_y = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.t_x, self.hamiltonian.t_y, t_con), fontsize=15)

		elif hasattr(self.hamiltonian, "mu") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Umbrella-like laser configuration.\n Parameters: mu = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.mu, t_con), fontsize=15)

		plt.show()

### double plots

	def plot_double_xyxz(self, scale, step):
		
		time_i = time.time()

		fig = plt.figure()

		plt.subplot(1, 2, 1)
		self.xy_contour_draw(scale, step)

		plt.subplot(1, 2, 2)
		self.xz_contour_draw(scale, step)
		time_f = time.time()
		t_con = time_f - time_i


		if hasattr(self.hamiltonian, "t_x") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Standard Tetrahedron laser configuration.\n Parameters: theta_x = %.02f, and theta_y = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.t_x, self.hamiltonian.t_y, t_con), fontsize=15)

		elif hasattr(self.hamiltonian, "mu") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Umbrella-like laser configuration.\n Parameters: mu = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.mu, t_con), fontsize=15)

		plt.show()
	
	def plot_double_xyyz(self, scale, step):
		
		time_i = time.time()

		fig = plt.figure()

		plt.subplot(1, 2, 1)
		self.xy_contour_draw(scale, step)

		plt.subplot(1, 2, 2)
		self.yz_contour_draw(scale, step)
		time_f = time.time()
		t_con = time_f - time_i


		if hasattr(self.hamiltonian, "t_x") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Standard Tetrahedron laser configuration.\n Parameters: theta_x = %.02f, and theta_y = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.t_x, self.hamiltonian.t_y, t_con), fontsize=15)

		elif hasattr(self.hamiltonian, "mu") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Umbrella-like laser configuration.\n Parameters: mu = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.mu, t_con), fontsize=15)

		plt.show()
		
	def plot_double_yzxz(self, scale, step):
		
		time_i = time.time()

		fig = plt.figure()

		plt.subplot(1, 2, 1)
		self.yz_contour_draw(scale, step)

		plt.subplot(1, 2, 2)
		self.xz_contour_draw(scale, step)
		time_f = time.time()
		t_con = time_f - time_i


		if hasattr(self.hamiltonian, "t_x") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Standard Tetrahedron laser configuration.\n Parameters: theta_x = %.02f, and theta_y = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.t_x, self.hamiltonian.t_y, t_con), fontsize=15)

		elif hasattr(self.hamiltonian, "mu") == True:
			fig.suptitle('Optical lattice of an atomic system with J_g = %.01f in 3D Umbrella-like laser configuration.\n Parameters: mu = %.02f. Simulation time: %.02f seconds' %(self.hamiltonian.f, self.hamiltonian.mu, t_con), fontsize=15)

		plt.show()

## Save

	def xy_contour_save(self, scale, step, z, filename):
		time_i = time.time()
		fig = plt.figure(figsize=(9.5,8))
		X = np.arange(-scale, scale + 2*scale/step, 2*scale/step)
		Y = np.arange(-scale, scale + 2*scale/step, 2*scale/step)

		z_a = self.hamiltonian.xy_shift_general(scale, step, z)

		plt.subplot(1, 1, 1)
		ax = plt.pcolor(X, Y, z_a, cmap='RdBu_r')	
		plt.subplots_adjust(top=0.84)
		plt.colorbar()
		plt.xlabel(r'$X/lambda$')
		plt.ylabel(r'$Y/lambda$')
		plt.title('XY plane with Z = %.02f' %z)
		plt.axis([-scale, scale, -scale, scale])

		time_f = time.time()
		t_con = time_f - time_i

		if hasattr(self.hamiltonian, "t_x") == True:
			fig.suptitle('3D optical lattice within Standard Tetrahedron.\n Parameters: F = %.02f, theta_x = %.02f, and theta_y = %.02f.\n Saved at ../%s.png' %(self.hamiltonian.f, self.hamiltonian.t_x, self.hamiltonian.t_y, filename), fontsize=15)

		elif hasattr(self.hamiltonian, "mu") == True:
			fig.suptitle('3D optical lattice within Ubrella.\n Parameters: F = %.02f, mu = %.02f.' %(self.hamiltonian.f, self.hamiltonian.mu), fontsize=15)

		plt.savefig(filename)

	def xz_contour_save(self, scale, step, y, filename):
		time_i = time.time()
		fig = plt.figure(figsize=(9.5,8))
		X = np.arange(-scale, scale + 2*scale/step, 2*scale/step)
		Y = np.arange(-scale, scale + 2*scale/step, 2*scale/step)

		z = self.hamiltonian.xz_shift_general(scale, step, y)

		plt.subplot(1, 1, 1)
		ax = plt.pcolor(X, Y, z, cmap='RdBu_r')	
		plt.subplots_adjust(top=0.84)
		plt.colorbar()
		plt.xlabel(r'$X/lambda$')
		plt.ylabel(r'$Z/lambda$')
		plt.title('XY plane with Y = %.02f' %y)
		plt.axis([-scale, scale, -scale, scale])

		time_f = time.time()
		t_con = time_f - time_i

		if hasattr(self.hamiltonian, "t_x") == True:
			fig.suptitle('3D optical lattice within Standard Tetrahedron.\n Parameters: F = %.02f, theta_x = %.02f, and theta_y = %.02f.' %(self.hamiltonian.f, self.hamiltonian.t_x, self.hamiltonian.t_y), fontsize=15)

		elif hasattr(self.hamiltonian, "mu") == True:
			fig.suptitle('3D optical lattice within Ubrella.\n Parameters: F = %.02f, mu = %.02f.' %(self.hamiltonian.f, self.hamiltonian.mu), fontsize=15)


		plt.savefig(filename)

	def yz_contour_save(self, scale, step, x, filename):
		time_i = time.time()
		fig = plt.figure(figsize=(9.5,8))
		X = np.arange(-scale, scale + 2*scale/step, 2*scale/step)
		Y = np.arange(-scale, scale + 2*scale/step, 2*scale/step)

		z = self.hamiltonian.yz_shift_general(scale, step, x)
		plt.subplot(1, 1, 1)
		ax = plt.pcolor(X, Y, z, cmap='RdBu_r')	
		plt.subplots_adjust(top=0.84)
		plt.colorbar()
		plt.xlabel(r'$Y/lambda$')
		plt.ylabel(r'$Z/lambda$')
		plt.title('YZ plane with X = %.02f' %x)
		plt.axis([-scale, scale, -scale, scale])

		time_f = time.time()
		t_con = time_f - time_i


		if hasattr(self.hamiltonian, "t_x") == True:
			fig.suptitle('3D optical lattice within Standard Tetrahedron.\n Parameters: F = %.02f, theta_x = %.02f, and theta_y = %.02f.' %(self.hamiltonian.f, self.hamiltonian.t_x, self.hamiltonian.t_y), fontsize=15)

		elif hasattr(self.hamiltonian, "mu") == True:
			fig.suptitle('3D optical lattice within Ubrella.\n Parameters: F = %.02f, mu = %.02f.' %(self.hamiltonian.f, self.hamiltonian.mu), fontsize=15)

		plt.savefig(filename)




