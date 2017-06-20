#coding:utf-8
import sys
sys.path.insert(0, "../source")
import read_exe
from shear_stream import *
import profile
from graph import *
from graph_plugin import *
import open_profile
from open_profile import *
if __name__ == "__main__":	
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/[]2.xlsx')	
	lis = val.cos_value	
	print lis
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,0.001)

	for v in g:
		print v

	g.ChangeWeight(0,1,0.002)
	g.ChangeWeight(4,5,0.002)

	thk = graph_line_thickness(g,[0,1,2,3,4,5])
	print '--------------------------',thk
	# draw_point_graph(g,dirddd,color='b')


	Pc = Profile_Constant(thickness = thk,graph = g,dir = dirddd)

	print 'area',Pc.Area
	print 'Ix-->',Pc.Ix
	print 'Iy-->',Pc.Iy
	print 'Ixy-->',Pc.Ixy
	new_dir = Pc.profile_To_centriod()
	print 'area',Pc.Area
	print 'Ix-->',Pc.Ix
	print 'Iy-->',Pc.Iy
	print 'Ixy-->',Pc.Ixy
	print 'cen_x',Pc.centroid_x,Pc.centroid_y
	draw_point_graph(g,Pc.dir ,color='b')
	cccc = dict_To_cos(Pc.dir)


	val = Open_Profile(cccc,Pc,thickness=thk)
	print '__doc__-->',val.__doc__
	print 'cos_value-->',val.cos_value
	print 'length-->',val.length
	print 'Ix-->',val.Ix
	print 'Iy-->',val.Iy
	print 'Ixy-->',val.Ixy
	print 'Sx-->',val.Sx
	print 'Sy-->-->',val.Sy
	print 'Shear_ST-->',val.Shear_ST
	
	A = Surround_Area(val.cos_value,basic_point = [-1,0])

	Q0 = get_Shear_Qo(val.Shear_ST, val.cos_value,basic_point = [3,0])/ (2*A)
	print A,Q0
	print 'sssssccccc--->',\
	get_Shear_center_x(val,basic_point = [1,0]),get_Shear_center_y(val,basic_point = [1,0])
	if 0:

		if val.Shear_ST:
			import matplotlib.pyplot as plt
			import matplotlib

			Shear_ST = [x+Q0 for x in val.Shear_ST]
			for n in range(0,len(Shear_ST)):
				xl = np.linspace(0,val.length[n],100)
				yl = []
				for i in xl:
					yl.append(Shear_ST[n].subs(s,i))
				plt.plot(xl,yl)
			plt.grid()
			plt.show()

	