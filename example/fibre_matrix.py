import sys
sys.path.insert(0, "../source")
from laminate_Tools import *
import matplotlib.pyplot as plt
import matplotlib

if __name__ == "__main__":
#define lamina from fibre and matrix
	f = Fibre(Ef1 = 74000e6,Ef2 = 74000e6 , Gf12 = 30800e6,vf21 = 0.2,density = 2.55e3)
	m = Matrix(Em = 3300e6 , Gm = 1222e6 , vm = 0.35,density = 1.18e3)

	a = Lamina()
	a.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 ,fibre_volume = 0, \
								Xt = 597.9e6, Xc = 650e6,Yt = 37.7e6, Yc = 130e6, S = 37.5e6,\
								max_stain_t=0.0218,max_stain_c=0.0218,angle = 30,thickness = 1e-3)

	b = Lamina()
	b.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 ,fibre_volume = 0.59, \
								Xt = 597.9e6, Xc = 650e6,Yt = 37.7e6, Yc = 130e6, S = 37.5e6,\
								max_stain_t=0.0218,max_stain_c=0.0218,angle = 60,thickness = 1e-3)
#define lamina directly 

	# aa = Lamina(5.4e4,1.8e4,8.8e3,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
	# 										Yt = 28,Yc = 140, S = 42,\
	# 										angle = 0,thickness=1)

#define laminate
	LA = Laminate()
	LA.add_Lamina(a)
	LA.add_Lamina(b)
	LA.add_Lamina(a)
	# LA.add_Lamina(b)
	# LA.add_Lamina(a)
	# LA.add_Lamina(a)
	# LA.add_Lamina(b)
	# LA.add_Lamina(a)
	# LA.add_Lamina(a)
	# LA.add_Lamina(aa)
	LA.update()

#define load
	Load = Loading(0,10,0,0,0,0)
	Load.apple_to(LA)

#results	
	# print a.matrix_Q,'\n\n'
	# print a.E1,a.E2,a.G12,a.v12,a.v21
	# print '******************************\n\n'

	print '----A-----\n\n',LA.A
	print '\n\n------B------\n\n',LA.B
	print '\n\n------D------\n\n',LA.D
	print LA.THICK
	print '******************************\n\n'
	print Report_stress(Load,layer_num = None,mode = '12')
	print Report_strain(Load,mode = '12')
	# plot_strain(Load,max_ten = None,mode = '12',mode2 = '1')

	P = Puck_Crterion()
	P.Fibre_Failure(Load,layer_num = None)
	print P.ret_list

	P.IFF_Modus_A(Load,layer_num = None)
	print P.ret_list

	P.IFF_Modus_B(Load,layer_num = None)
	print P.ret_list

	P.IFF_Modus_C(Load,layer_num = None)
	print P.ret_list