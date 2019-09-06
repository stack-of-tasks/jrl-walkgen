import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#FPGI = np.transpose(np.loadtxt('Kajita/TestKajita2003StraightWalking64TestFGPI.dat'))
FPGI = np.transpose(np.loadtxt('Naveau10cm/TestNaveau2015Online64TestFGPIFull.dat'))

print(len(FPGI))
# print(len(np.transpose(np.loadtxt('TestNaveau2015Online64TestFGPI.dat'))))
# print(len(FPGI))
# print(len(np.transpose(np.loadtxt('test.dat'))))

for k in range (1,39):
	print("q",FPGI[44+k][0],44+k)
#	print("dq",FPGI[85+k][0],85+k)	
#	print("ddq",FPGI[123+k][0],123+k)
#	print("ddq",FPGI[161+k][100])

lfX_FPGI = FPGI[15]
rfX_FPGI = FPGI[29]
zmpX_FPGI = FPGI[13]
comX_FPGI = FPGI[1]
dcomX_FPGI = FPGI[5]
ddcomX_FPGI = FPGI[9]
zmpmbX_FPGI = FPGI[83]

#print (zmpmbX_FPGI)

lfY_FPGI = FPGI[16]
rfY_FPGI = FPGI[30]
zmpY_FPGI = FPGI[14]
comY_FPGI = FPGI[2]
dcomY_FPGI = FPGI[6]
ddcomY_FPGI = FPGI[10]
zmpmbY_FPGI = FPGI[84]

lfZ_FPGI = FPGI[17]
rfZ_FPGI = FPGI[31]
comZ_FPGI = FPGI[3]
dcomZ_FPGI = FPGI[7]
ddcomZ_FPGI = FPGI[11]

time_FPGI = FPGI[0]
print(len(time_FPGI))

#plt.subplot(121) 
plt.plot(time_FPGI,zmpX_FPGI,'r',label='zmp X')
plt.plot(time_FPGI,zmpY_FPGI,'r--',label='zmp Y')
plt.plot(time_FPGI,zmpmbX_FPGI,'g',label='zmpmb X')
plt.plot(time_FPGI,zmpmbY_FPGI,'g--',label='zmpmb Y')
legend = plt.legend(loc='upper left')

plt.show()

plt.subplot(131) 
plt.plot(time_FPGI,comX_FPGI,'r',label='com X')
plt.plot(time_FPGI,comY_FPGI,'b',label='com Y')
plt.plot(time_FPGI,comZ_FPGI,'g',label='com Z')
legend = plt.legend(loc='upper left')
plt.subplot(132)
plt.plot(time_FPGI,dcomX_FPGI,'r',label='dcom X')
plt.plot(time_FPGI,dcomY_FPGI,'b',label='dcom Y')
plt.plot(time_FPGI,dcomZ_FPGI,'g',label='dcom Z')
legend = plt.legend(loc='upper left')
plt.subplot(133)
plt.plot(time_FPGI,ddcomX_FPGI,'r',label='ddcom X')
plt.plot(time_FPGI,ddcomY_FPGI,'b',label='ddcom Y')
plt.plot(time_FPGI,ddcomZ_FPGI,'g',label='ddcom Z')
legend = plt.legend(loc='upper left')

plt.show()
#plt.subplot(122) 
plt.plot(time_FPGI,lfX_FPGI,'r',label='Left foot X')
plt.plot(time_FPGI,lfY_FPGI,'r--',label='Left foot Y')
plt.plot(time_FPGI,rfX_FPGI,'b',label='Right foot X')
plt.plot(time_FPGI,rfY_FPGI,'b--',label='Right foot  Y')
legend = plt.legend(loc='upper left')

plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(lfX_FPGI, lfY_FPGI, lfZ_FPGI, 'r',label='Left foot')
ax.plot3D(rfX_FPGI, rfY_FPGI, rfZ_FPGI, 'b',label='Right foot')
ax.plot3D(comX_FPGI, comY_FPGI, comZ_FPGI, 'g',label='CoM')
legend = plt.legend(loc='upper left')

plt.show()
