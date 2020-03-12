from pylab import show, plot, xlim, ylim, xlabel, ylabel
from numpy import linspace, sin, cos
x=linspace(0,10,100)
print(x)
y=sin(x)
plot(x,y,"ko")
xlabel("Radians")
show()
a=open("datos.dat","w")
for i in range(len(x)):
	a.write("%.2f %.2f\n" % (x[i],y[i]))
a.close()
from numpy import loadtxt
b=loadtxt("datos.dat",float)
print(b[:,0])
print(b[:,1])
plot(b[:,0],b[:,1],"g--")
ylim(-0.5,0.5)
show()
z=sin(x)
w=cos(x)
plot(x,z,"k--")
plot(x,w,"g--")
show()
