import pandas as pd
import sympy as syp
import math
t = syp.symbols('t')
c = syp.symbols('c')
x = syp.symbols('x')
y = syp.symbols('y')
s = syp.symbols('s')
Qx= syp.symbols('Qx')
Qy= syp.symbols('Qy')


class Read_COS(object):
	"""docstring for Read_COS"""
	def __init__(self, path,unit = 1):
		super(Read_COS, self).__init__()
		self.path = path
		a = pd.read_excel(self.path)
		self.cos_value = []
		self.TK = []
		self.length = []
		self.unit = float(unit)
		for i in range(0,a.shape[0]):
			self.cos_value.append([a.iloc[i,0] / self.unit , a.iloc[i,1] / self.unit])
			self.TK.append(a.iloc[i,2]/ self.unit)

		self.A = self.get_area()
		# self.Sx = self.get_Sx().subs(t,1)
		# self.Sy = self.get_Sy().subs(t,1)


	def get_area(self):
		A = 0
		for i in range(0,len(self.cos_value)-1):
			yy = self.cos_value[i+1][1] - self.cos_value[i][1]
			xx = self.cos_value[i+1][0] - self.cos_value[i][0]
			leng = math.sqrt(yy**2+xx**2) 
			self.length.append(leng)
			A = A + leng * self.TK[i]
		return A



def draw_points(cos_value,linewidth = 1,color = 'b',linestyle = '--',axis = ''):
	import matplotlib.pyplot as plt
	import matplotlib

	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	
	x = [cos_value[i][0] for i in range(0,len(cos_value))]
	y = [cos_value[i][1] for i in range(0,len(cos_value))]

	max_x = int(max([(num) for num in x])) +1
	min_x = int(min([(num) for num in x])) -1

	max_y = int(max([(num) for num in y])) +1
	min_y = int(min([(num) for num in y])) -1
 	ax1.set_xlim(min_x,max_x)
	ax1.set_ylim(min_y,max_y)
	# print min_x-max_x,max_y - min_y

	for i in range(len(x)):
		plt.text(x[i],y[i],i, family='serif',style='italic', ha='right', wrap=True)

	ax1.plot(x,y,'o',color = 'red')
	ax1.plot(x,y,linewidth = linewidth,color = color ,linestyle = linestyle)
	
	if axis:
		ss = str(axis)
		plt.axis(ss)
	plt.grid()
	plt.show()

if __name__ == "__main__":

	val = Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/naca2412.xlsx')
	# print val.cos_value
	draw_points(val.cos_value,axis = 'equal')