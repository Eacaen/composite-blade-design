import sys
sys.path.insert(0, "../source")
import read_exe
import profile
import open_profile
from graph import *
from graph_plugin import *
from profile_plugin import *
from beam import *
from laminate_Tools import *
import close_profile




if __name__ == "__main__":
# define lamina from fibre and matrix
	UUNN = 1.0

	f = Fibre(Ef1 = 74000,Ef2 = 74000 , Gf12 = 30800,vf21 = 0.2,density = 2.55e-3)
	m = Matrix(Em = 3300 , Gm = 1222 , vm = 0.35,density = 1.18e-3)

	lamina_THK = 0.125
	a0 = Lamina()
	a0.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 ,\
								Xt = 597.9, Xc = 650,Yt = 37.7, Yc = 130, S = 37.5,\
												angle = 0,thickness = lamina_THK)
 
	b90 = Lamina()
	b90.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 , \
								Xt = 597.9, Xc = 650,Yt = 37.7, Yc = 130, S = 37.5,\
												angle = 90,thickness = lamina_THK)
######################################################################################
	b45 = Lamina()
	b45.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 , \
								Xt = 597.9, Xc = 650,Yt = 37.7, Yc = 130, S = 37.5,\
												angle = 45,thickness = lamina_THK)
	b_45 = Lamina()
	b_45.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 , \
								Xt = 597.9, Xc = 650,Yt = 37.7, Yc = 130, S = 37.5,\
 											angle = 45,thickness = lamina_THK)

 

# 	f = Fibre(Ef1 = 74000e6,Ef2 = 74000e6, Gf12 = 30800e6,vf21 = 0.2,density = 2.55e3)
# 	m = Matrix(Em = 3300e6, Gm = 1222e6, vm = 0.35,density = 1.18e3)

# 	lamina_THK = 0.125 / UUNN
# 	a0 = Lamina()
# 	a0.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 ,\
# 								Xt = 597.9e6, Xc = 650e6,Yt = 37.7e6, Yc = 130e6, S = 37.5e6,\
# 												angle = 0,thickness = lamina_THK)
 
# 	b90 = Lamina()
# 	b90.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 , \
# 								Xt = 597.9e6, Xc = 650e6,Yt = 37.7e6, Yc = 130e6, S = 37.5e6,\
# 												angle = 90,thickness = lamina_THK)
# ######################################################################################
# 	b45 = Lamina()
# 	b45.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 , \
# 								Xt = 597.9e6, Xc = 650e6,Yt = 37.7e6, Yc = 130e6, S = 37.5e6,\
# 												angle = 45,thickness = lamina_THK)
# 	b_45 = Lamina()
# 	b_45.Fibre_Matrix_Lamina(f,m ,fibre_mass = 0.4 , \
# 								Xt = 597.9e6, Xc = 650e6,Yt = 37.7e6, Yc = 130e6, S = 37.5e6,\
#  											angle = 45,thickness = lamina_THK)
#define laminate
	SKIN = Laminate()
	SKIN.add_Lamina(b45)
	SKIN.add_Lamina(b_45)
	SKIN.add_Lamina(b45)
 	SKIN.update()

	WEB = Laminate()
	WEB.add_Lamina(b_45)
 	WEB.add_Lamina(b45)
	WEB.add_Lamina(b_45)
	WEB.add_Lamina(b45)
	WEB.add_Lamina(b_45)
	WEB.add_Lamina(b45)
	WEB.add_Lamina(b_45)
	WEB.add_Lamina(b45)
	WEB.add_Lamina(b_45)
	WEB.add_Lamina(b45)
	WEB.add_Lamina(b_45)
	WEB.add_Lamina(b45)
	WEB.add_Lamina(b_45)
 	WEB.update()

	CAP = Laminate()
	CAP.add_Lamina(a0)
	CAP.add_Lamina(b90)
	CAP.add_Lamina(a0)
	CAP.add_Lamina(b90)
	CAP.add_Lamina(a0)
	CAP.add_Lamina(b90)
	CAP.add_Lamina(a0)
	CAP.add_Lamina(b90)
	CAP.add_Lamina(a0)
	CAP.add_Lamina(b90)
	CAP.add_Lamina(a0)
	CAP.add_Lamina(b90)
	CAP.add_Lamina(a0)
	CAP.add_Lamina(b90)
	CAP.add_Lamina(a0)
	CAP.add_Lamina(b90)
	CAP.add_Lamina(a0)
 	CAP.update()

 	print 'SKIN********-----',SKIN.THICK,SKIN.density,SKIN.Ex,SKIN.Ey,SKIN.Gxy
 	print 'CAP********-----',CAP.THICK,CAP.density,CAP.Ex,CAP.Ey,CAP.Gxy
 	print 'WEB********-----',WEB.THICK,WEB.density,WEB.Ex,WEB.Ey,WEB.Gxy

 	#define load
	Load = Loading(79,0,11,0,0,0)
	Load.apple_to(CAP)

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