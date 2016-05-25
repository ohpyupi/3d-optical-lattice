import mathematics as hmath
import numpy as np

def f_return(a):
	if a == "1/2 to 3/2":
		return 0.5
	elif a == "1 to 2":
		return 1
	elif a == "2 to 3":
		return 2
	elif a == "3 to 4":
		return 3
	elif a == "4 to 5":
		return 4
	else:
		print "Error in f_return"

def resol_return(a):
	if a == "low":
		return 30
	elif a == "medium":
		return 60
	elif a == "high":
		return 90
	else:
		print "Error in resol_return"

def polconfig_return(a):
	if a == "in-plane":
		return "inplane"
	elif a == "out-of-plane":
		return "outplane"
	elif a == "user-custom":
		return "stcustom"
	elif a == "standard":
		return "umstandard"
	else:
		print "Error in laser_return"

def custom_return(a, t_x, t_y):
	t_x, t_y = hmath.deg_to_rad(float(t_x)), hmath.deg_to_rad(float(t_y))
	if a == "0":
		return 0
	elif a == "1":
		return 1
	elif a == "-1":
		return -1
	elif a == "cos(theta_x)":
		return np.cos(t_x)
	elif a == "-cos(theta_x)":
		return -np.cos(t_x)
	elif a == "sin(theta_x)":
		return np.sin(t_x)
	elif a == "-sin(theta_x)":
		return -np.sin(t_x)
	elif a == "cos(theta_y)":
		return np.cos(t_y)
	elif a == "-cos(theta_y)":
		return -np.cos(t_y)
	elif a == "sin(theta_y)":
		return np.sin(t_y)
	elif a == "-sin(theta_y)":
		return -np.sin(t_y)
	else:
		return None
