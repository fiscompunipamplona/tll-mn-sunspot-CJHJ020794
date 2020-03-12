from pylab import xlabel, ylabel, xlim, ylim, plot, show
from numpy import loadtxt
datos=loadtxt("sunspots.dat",float)
plot(datos[:,0],datos[:,1],"r-")
y=[]
x=[]
for k in range(5,1000):
	ykm=0
	for m in range(k-5,k+5):
		d=datos[m,1]
		ykm=ykm+d
	y.append(ykm/11)
	x.append(k)
plot(x,y,"k-")
xlim(0,1000)
xlabel("Meses")
ylabel("Numero de Manchas")
show()
