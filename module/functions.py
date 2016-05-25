import numpy as np
import qutip as qt
import mathematics as hmath
from scipy import optimize

####################################################################################

## eigenstates of the system

def eigen(f, a, b):
	if a == 1:
		# returns excited states
		return qt.basis(int(4*(f+1)), int(b+(f+1)))
	elif a == 2:
		# returns ground states
		return qt.basis(int(4*(f+1)), int(b+3*(f+1)))
	else:
		return "Error in function eigen"


####################################################################################

## Polarization

def pol(a):
	el = np.zeros((3, 1), complex)
	el[0][0] = 1.0/np.sqrt(2) 
	el[1][0] = 1.0j/np.sqrt(2)
	el[2][0] = 0

	e = np.zeros((3, 1), complex)
	e[0][0] = 0 
	e[1][0] = 0
	e[2][0] = 1

	er = np.zeros((3, 1), complex)
	er[0][0] = 1.0/np.sqrt(2) 
	er[1][0] = -1.0j/np.sqrt(2)
	er[2][0] = 0

	if a == -1:
		return el
	elif a == 0:
		return e
	elif a == 1:
		return er
	else:
		return "Error in function pol"

####################################################################################

## Clebsch-Gordan Coefficients

def clebsch(f, j, i):
	c = np.zeros((3, int(2*f+1)), complex)
	if f == 0.5:
		c[0][0] = 1.0
		c[1][0] = np.sqrt(2.0/3)
		c[2][0] = np.sqrt(1.0/3)
		c[0][1] = np.sqrt(1.0/3)
		c[1][1] = np.sqrt(2.0/3)
		c[2][1] = 1.0

		if i == -f:
			j = int(j + f + 1)
			return c[j][int(i+f)]
		elif i == -f + 1:
			j = int(j + f)
			return c[j][int(i+f)]
		else:
			return 0.0

	elif f == 1:
		c[0][0] = 1.0
		c[1][0] = np.sqrt(1.0/2)
		c[2][0] = np.sqrt(1.0/6)
		c[0][1] = np.sqrt(1.0/2)
		c[1][1] = np.sqrt(2.0/3)
		c[2][1] = np.sqrt(1.0/2)
		c[0][2] = np.sqrt(1.0/6)
		c[1][2] = np.sqrt(1.0/2)
		c[2][2] = 1.0

		if i == - f:
			j = j + f + 1
			return c[j][i+f]
		elif i == -f + 1:
			j = j + f
			return c[j][i+f]
		elif i == -f + 2:
			j = j + f - 1
			return c[j][i+f]
		else:
			return 0.0

	elif f == 2:
		c[0][0] = 1.0
		c[1][0] = np.sqrt(1.0/3)
		c[2][0] = np.sqrt(1.0/15)
		c[0][1] = np.sqrt(2.0/3)
		c[1][1] = np.sqrt(8.0/15)
		c[2][1] = np.sqrt(1.0/5)
		c[0][2] = np.sqrt(6.0/15)
		c[1][2] = np.sqrt(3.0/5)
		c[2][2] = np.sqrt(6.0/15)
		c[0][3] = np.sqrt(1.0/5)
		c[1][3] = np.sqrt(8.0/15)
		c[2][3] = np.sqrt(2.0/3)
		c[0][4] = np.sqrt(1.0/15)
		c[1][4] = np.sqrt(1.0/3)
		c[2][4] = 1.0

		if i == -f:
			j = j + f + 1
			return c[j][i+f]
		elif i == -f + 1:
			j = j + f
			return c[j][i+f]
		elif i == -f + 2:
			j = j + f - 1
			return c[j][i+f]
		elif i == -f + 3:
			j = j + f - 2
			return c[j][i+f]
		elif i == -f + 4:
			j = j + f - 3
			return c[j][i+f]
		else:
			return 0.0

	elif f == 3:
		c[0][0] = 1.0
		c[1][0] = 1.0/2
		c[2][0] = np.sqrt(1.0/28)
		c[0][1] = np.sqrt(3.0/4)
		c[1][1] = np.sqrt(3.0/7)
		c[2][1] = np.sqrt(3.0/28)
		c[0][2] = np.sqrt(15.0/28)
		c[1][2] = np.sqrt(15.0/28)
		c[2][2] = np.sqrt(3.0/14)
		c[0][3] = np.sqrt(5.0/14)
		c[1][3] = np.sqrt(4.0/7)
		c[2][3] = np.sqrt(5.0/14)
		c[0][4] = np.sqrt(3.0/14)
		c[1][4] = np.sqrt(15.0/28)
		c[2][4] = np.sqrt(15.0/28)
		c[0][5] = np.sqrt(3.0/28)
		c[1][5] = np.sqrt(3.0/7)
		c[2][5] = np.sqrt(3.0/4)
		c[0][6] = np.sqrt(1.0/28)
		c[1][6] = 1.0/2
		c[2][6] = 1.0 

		if i == -f:
			j = j + f + 1
			return c[j][i+f]
		elif i == -f + 1:
			j = j + f
			return c[j][i+f]
		elif i == -f + 2:
			j = j + f - 1
			return c[j][i+f]
		elif i == -f + 3:
			j = j + f - 2
			return c[j][i+f]
		elif i == -f + 4:
			j = j + f - 3
			return c[j][i+f]
		elif i == -f + 5:
			j = j + f - 4
			return c[j][i+f]
		elif i == -f + 6:
			j = j + f - 5
			return c[j][i+f]
		else:
			return 0.0

	elif f == 4:
		c[0][0] = 1.0
		c[1][0] = np.sqrt(9.0/45)
		c[2][0] = np.sqrt(1.0/45)
		c[0][1] = np.sqrt(36.0/45)
		c[1][1] = np.sqrt(16.0/45)
		c[2][1] = np.sqrt(3.0/45)
		c[0][2] = np.sqrt(28.0/45)
		c[1][2] = np.sqrt(21.0/45)
		c[2][2] = np.sqrt(6.0/45)
		c[0][3] = np.sqrt(21.0/45)
		c[1][3] = np.sqrt(24.0/45)
		c[2][3] = np.sqrt(10.0/45)
		c[0][4] = np.sqrt(15.0/45)
		c[1][4] = np.sqrt(25.0/45)
		c[2][4] = np.sqrt(15.0/45)
		c[0][5] = np.sqrt(10.0/45)
		c[1][5] = np.sqrt(24.0/45)
		c[2][5] = np.sqrt(21.0/45)
		c[0][6] = np.sqrt(6.0/45)
		c[1][6] = np.sqrt(21.0/45)
		c[2][6] = np.sqrt(28.0/45)
		c[0][7] = np.sqrt(3.0/45)
		c[1][7] = np.sqrt(16.0/45)
		c[2][7] = np.sqrt(36.0/45)
		c[0][8] = np.sqrt(1.0/45)
		c[1][8] = np.sqrt(9.0/45)
		c[2][8] = 1.0

		if i == -f:
			j = j + f + 1
			return c[j][i+f]
		elif i == -f + 1:
			j = j + f
			return c[j][i+f]
		elif i == -f + 2:
			j = j + f - 1
			return c[j][i+f]
		elif i == -f + 3:
			j = j + f - 2
			return c[j][i+f]
		elif i == -f + 4:
			j = j + f - 3
			return c[j][i+f]
		elif i == -f + 5:
			j = j + f - 4
			return c[j][i+f]
		elif i == -f + 6:
			j = j + f - 5
			return c[j][i+f]
		elif i == -f + 7:
			j = j + f - 6
			return c[j][i+f]
		elif i == -f + 8:
			j = j + f - 7
			return c[j][i+f]
		else:
			return 0.0

	else:
		return "Error in function clebsch"

