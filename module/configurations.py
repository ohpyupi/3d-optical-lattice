import numpy as np
import qutip as qt
import mathematics as hmath

## Initialization

e1 = np.zeros(3)
e2 = np.zeros(3)
e3 = np.zeros(3)
e4 = np.zeros(3)

k1 = np.zeros(3)
k2 = np.zeros(3)
k3 = np.zeros(3)
k4 = np.zeros(3)

####################################################################################################
## Standard Tetrahedron
####################################################################################################

def standard(t_x, t_y):

	t_x_rad = hmath.deg_to_rad(float(t_x))
	t_y_rad = hmath.deg_to_rad(float(t_y))

	k1 = np.zeros(3)
	k2 = np.zeros(3)
	k3 = np.zeros(3)
	k4 = np.zeros(3)

	k1[0] = np.sin(t_x_rad)
	k1[1] = 0 
	k1[2] = np.cos(t_x_rad)
 
	k2[0] = -np.sin(t_x_rad)
	k2[1] = 0
	k2[2] = np.cos(t_x_rad)

	k3[0] = 0
	k3[1] = np.sin(t_y_rad)
	k3[2] = -np.cos(t_y_rad)

	k4[0] = 0
	k4[1] = -np.sin(t_y_rad)
	k4[2] = -np.cos(t_y_rad)

	standard = np.zeros(4)
	standard = [k1, k2, k3, k4]

	return standard

####################################################################################################
## Standard Tetrahedron - Out-of-plane
####################################################################################################



def stoutplane(t_x_rad, t_y_rad):

	t_x_rad = hmath.deg_to_rad(float(t_x_rad))
	t_y_rad = hmath.deg_to_rad(float(t_y_rad))


	e1[0] = 0
	e1[1] = 1
	e1[2] = 0

	e2[0] = 0
	e2[1] = 1
	e2[2] = 0

	e3[0] = 1
	e3[1] = 0
	e3[2] = 0

	e4[0] = 1
	e4[1] = 0
	e4[2] = 0

	stoutplane = np.zeros(4)
	stoutplane = [e1, e2, e3, e4]
	return stoutplane

####################################################################################################
## Standard Tetrahedron - in-plane
####################################################################################################

def stinplane(t_x, t_y):

	t_x = hmath.deg_to_rad(float(t_x))
	t_y = hmath.deg_to_rad(float(t_y))


	e1[0] = np.cos(t_x)
	e1[1] = 0
	e1[2] = -np.sin(t_x)

	e2[0] = np.cos(t_x)
	e2[1] = 0
	e2[2] = np.sin(t_x)

	e3[0] = 0
	e3[1] = -np.cos(t_y)
	e3[2] = np.sin(t_y)

	e4[0] = 0 
	e4[1] = -np.cos(t_y)
	e4[2] = -np.sin(t_y)

	result = np.zeros(4)
	result = [e1, e2, e3, e4]
	return result

####################################################################################################
## Umbrella
####################################################################################################

def umbrella(mu):

	mu = hmath.deg_to_rad(float(mu))

	k1 = np.zeros(3)
	k2 = np.zeros(3)
	k3 = np.zeros(3)
	k4 = np.zeros(3)
	
	pi_6 = np.pi/6

	k1[0] = -np.sin(mu)
	k1[1] = 0 
	k1[2] = np.cos(mu)
 
	k2[0] = np.sin(mu)*(np.sin(pi_6))
	k2[1] = np.sin(mu)*(-np.cos(pi_6))
	k2[2] = np.cos(mu)

	k3[0] = np.sin(mu)*(np.sin(pi_6))
	k3[1] = np.sin(mu)*(np.cos(pi_6))
	k3[2] = np.cos(mu)

	k4[0] = 0
	k4[1] = 0
	k4[2] = -1

	umbrella = np.zeros(4)
	umbrella = [k1, k2, k3, k4]

	return umbrella

def umpol(mu):

	mu = hmath.deg_to_rad(float(mu))

	e1 = np.zeros(3)
	e2 = np.zeros(3)
	e3 = np.zeros(3)
	e4 = np.zeros(3)
	
	pi_6 = np.pi/6

	e1[0] = 0
	e1[1] = 1 
	e1[2] = 0
 
	e2[0] = np.cos(pi_6)
	e2[1] = np.sin(pi_6)
	e2[2] = 0

	e3[0] = 0
	e3[1] = -np.sin(pi_6)
	e3[2] = np.cos(pi_6)

	e4[0] = 1
	e4[1] = 0
	e4[2] = 0

	umpol = np.zeros(4)
	umpol = [e1, e2, e3, e4]

	return umpol

def umpol2(mu):

	mu = hmath.deg_to_rad(float(mu))

	e1 = np.zeros(3)
	e2 = np.zeros(3)
	e3 = np.zeros(3)
	e4 = np.zeros(3)
	
	pi_6 = np.pi/6

	e1[0] = np.cos(mu)
	e1[1] = 0 
	e1[2] = np.sin(mu)
 
	e2[0] = -np.cos(mu)*(np.sin(pi_6))
	e2[1] = np.cos(mu)*(np.cos(pi_6))
	e2[2] = np.sin(mu)

	e3[0] = -np.cos(mu)*(np.sin(pi_6))
	e3[1] = -np.cos(mu)*(np.cos(pi_6))
	e3[2] = np.sin(mu)

	e4[0] = 0
	e4[1] = 1
	e4[2] = 0

	umpol = np.zeros(4)
	umpol = [e1, e2, e3, e4]

	return umpol


