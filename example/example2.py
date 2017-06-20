import sys
sys.path.insert(0, "../source")
from laminate_Tools import *
from sympy import *

import matplotlib.pyplot as plt
import matplotlib

if __name__ == "__main__":
	max_load_list = []
	load_strain = []
	a = Lamina(4.4e4,1.8e4,8.8e3,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
											Yt = 28,Yc = 140, S = 42,\
											angle = 45,thickness=1)

	b = Lamina(5.4e4,1.8e4,8.8e3,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
											Yt = 28,Yc = 140, S = 42,\
											angle = 65.9,thickness=10)

	print b.matrix_Q_bar
	print '------------------------\n\n'
	LAA = Laminate()
	LAA.add_Lamina(a)
	LAA.add_Lamina(a)
	LAA.update()
	print '----A-----\n\n',LAA.A
	print '\n\n------B------\n\n',LAA.B
	print '\n\n------D------\n\n',LAA.D
	print '******************************\n\n'
	Load = Loading(1,0,0,15)
	Load.apple_to(LAA)
	print Load.laminate_stresses_12
