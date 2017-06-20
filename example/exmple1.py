import sys
sys.path.insert(0, "../source")
from laminate_Tools import *
import matplotlib.pyplot as plt
import matplotlib

if __name__ == "__main__":
	max_load_list = []
	load_strain = []
	a = Lamina(5.4e4,1.8e4,8.8e3,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
											Yt = 28,Yc = 140, S = 42,\
											angle = 0,thickness=1)

	b = Lamina(5.4e4,1.8e4,8.8e3,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
											Yt = 28,Yc = 140, S = 42,\
											angle = 90,thickness=10)

	
	# print b.matrix_Q,'\n\n'
	# print b_reduced.matrix_Q_bar
	LA = Laminate()
	LA.add_Lamina(a)
	LA.add_Lamina(b)
	LA.add_Lamina(a)
	LA.update()


	Load = Loading(1,0,0)
	Load.apple_to(LA)


	print Report_strain(Load,layer_num = 1,mode = '12')
	ssr = Report_strain(Load,layer_num = 1,mode = '12')

	criterian = Failture_Criterion()
	criterian.Tsai_Hill(Load,layer_num = 1)
	ret =  criterian.ret_list[0]
	import math
	max_load = math.sqrt(1/(float(ret)))
	print max_load
	max_load_list.append(max_load)
	load_strain.append(ssr.iloc[0,0])
	
	b_reduced = Lamina(E1 = 5.4e4,E2 = 0.001,G12 = 0.0001,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
											Yt = 28,Yc = 140, S = 42,\
											angle = 90,thickness=10)
	LA.repalce_Lamina(1,b_reduced)
	LA.update()
	Load.apple_to(LA)
	print Report_strain(Load,layer_num = 1,mode = '12')
	ssr =  Report_strain(Load,layer_num = 1,mode = '12')

	criterian = Failture_Criterion()
	criterian.Tsai_Hill(Load)
	ret =  max(criterian.ret_list)
	import math
	max_load = math.sqrt(1/(float(ret)))
	print max_load
	max_load_list.append(max_load)
	load_strain.append(ssr.iloc[0,0])


	a_reduced = Lamina(E1 = 5.4e4,E2 = 0.001,G12 =0.001,v21 = 0.25,Xt = 1.05e3,Xc = 1.05e3,\
											Yt = 28,Yc = 140, S = 42,\
											angle = 0,thickness=1)

	# print a_reduced.matrix_Q,'\n\n',b_reduced.matrix_Q
	LA.repalce_Lamina(0,a_reduced)
	LA.repalce_Lamina(2,a_reduced)
	LA.update()
	Load.apple_to(LA)
	print Report_strain(Load,layer_num = 1,mode = '12')
	ssr  = Report_strain(Load,layer_num = 1,mode = '12')

	criterian.Tsai_Hill(Load)
	ret =  max(criterian.ret_list)
	import math
	max_load = math.sqrt(1/(float(ret)))
	print max_load
	max_load_list.append(max_load)
	load_strain.append(ssr.iloc[0,0])

	# load_strain[0] = load_strain[0]
	# load_strain[1] = load_strain[0] + load_strain[1]
	# load_strain[2] = load_strain[0] + load_strain[1] + load_strain[2]

	# max_load_list[0] = max_load_list[0]
	# max_load_list[1] = max_load_list[0] + max_load_list[1]
	# max_load_list[2] = max_load_list[0] + max_load_list[1] + max_load_list[2] 

	# load_strain = [-1*i for i in load_strain]
	# print max_load_list,load_strain
	
	# plt.plot(load_strain,max_load_list)
	# plt.show()