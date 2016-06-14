#3D Visualization of Optical Lattice

1. Installation
  1. Scipy Stack
  2. Cython (optional)
  3. QuTiP
2. Applications
  1. Single Plots
  2. Double Plots
  3. Silde Plots
  4. Vibrational Frequencies
3. Examples
4. Reference


This software is developed for scientists who work on the realization of optical lattices. For convenience, the graphical user interface has been added to the software for users who does not have deep computer programming backgrounds.

### Installation

Before using the software, it is required to install few open source Python packages. We will briefly describe how to install the packages based on OS, such as Ubuntu, Mac, and Windows.

#### 1. Scipy Stack

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


#### 2. Cython (For those who don't use Python distributions above)

If you are Ubuntu user and followed the step above, you might need to additionall install Cython packages manually. One of the recommended way of installing is to get source code from git repository.

##### Ubuntu & Mac

Download latest version of Cython. [Git link](https://github.com/cython/cython)
```
sudo apt-get setup.py install
```

#### 3. QuTiP

##### Ubuntu $ Mac

Download the latest version of QuTip. [Official Download Link](http://qutip.org/download.html)
```
sudo apt-get setup.py install
```

##### Windows

1. Install the Python(X,Y) distribution (tested with version 2.7.3.1). Other Python distributions, such as Enthought Python Distribution or Anaconda CE have also been reported to work.
2. When installing Python(x,y), explicitly select to include the Cython package in the installation. This package is not selected by default.
3. Add the following content to the file C:/Python27/Lib/distutils/distutils.cfg (or create the file if it does not already exists):
```
[build]
compiler = mingw32

[build_ext]
compiler = mingw32
```
The directory where the distutils.cfg file should be placed might be different if you have installed the Python environment in a different location than in the example above.
4. Obtain the QuTiP source code and installed it following the instructions given above.

For more detail on the installation of QuTiP, please refer to [official document link](http://qutip.org/docs/3.1.0/installation.html#installing-from-source)
