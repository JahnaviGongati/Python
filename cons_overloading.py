class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #print(self.x+self.y)
    def __add__(self,other,other1):
        return point(self.x+other.x,other1.x,self.y+other.y,other1.y)
p1=point(1,2)
p2=point(3,4)
p3=point(1,5)
print(p1+p2+p3)
