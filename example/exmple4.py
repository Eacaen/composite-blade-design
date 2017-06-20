import sys
sys.path.insert(0, "../source")
from laminate_Tools import *
import matplotlib.pyplot as plt
import matplotlib
#the chinese book example P31
if __name__ == "__main__":
	max_load_list = []
	load_strain = []
	a = Lamina(53.74,17.95,8.63,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
											Yt = 28,Yc = 140, S = 42,\
											angle = 0,thickness=1)

	b = Lamina(53.74,17.95,8.63,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
											Yt = 28,Yc = 140, S = 42,\
											angle = 60,thickness=10)

 	c = Lamina(53.74,17.95,8.63,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
											Yt = 28,Yc = 140, S = 42,\
											angle = 70,thickness=10)

	LAA = Laminate()
	# LAA.add_Lamina(a)
	LAA.add_Lamina(a)
	LAA.add_Lamina(b)	
	LAA.add_Lamina(c) 
	# LAA.add_Lamina(a)
	LAA.update()

	print '----A-----\n\n',LAA.A
	print '\n\n------B------\n\n',LAA.B
	print '\n\n------D------\n\n',LAA.D

	Load = Loading(1,0,0)
	Load.apple_to(LAA)
	print Report_strain(Load,layer_num = 1,mode = 'xy')
	print Report_stress(Load,layer_num = 1,mode = 'xy')
	print Load.laminate_loaded.lamina_list
	print Load.laminate_loaded.lamina_num