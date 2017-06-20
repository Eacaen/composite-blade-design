#coding:utf-8
import sys
sys.path.insert(0, "../source")
import read_exe
import profile
import open_profile
from graph import *
from graph_plugin import *
from profile_plugin import *

if __name__ == "__main__":	
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/Z.xlsx')
	lis = val.cos_value	
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,0.1)
 

	# draw_point_graph(g,dirddd,color='b')
	ccc = [0,1,2,3]
	cccc = [lis[i] for i in ccc]
	thk = graph_line_thickness(g,ccc)

	Pc = Profile_Constant(graph = g,dir = dirddd,thickness = thk)
	
	lis = Pc.profile_To_centriod()


	ccc = [0,1,2,3]
	cccc = [lis[i] for i in ccc]
	thk = graph_line_thickness(g,ccc)
	print 'ccccc--',cccc
	
	pp = [-0.5,0.5]
  
	cc = open_profile.Open_Profile(cccc,Pc,Qx = 0,Qy = 1,thickness = thk)
	xx = open_profile.get_Shear_center_x(cc ,basic_point = pp)
	# print cc.Shear_ST
	print 'xxxxxx--->\n',xx,xx-pp[0],xx+ pp[0]


	cc = open_profile.Open_Profile(cccc,Pc ,Qx = 1,Qy = 0,thickness = thk)
	yy = open_profile.get_Shear_center_y(cc ,basic_point = pp)
	# print cc.thickness
	print 'yyyyyyy--->\n',yy,yy-pp[1],yy+ pp[1] 

  	print '\n',open_profile.get_resultant_Q(cccc,Shear_ST = cc.Shear_ST,thickness = thk)

	print '\n\n'
	cc.report()
	