####################################################################################

## Dipole moment operator constructor

def dipole(f):
	d = 0;
	for i in hmath.frange(-f, f+1):
		for j in range(-1, 2):
			dele = clebsch(f, i+j, i)*np.outer(eigen(f, 1, i+j), eigen(f, 2, i).dag())
			dcomp = np.tensordot(dele, pol(j), axes=0)
			d = d + dcomp
	return d[0][0]

####################################################################################

## Light-shift function

def light_shift(x, y, z, d, laser, pol):

	r = np.zeros(3, complex)
	r[0] = x
	r[1] = y
	r[2] = z

	# Electric field

	E = pol[0]*np.exp(1.0j*(2*np.pi*np.inner(laser[0], r))) + pol[1]*np.exp(1.0j*(2*np.pi*np.inner(laser[1], r))) + pol[2]*np.exp(1.0j*(2*np.pi*np.inner(laser[2], r))) + pol[3]*np.exp(1.0j*(2*np.pi*np.inner(laser[3], r)))
	
	# Hamitonian

	DE = d[0]*E[0] + d[1]*E[1] + d[2]*E[2]
	DE = DE[0]
	DEdag = DE.dag()

	h = np.outer(DEdag, DE)
	h = h[0][0]
	e = -h.eigenenergies()

	return min(e)


