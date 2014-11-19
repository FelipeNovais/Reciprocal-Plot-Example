######################RECIPROCAL FUNCTION EXAMPLE###################
#			-Created by Felipe Novais & Estela Mello-
#		-Dedicated to Renato Cantao great guy and teacher-
#
####################################################################

#IMPORTS
import matplotlib.pyplot as plt
from numpy import arange, inf

#VARIABLES
x = arange(-10.0, 10.0, 0.0001)
y = 1.0/x
y[y>100] = inf
y[y<-100] = -inf
##PLOTING
plt.plot(x, y)

#SHOWING
plt.axes().set_aspect('equal','box')
plt.axes().set_ylim([-10,10])
plt.grid()
plt.show()
