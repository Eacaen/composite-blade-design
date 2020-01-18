from graph import *
import matplotlib.pyplot as plt
import matplotlib

import sys
sys.path.append('/home/eacaen/TUBS_graduation/draft/source')
import read_exe
# from shear_stream import *
from profile import *

#################################################################################
#Function info:
# connect points in the direction
# The relationship of the points based on the edges in the graph
#
#
#################################################################################

def draw_point_graph(graph , dir,linewidth = 1,color = 'black',linestyle = '-'\
					,axis = '',Show_Number = True,Shear_Center=[],Shear_Center_List = [],title=''):
	import matplotlib.pyplot as plt
	import matplotlib

	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	
	x = [dir[i][0] for i in range(0,len(dir))]
	y = [dir[i][1] for i in range(0,len(dir))]

	max_x = int(max([(num) for num in x])) +1
	min_x = int(min([(num) for num in x])) -1

	max_y = int(max([(num) for num in y])) +1
	min_y = int(min([(num) for num in y])) -1
	ax1.set_xlim(min_x,max_x)
	ax1.set_ylim(min_y,max_y)

	ax1.plot(x,y,'o',color = 'red')
	for v in graph:
		for e in v.getConnections():
			ax1.plot([x[v.id],x[e.id]] , [y[v.id],y[e.id] ],\
				linewidth = linewidth * v.getWeight(e) ,color = color,linestyle = linestyle)

	if Show_Number:

		for i in range(len(x)):
			a = round(x[i],2)
			b = round(y[i],2)
			plt.text(a,b,i, family='serif',style='italic', ha='right', wrap=True)

	if axis:
		ss = str(axis)
		plt.axis(ss)
	
	if Shear_Center != []:

		xs = round(Shear_Center[0],2)
		ys = round(Shear_Center[1],2)
		ax1.plot([xs],[ys],'r*',label='Shear Center')
		ax1.text(xs,ys ,'Shear Center', family='serif',style='italic', ha='right', wrap=True,\
										color='blue',fontsize=8)


	if Shear_Center_List != []:
		xs = []
		ys = []
		for i in range(len(Shear_Center_List)):
			xs.append(round(Shear_Center_List[i][0],2))
			ys.append(round(Shear_Center_List[i][1],2))
		
		ax1.plot(xs,ys,'r*',label='Shear Center')
		plt.legend()

	if title:
		TiT = str(title)
		plt.title(TiT)
	plt.grid()
	plt.show()

def cos_To_dict(cos_value = []):
	direction ={}
	for i in range(len(cos_value)):
		direction[i] = cos_value[i]

	return direction

def dict_To_cos(direction = {}):
	cos_value = []
	for i in range(len(direction)):
		cos_value.append(direction[i])

	return cos_value

def graph_line_thickness(graph,points = []):
	"""collect the thickness of edge's thickness(weight) """
	thickness = []
	if points:
		for i in range(len(points)-1):
			p1 = points[i]
			p2 = points[i+1]
			thick_ij = graph.vertList[ p1 ].getWeight(graph.vertList[ p2 ])
			thickness.append(thick_ij)
		return thickness

def line_value_package(cos_value = []):
	line = []
	for i in range(len(cos_value)-1):
		a = [cos_value[i],cos_value[i+1]]
		line.append(a)

	return line

def graph_line_length(graph,dir,points = []):
	"""collect the thickness of edge's thickness(weight) """
	length = []
	if points:
		for i in range(len(points)-1):
			p1 = dir [ points[i] ]
			p2 = dir [ points[i+1] ]

			le = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

			length.append(le)
		return length

if __name__ == "__main__":	

	lis = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 4], [5, 3], [5, 2], [4, 1], [3, 1], [2, 1]]

	dirddd =cos_To_dict(lis)
	print(dirddd)
	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,i+1)


	# draw_point_graph(g,dirddd,color='b')

	# g.addEdge(0,9,1)
	# # g.addEdge(1,4,1)
	# # g.remove_Edge(2,3)
	# draw_point_graph(g,dirddd,color='b')

	lll = dict_To_cos(dirddd)
	print(lll)
	print(graph_line_thickness)(g,[0,1,2,3,4,5,6,7,8,9])
	print(graph_line_length)(g,dirddd,[0,1,2,3,4,5,6,7,8,9])
	print(line_value_package)([1,2,3,4,5])