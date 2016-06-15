#3D Visualization of Optical Lattice

1. Abstract 
2. Installation
  1. Scipy Stack
  2. Cython (optional)
  3. QuTiP
  4. How to start the software
3. Directions
  1. Basic window
  2. Standard Tetrahedron config.
  3. Umbrella-like config.
4. Examples
5. Reference

## 1. Abstract
My master's research began with Brownian motors at Miami University. Brownian motor is a motor that can extract net work from external noise field at certain conditions, such as at non-equilibrium state or at specific symmetry breaking state. One of the physical realization of Brownian motor system is atomic system that lies in optical lattices. Optical lattices originially rise from the interaction between laser-induced dipole moment of atomic system and external laser beam fields. One of the reasons why optical lattices are fit to Brownian motor experiment is that the lattices can be tuned very easily. During my research time, my research collaborator who actually aimed to build optical lattices asked our theory team to build optical lattice simulation software with appropriate graphical user interface(GUI). Thus, as my master's thesis work, I built a GUI software for simulating optical lattices. In our study, we have assumed that the atoms are at low saturation so that the optical pumping time is much longer than the spontaneous emission tiem. In accordance with such conditions, the excited states dependence has bee deleted adiabatically and the optical lattice can be deducted from finding the eigenvalues of the Hamiltonian operator. For the software framework, Python and its libraries, such as Scipy and QuTip have been used. I sincerely wish the software will be used by any scientists who realize optical lattices in lab environments and it will guide their future research.

## 2. Installation

Before using the software, it is required to install few open source Python packages. We will briefly describe how to install the packages based on OS, such as Ubuntu, Mac, and Windows.

#### 2.i Scipy Stack

Scipy stack is a collection of open souce packages for scientific computing in Python. In our software, Numpy and Matplotlib are the primary packages that used for the calculation and visulization of optical lattices.
  
##### Ubuntu

```
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
```

##### Mac

```
sudo port install py27-numpy py27-scipy py27-matplotlib py27-ipython +notebook py27-pandas py27-sympy py27-nose
```

##### Windows

For Windows users, the easiest way to install the packages of Scipy stack is to download one of these Python distributions, which includes all the key packages:

- [Anaconda](https://www.continuum.io/downloads)
- [Enthought Canopy](https://www.enthought.com/products/canopy/)
- [Python(x,y)](http://python-xy.github.io/)
- [WinPython](http://winpython.github.io/)
- [Pyzo](http://www.pyzo.org/)

For more detail on the installation of Scipy Stack, please refer to the [official Scipy document](https://www.scipy.org/install.html)


#### 2.ii Cython (For those who don't use Python distributions above)

If you are Ubuntu user and followed the step above, you might need to additionally install Cython packages manually. One of the recommended way of installing is to get source code from git repository.

##### Ubuntu & Mac

Download latest version of Cython. [Git link](https://github.com/cython/cython)
```
sudo apt-get setup.py install
```

#### 2.iii QuTiP

##### Ubuntu $ Mac

Download the latest version of QuTip. [Official Download Link](http://qutip.org/download.html)
```
sudo apt-get setup.py install
```

##### Windows

- Install the Python(X,Y) distribution (tested with version 2.7.3.1). Other Python distributions, such as Enthought Python Distribution or Anaconda CE have also been reported to work.
- When installing Python(x,y), explicitly select to include the Cython package in the installation. This package is not selected by default.
- Add the following content to the file C:/Python27/Lib/distutils/distutils.cfg (or create the file if it does not already exists):
```
[build]
compiler = mingw32

[build_ext]
compiler = mingw32
```
*The directory where the distutils.cfg file should be placed might be different if you have installed the Python environment in a different location than in the example above.*
- Obtain the QuTiP source code and installed it following the instructions given above.

For more detail on the installation of QuTiP, please refer to [official document link](http://qutip.org/docs/3.1.0/installation.html#installing-from-source)

#### 2.iv How to start the software

Once you are done with all the installation procedure above, you need to download the software using the command 'git clone' on your terminal.
```
git clone https://github.com/ohpyupi/3d-optical-lattice.git
```
Then, go to the directory, type the command
```
cd 3d-optical-lattice
```
To start the software, type the command
```
python optlattice.py
```

Finally, you are ready to use the software and plot optical lattice with your choice of atomic transitions and laser configurations!

## 3. Directions

