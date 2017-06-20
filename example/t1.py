
import sys
sys.path.append('/home/eacaen/TUBS_graduation/draft/source')
sys.path.insert(0, "../source")
import read_exe
from shear_stream import *
from graph import *
import matplotlib.pyplot as plt
import matplotlib

# lis = [[-1,-1],[0,-1],[0,1],[-1,1]]
# lis = [[0,-1],[0,1],[1,1],[-1,1]]
lis = [[-1,-1],[0,-1],[1,-1],[-1,1],[0,1],[1,1]]
# lis = [[-1.08578643762691, -1.00000000000000], [-0.0857864376269051, -1.00000000000000], [0.914213562373095, 0], [-0.0857864376269051, 1.00000000000000], [-1.08578643762691, 1.00000000000000]]
dir ={}
for i in range(len(lis)):
	dir[i] = lis[i]


g = Graph()
for i in range(len(dir)):
	g.addVertex(i)
for i in range(len(dir)-1):
	g.addEdge(i,i+1)



#################################################################################
#Function info:
# connect points in the direction
# The relationship of the points based on the edges in the graph
#
#
#################################################################################

def draw_point_graph(graph,dir,linewidth = 1,color = 'black',linestyle = '-'):
	import matplotlib.pyplot as plt
	import matplotlib

	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	
	x = [dir[i][0] for i in range(0,len(dir))]
	y = [dir[i][1] for i in range(0,len(dir))]

	mx = int(max([abs(num) for num in x])+1)
	my = int(max([abs(num) for num in y])+1)	
	ax1.set_ylim(-1.0*mx-1,mx + 1)
	ax1.set_xlim(-1.0*my-1,my + 1)

	for i in range(len(x)):
		plt.text(x[i],y[i],i, family='serif',style='italic', ha='right', wrap=True)

	ax1.plot(x,y,'o',color = 'red')
	for v in graph:
		for e in v.getConnections():
			ax1.plot([x[v.id],x[e.id]] , [y[v.id],y[e.id] ],\
				linewidth = linewidth ,color = color,linestyle = linestyle)  

	plt.grid()
	plt.show()




def find_head(graph):
	open_line =[]
	for v in graph:
		if v not in open_line:
			open_line.append(v)

		for e in v.getConnections():
			if e in open_line:
				pass

			elif e not in open_line:
				open_line.append(e)

	each_vertex_connecto = [len(v.edge) for v in graph]
	# print [x.id for x in open_line]
	return [x.id for x in open_line]

g.addEdge(1,4)
g.remove_Edge(2,3)
# for v in g:
# 	print dir[v.id],v
i =0
for v in g:
	for e in v.getConnections():
		i = i +1
		cos_value =[dir[v.id],dir[e.id] ]
		print i,cos_value
# draw_point_graph(g, dir,color='b')

# read_exe.draw_points(lis)


open_order = find_head(g)
new_value = [dir[num] for num in open_order]
print 'value_using---------',new_value



# val = Open_Profile(new_value)
# print val.Ix
# print val.Iy
# print val.Ixy
# print val.Sx
# print val.Sy
# print val.Shear_ST
if 0:
	if val.Shear_ST:
			import matplotlib.pyplot as plt
			import matplotlib

			for n in range(0,len(val.length)):
				xl = np.linspace(0,val.length[n],100)
				yl = []
				for i in xl:
					yl.append(val.Shear_ST[n].subs(s,i))
				plt.plot(xl,yl)
			plt.grid()
			plt.show()			



