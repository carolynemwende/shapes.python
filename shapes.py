class circle:

	def __init__(self,radius):
		self.radius= 6

	def area1(self):
		area= 22/7*(self.radius)**2
		return area
	   
	def calcCircumfrence(self):
		circumfrence= 2*22/7*(self.radius)
		return circumfrence


class square:
	def __init__(self,side):
		self.side= 5

	def area2(self):
		area= (self.side)**2
		return area
	def calcPerimeter(self):
		perimeter=4*self.side
		return perimeter

class rectangle:

	def __init__(self,w,l):
		self.w= w
		self.l=l

	def area3(self):
		area= self.w*self.l
		return area

	def perimeter(self):
		perimeter= 2*(self.w+ self.l)
		return perimeter

class sphere:

	def __init__(self,sphereradius):
		sef.sphereradius= 6

	def surfaceArea(self,surfaceArea):
		surfaceArea= 4*(22/7)*(self.sphereradius)**2
		return surfaceArea

	def volume(self):
		volume= 4/3 * (22/7)*(self.sphereradius*sphereradius*sphereradius)
		return volume