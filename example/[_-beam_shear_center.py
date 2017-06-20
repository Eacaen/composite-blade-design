#coding:utf-8
#############################################################################
# move C-beam to its Centroid
# get its engineer constant value
# plot it out find its shear center
#############################################################################
 
import sys
sys.path.insert(0, "../source")
import read_exe
import profile
import open_profile
from graph import *
from graph_plugin import *
from profile_plugin import *
if __name__ == "__main__":	

 	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/[_.xlsx')
	lis = val.cos_value	
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)
 

	# draw_point_graph(g,dirddd,color='b')

	val = Profile_Constant(graph = g,dir = dirddd)
	
	lis = val.profile_To_centriod()

	
	thk = graph_line_thickness(g,[0,1,2,3])
	
	pp = [-0.5,-0.5]
  
	cc = open_profile.Open_Profile(lis,val,thickness = thk,Qx = 0,Qy = 1)
	xx = open_profile.get_Shear_center_x(cc,Shear_ST = cc.Shear_ST,basic_point = pp)
	print cc.Shear_ST
	print 'xxxxxx--->\n',xx,xx-pp[0],xx+ pp[0]


	cc = open_profile.Open_Profile(lis,val ,thickness = thk,Qx = 1,Qy = 0)
	yy = -1.0*open_profile.get_Shear_center_y(cc,Shear_ST = cc.Shear_ST,basic_point = pp)
	print cc.Shear_ST
	print 'yyyyyyy--->\n',yy,yy-pp[1],yy+ pp[1] 

	cc.report()