import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

FPGI = 0

if FPGI == 0:
	lf = np.transpose(np.loadtxt('Naveau/TestNaveau2015Online64LeftFoot.dat'))
	rf = np.transpose(np.loadtxt('Naveau/TestNaveau2015Online64RightFoot.dat'))
	com = np.transpose(np.loadtxt('Naveau/TestNaveau2015Online64CoM.dat'))
	waist = np.transpose(np.loadtxt('Naveau/TestNaveau2015Online64WaistOrientation.dat'))

	# lf2 = np.transpose(np.loadtxt('NaveauWithDF/TestNaveau2015Online64LeftFoot.dat'))
	# rf2 = np.transpose(np.loadtxt('NaveauWithDF/TestNaveau2015Online64RightFoot.dat'))
	# com2 = np.transpose(np.loadtxt('NaveauWithDF/TestNaveau2015Online64CoM.dat'))
	# waist = np.transpose(np.loadtxt('NaveauWithDF/TestNaveau2015Online64WaistOrientation.dat'))

	time = np.arange(0,len(lf[0]),1)*0.001
	timew = np.arange(0,len(waist[0]),1)*0.001
	lfX = lf[0]#data[15]
	rfX = rf[0]#data[29]
	comX = com[0]#data[1]

	lfY = lf[1] #data[16]
	rfY = rf[1]#data[30]
	comY = com[1]#data[2]

	lfZ = lf[2]#data[17]
	rfZ = rf[2]#data[31]
	comZ = com[2]#data[3]

	lfYaw = lf[3]#data[24]
	lfPitch = lf[4]#data[28]
	lfRoll = lf[5]#data[27]
	rfYaw = rf[3]#data[38]
	rfPitch = rf[4]#data[42]
	rfRoll = rf[5]#data[41]	

	wRoll = waist[0]
	wPitch = waist[1]
	wYaw = waist[2]		
else:
	data = np.transpose(np.loadtxt('NaveauWithDF/TestNaveau2015Online64TestFGPI.dat'))
	data2 = np.transpose(np.loadtxt('NaveauWithoutDF/TestNaveau2015Online64TestFGPI.dat'))

	lfX = data[15]
	rfX = data[29]
	zmpX = data[13]
	comX = data[1]
	zmpX2 = data[13]
	comX2 = data[1]

	lfY = data[16]
	rfY = data[30]
	zmpY = data[14]
	comY = data[2]
	zmpY2 = data[14]
	comY2 = data[2]

	lfZ = data[17]
	rfZ = data[31]
	comZ = data[3]

	lfYaw = data[24]
	lfPitch = data[28]
	lfRoll = data[27]
	rfYaw = data[38]
	rfPitch = data[42]
	rfRoll = data[41]

	time = data[0]

# plt.subplot(221) 
# plt.plot(t,zmp[0],'r',label='zmp X')
# plt.plot(t,zmp[1],'r--',label='zmp Y')
# plt.plot(t,com[0],'b',label='com X')
# plt.plot(t,com[1],'b--',label='com Y')
# legend = plt.legend(loc='upper left')
# plt.title("Fichier Kajita généré avant")

plt.subplot(121) 
# plt.plot(time,zmpX,'r',label='zmp X')
# plt.plot(time,zmpY,'r--',label='zmp Y')
plt.plot(time,comX,'b',label='com X')
plt.plot(time,comY,'b--',label='com Y')
legend = plt.legend(loc='upper left')
plt.title("Zmp et Com")
#plt.show()

# plt.subplot(122) 
# plt.plot(time,zmpX2,'r',label='zmp X')
# plt.plot(time,zmpY2,'r--',label='zmp Y')
# plt.plot(time,comX2,'b',label='com X')
# plt.plot(time,comY2,'b--',label='com Y')
# legend = plt.legend(loc='upper left')
# plt.title("Zmp et Com without DF")

# plt.subplot(222) 
# plt.plot(t,lf[0],'r',label='Left foot X')
# plt.plot(t,lf[1],'r--',label='Left foot Y')
# plt.plot(t,rf[0],'b',label='Right foot X')
# plt.plot(t,rf[1],'b--',label='Right foot  Y')
# legend = plt.legend(loc='upper left')
# plt.title("Fichier Kajita généré avant")

# plt.subplot(313) 
# plt.plot(time,lfX,'r',label='Left foot X')
# plt.plot(time,lfY,'r--',label='Left foot Y')
# plt.plot(time,rfX,'b',label='Right foot X')
# plt.plot(time,rfY,'b--',label='Right foot  Y')
# legend = plt.legend(loc='upper left')
# plt.title("Pieds")


#plt.show()
# plt.subplot(313) 
# plt.plot(t,lf[0],'r',label='Left foot X')
# plt.plot(t,lf[1],'r--',label='Left foot Y')
# plt.plot(t,rf[0],'b',label='Right foot X')
# plt.plot(t,rf[1],'b--',label='Right foot  Y')
# legend = plt.legend(loc='upper left')
# plt.title("Pieds")
plt.show()

plt.subplot(131)
plt.plot(time,lfYaw,'r',label='Left foot Yaw')
plt.plot(time,rfYaw,'b',label='Right foot Yaw')
legend = plt.legend(loc='upper left')
# plt.subplot(324)
# plt.plot(t,lf[3],'r--',label='Left foot Yaw')
# plt.plot(t,rf[3],'b--',label='Right foot Yaw')
legend = plt.legend(loc='upper left')

plt.subplot(132)
plt.plot(time,lfPitch,'r',label='Left foot Pitch')
plt.plot(time,rfPitch,'b',label='Right foot Pitch')
legend = plt.legend(loc='upper left')
# plt.subplot(325)
# plt.plot(t,lf[4],'r--',label='Left foot Pitch')
# plt.plot(t,rf[4],'b--',label='Right foot Pitch')
legend = plt.legend(loc='upper left')

plt.subplot(133)
plt.plot(time,lfRoll,'r',label='Left foot Roll')
plt.plot(time,rfRoll,'b',label='Right foot Roll')
legend = plt.legend(loc='upper left')
# plt.subplot(326)
# plt.plot(t,lf[5],'r--',label='Left foot Roll')
# plt.plot(t,rf[5],'b--',label='Right foot Roll')
legend = plt.legend(loc='upper left')

plt.show()

#print(len(data[0]),len(zmp[0]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(lfX, lfY, lfZ, 'r',label='Left foot')
ax.plot3D(rfX, rfY, rfZ, 'b',label='Right foot')
ax.plot3D(comX, comY, comZ, 'g',label='CoM')
legend = plt.legend(loc='upper left')

plt.show()

plt.subplot(131)
plt.plot(timew,wRoll,'r',label='Waist Roll')
legend = plt.legend(loc='upper left')


plt.subplot(132)
plt.plot(timew,wPitch,'r',label='Waist Pitch')
legend = plt.legend(loc='upper left')

plt.subplot(133)
plt.plot(timew,wYaw,'r',label='Waist Yaw')
legend = plt.legend(loc='upper left')

plt.show()