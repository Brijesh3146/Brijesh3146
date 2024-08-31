class calc:
    def __init__(self,a,b):
      self.no1=a
      self.no2=b
    def add(self):
        print("sum=",self.no1+self.no2)
    def sub(self):
        print("sub=",self.no1-self.no2)
    def mul(self):
        print("mul=",self.no1*self.no2)   
    def div(self):
        print("div=",self.no1/self.no2)  
x=int(input("enter no.1\n"))
y=int(input("enter no.2\n"))  
c1=calc(x,y)
a=int(input('''enter (1 for addition,2 for subtraction,3 for multiplication, 4 for divition)\n'''))
if a==1:
    c1.add()
elif a==2:
    c1.sub()
elif a==3:
    c1.mul()
elif a==4:
    c1.div()
else:
    print("no option ")