####################################################################################

## Optimization for slicing factors

def z_opt(d, laser, pol):
	
	a = []

	for z in range(0, 100):
		z = 0.01*z

		def f(x):

			r = np.zeros(3, complex)
			r[0] = x[0]
			r[1] = x[1]
			r[2] = z

		# Electric field

			E = pol[0]*np.exp(1.0j*(2*np.pi*np.inner(laser[0], r))) + pol[1]*np.exp(1.0j*(2*np.pi*np.inner(laser[1], r))) + pol[2]*np.exp(1.0j*(2*np.pi*np.inner(laser[2], r))) + pol[3]*np.exp(1.0j*(2*np.pi*np.inner(laser[3], r)))
	
		# Hamitonian

			DE = d[0]*E[0] + d[1]*E[1] + d[2]*E[2]
			DE = DE[0]
			DEdag = DE.dag()

			h = np.outer(DEdag, DE)
			h = h[0][0]
			e = -h.eigenenergies()

			return min(e)
	
		opt = optimize.fmin(f, [0.0, 0.0], full_output=1, disp=0)[1]
		a.append(opt)
		mini = min(a)
		
	return 0.01*a.index(mini)

def y_opt(d, laser, pol):
	
	a = []

	for z in range(0, 100):
		z = 0.01*z

		def f(x):

			r = np.zeros(3, complex)
			r[0] = x[0]
			r[1] = z
			r[2] = x[1]

		# Electric field

			E = pol[0]*np.exp(1.0j*(2*np.pi*np.inner(laser[0], r))) + pol[1]*np.exp(1.0j*(2*np.pi*np.inner(laser[1], r))) + pol[2]*np.exp(1.0j*(2*np.pi*np.inner(laser[2], r))) + pol[3]*np.exp(1.0j*(2*np.pi*np.inner(laser[3], r)))
	
		# Hamitonian

			DE = d[0]*E[0] + d[1]*E[1] + d[2]*E[2]
			DE = DE[0]
			DEdag = DE.dag()

			h = np.outer(DEdag, DE)
			h = h[0][0]
			e = -h.eigenenergies()

			return min(e)
	
		opt = optimize.fmin(f, [0.0, 0.0], full_output=1, disp=0)[1]
		a.append(opt)
		mini = min(a)
		
	return 0.01*a.index(mini)

def x_opt(d, laser, pol):
	
	a = []

	for z in range(0, 100):
		z = 0.01*z

		def f(x):

			r = np.zeros(3, complex)
			r[0] = z
			r[1] = x[0]
			r[2] = x[1]

		# Electric field

			E = pol[0]*np.exp(1.0j*(2*np.pi*np.inner(laser[0], r))) + pol[1]*np.exp(1.0j*(2*np.pi*np.inner(laser[1], r))) + pol[2]*np.exp(1.0j*(2*np.pi*np.inner(laser[2], r))) + pol[3]*np.exp(1.0j*(2*np.pi*np.inner(laser[3], r)))
	
		# Hamitonian

			DE = d[0]*E[0] + d[1]*E[1] + d[2]*E[2]
			DE = DE[0]
			DEdag = DE.dag()

			h = np.outer(DEdag, DE)
			h = h[0][0]
			e = -h.eigenenergies()

			return min(e)
	
		opt = optimize.fmin(f, [0.0, 0.0], full_output=1, disp=0)[1]
		a.append(opt)
		mini = min(a)
		
	return 0.01*a.index(mini)


####################################################################################



