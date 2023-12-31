import numpy as np
import matplotlib.pyplot as plt

# A=np.linspace(0,np.pi,10)
# B=np.empty(10)
# np.sin(A,out=B)
# print(B)

################################
# A=np.linspace(0,np.pi,10)
# B=np.sin(A)
# print(B)
#
# print(np.info(np.linspace))
# print(np.info(np.sin))

################################
# A=np.arange(6)
# print(A)
# print(np.power(A,2))
# print(A**2)
# print(np.power(A,A))
# print(A**A)

################################
# A=np.linspace(0,np.pi,10)
# B=np.sin(A,dtype='float16')
# print(' '.join(format(x,'05,.3f') for x in B))

################################
# A=np.linspace(0,2*np.pi) #default 50
# # print(A)
# # plt.plot(A,np.sin(A))
# plt.plot(A,np.cos(A))
# plt.show()

################################
# A=np.linspace(0.1,10)
# plt.plot(A,1/A)
# plt.show()

################################
# plt.plot([0,1,2,3,4],[1,2,4,5,3])
# plt.plot([1,2,4,5,3])
# plt.show()

################################
# plt.plot([3,4,1,5,2,3],[4,1,3,3,1,4])
# plt.show() #star

################################
# A=np.linspace(-15,20)
# plt.plot(A,A**3-(15*A**2)+25)
# plt.show()

################################
# A=np.linspace(0,2*np.pi)
# plt.plot(A,np.sin(A))
# plt.plot(A,np.cos(A))
# plt.show()

        #or
# A=np.linspace(0,2*np.pi)
# plt.plot(A,np.sin(A),A,np.cos(A))
# plt.show()

################################
# A=np.linspace(0,2*np.pi)
# plt.plot(A,np.sin(A),A,np.cos(A),'o')
# plt.show()

#################################
# A=np.linspace(0,2*np.pi)
# plt.plot(A,np.sin(A),'^',A,np.cos(A),'o')
# plt.title('Sine and Cosine')
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.show()

################################
# A=np.linspace(0,60,60)
# plt.plot(A,2*A,'o',A,1.1**A)
# plt.title('Compounded Interest v. Linear')
# plt.xlabel('Years')
# plt.ylabel('Value of Funds')
# plt.show()

################################
# IQ_list = [91, 110, 105, 107, 135, 127, 92, 111,
#            105, 106, 130, 145, 145, 128, 109, 108, 98, 129,
#            100, 108, 114, 119, 99, 137, 142, 145, 112, 113 ]
#
# IQ_A=np.array(IQ_list)
# # plt.hist(IQ_A)
# plt.hist(IQ_A,bins=20)
# plt.title('IQ Distribution of the development team.')
# plt.show()

################################
# A = np.random.standard_normal(200000)
# A=A*10+100
# # print(A)
# # print(help(np.random.standard_normal))
# plt.hist(A,bins=80,color='g')
# plt.title('Normal distribution in 80 bins')
# plt.show()

################################
# A=np.random.standard_normal(2000000)
# A=A*10+100
# B=np.histogram(A,50)[0]
# plt.plot(B)
# plt.show()

################################
# theta=np.linspace(0,2*np.pi,1000)
# plt.plot(np.cos(theta),np.sin(theta))
# plt.axis('equal')
# plt.show()

################################
# A_data = [3.7, 2.5, 1.9, 0.5]
# A_labels = ['Poker', 'Chess', 'Comic Books', 'Exercise']
# A_colors = ['k', 'g', 'r', 'c']
# plt.pie(A_data,labels=A_labels,colors=A_colors)
# plt.title('Relative Hobbies of Dev. Team')
# plt.axis('equal')
# plt.show()

################################
# A=np.ones(5)
# B=np.arange(5)
# print(np.dot(A,B))
# print(np.dot(A,A))
# print(np.dot(B,B))

################################
# A=np.arange(6).reshape(2,3)
# B=np.arange(6).reshape(3,2)
# C=np.dot(A,B)
# print(A,B,sep='\n\n')
# print(C)

################################
# B=[[0,1],[2,3],[4,5]]
# B=np.array(B)
# print(np.dot([10,15,30],B))

################################
# A=np.array([0,1,2])
# B=np.array([100,200,300,400])
# print(np.outer(A,B))

################################
# A=np.arange(1,11)
# s=str(np.outer(A,A)).replace('[','').replace(']','')
# print(' '+s)

################################
from mpl_toolkits.mplot3d import Axes3D

# fig=plt.figure()
# ax=fig.add_subplot(111,projection='3d')
#
# ua=np.linspace(0,2*np.pi,100)
# va=np.linspace(0,np.pi,100)
#
# x=10*np.outer(np.cos(ua),np.sin(va))
# y=10*np.outer(np.sin(ua),np.sin(va))
# z=10*np.outer(np.ones(np.size(ua)),np.cos(va))
# ax.plot_surface(x,y,z,color='w')
# plt.show()

################################
# rate=0.05/12
# nper=30*12
# pv=155000
# total=-1*np.pm(rate,nper,pv)
#
# A=np.linspace(0,nper)
# B=-1*np.ppmt(rate,A,nper,pv)/total #depricated
# print(A,B,sep='\n')
# plt.plot(A,B)
# plt.xlabel('Months')
# plt.ylabel('Percentage Applied to Principal')
# plt.show()

################################
# Words = np.array(('To', 'be', 'orNotToBe'))
# print(Words)
# Words[0]='My uncle is caesar.'
# print(Words)

# Words = np.array(('To', 'be', 'orNotToBe'),dtype='U20')
# print(Words)
# Words[0]='My uncle is caesar.'
# print(Words)

################################
# X=np.array([(12,33,'red'),(0,1,'blue'),(27,103,'yellow'),(-1,-2,'blue')],dtype=[('a','i4'),('b','i4'),('color','U10')])
# print(X)
# print(X['a'])
# print(X['b'])
# print(X['color'])
# X['a']=0 #numpy works on array
# print(X)

################################
dt=[('IQ','i2'),('Height','f4'),('Age','i2'),('Rating','f4'),('College','U30')]
team_a=np.loadtxt(fname='./team_data.csv',dtype=dt,delimiter=',')
print(team_a)
# print(team_a['IQ'])
new_a=np.array((100,70,18,5.5,'C.C.C.'),dtype=dt)
team_a=np.append(team_a,new_a)
print(team_a)
np.savetxt('./team_dataa.csv',team_a,fmt='%i, %.1f, %i, %.1f, %s')
################################
################################
################################
################################
################################
################################
################################