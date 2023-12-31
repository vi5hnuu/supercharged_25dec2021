import array
import numpy as np
import numpy.random as ran
from time import time

# a=array.array('h',[1,2,3])
# aa=array.array('h',range(1000))
# print(a)
# print(aa)

##########################################
# a_list=list(range(1,1_000_001))
# print(sum(a_list))
#
# a=np.arange(1,1_000_001,dtype=float)
# print(np.sum(a))

##########################################
# def benchmark(n):
#     t1=time()
#     a_list=list(range(1,n+1))
#     tot=sum(a_list)
#     t2=time()
#     print('Time taken by python is ',t2-t1)
#
#     t1=time()
#     a=np.arange(1,n+1)
#     tot=np.sum(a)
#     t2=time()
#     print('Time taken by python is ',t2-t1)
#
# benchmark(10_000_000)

##########################################
# # temp=np.linspace(1,20,100)
# temp=np.empty((2,3),dtype=int)
# temp=np.empty(shape=3,dtype=np.int16)
# temp=np.eye(3,dtype=np.int16)
# temp=np.eye(n=3,m=2,dtype=np.int16)
# temp=np.eye(N=3,M=2,k=-2,dtype=np.int16)
# temp=np.ones((2,3),dtype=int)
# temp=np.ones(shape=3,dtype=int)
# temp=np.ones(shape=(3,2,3),dtype=int)
# temp=np.ones(shape=(3,2,3),dtype=bool)
# # temp=np.zeros((2,3),dtype=int)
# temp=np.full((2,3),fill_value=5,dtype=int)
# temp=np.full(shape=3,fill_value=5,dtype=int)
# temp=np.full(shape=(3,2,5),fill_value='vishnu')
# temp[0][0][0]='vishuzzzzzzzzzzzzzzzzz'

# temp=np.full(shape=(3,2),fill_value=5,dtype=int)
# # temp1=temp.copy()
# temp1=temp
# temp1[0][0]=100 #Behaves like c++ array
# # temp=np.full((2,3),fill_value='vishnu',dtype='U6')
# print(temp)
# print(id(temp))
# # print(temp.__repr__())
# print(temp1)
# print(id(temp1))

##########################################
# a=np.array([1,2,3])
# print(a)

# a=np.array([[1,2,3],[10,20,30],[0,0,-1]])
# # a=np.array([[1,2,3],[10,20,30,40]],dtype=int) #error
# print(a)

##########################################
# a=np.arange(1,1000001,2,dtype=int)
# print(a)

##########################################
# # a=np.linspace(0,1.0,num=5)
# a=np.linspace(0,1.0,num=5,endpoint=False)
# # a=np.linspace(0,1.0,num=5,dtype=int) #apply truncate on result
# print(a)

##########################################
# a=np.fromfunction(lambda x:x**2,shape=(5,),dtype=int)
# a=np.fromfunction(lambda x,y:x+y,shape=(5,3))
# print(a)

# a = np.fromfunction(lambda r, c: 1, (3, 3),dtype='int')
# a = np.fromfunction(lambda r, c: (r+1)*1//(r+1), (3, 3),dtype='int')
# print(a)

##########################################
# def multiply(r,c):
#     return (r+1)*(c+1)
#
# a=np.fromfunction(multiply,(10,10),dtype=int)
# # print(a)
# print(' '+str(a).replace('[','').replace(']','')+' ') #space for loss

##########################################
# A=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
# print(A)
#
# B=np.arange(16).reshape(4,4)
# print(B)
#
# c=np.fromfunction(lambda x,y:x*4+y,shape=(4,4),dtype=np.int16)
# print(c)

##########################################
# A=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
# print(A)
#
# B=np.eye(4,dtype='int16')
# # C=A*10
# # C=A*A
# C=A**2
# D=A*B
# print(D)

##########################################
# A=np.arange(1,11)
# print(A)
# print(A[2:5])
# # A[0:0]=[15]
# A[2:5]=12
# A[1:3]=[11,21] #remember np arrays are fixed size so np big array initilize
# print(A)

lst=[1,2,3]
# lst[0:0]=[15]
# lst[0:2]*=2 #
# # lst[1:2]=[11,22,33] #ok
# print(lst)

# lstt=lst[0:1]
# print(lst)
# print(lstt)
# lstt[0]=15
# print(lst)
# print(lstt)


# A=np.arange(1,11)
# # print(A)
# # A[0:5]*=10
# A[0:5]=10
# z=A[0:5]
# z=12
# print(A)

##########################################
# A = np.arange(51)
# # print(A)
# A[1]=0
# A[2*2::2]=0
# A[3*3::3]=0
# A[5*5::5]=0
# A[7*7::7]=0
# # my_prime=[i for i in A if i>0]
# # print(my_prime)
# prime_mask=A>0
# prime_num=A[prime_mask]
# print(prime_num)
# # print(prime)
# print(A)

##########################################
# a=np.arange(1,17).reshape((4,4))
# print(a)
# print('-'*50)
# print(a[1:3,1:3])
# print(a[3,3])
# print(a[3,1:4])
# print('-'*50)
# print(a[:2])
# print('-'*50)
# print(a[:,2])
# print('-'*50)
# print(a[::2,2])
# print(a[1:3,1:3])
##########################################
# a=np.arange(1,37).reshape((4,3,3))
# print(a)
# # print(a[2,2])
# # print(a[2,2,:])
# # print(a[:,1:3,2])
# # print(a[::2,1:3,2])
# print(a[0,0,1])

##########################################
# B=np.arange(1,10).reshape(3,3)
# print(B)
# # print(B>4)
# # print(B*(B>4))
# # print(B[(B>7)])
# # print(B[(B%3)==1])
#
# B2=(B>2) & (B<7)  #bitwise 0&1 etc
# print(B[B2])

##########################################
# def sieve(n):
#     t1 = time() * 1000
#     b_list=[True]*(n+1)
#     for i in range(2,n+1):
#         if b_list[i]:
#             for j in range(i*i,n+1,i):
#                 b_list[j]=False
#     primes=[i for i in range(2,n+1) if b_list[i]]
#     t2 = time() * 1000
#     print('sieve took', t2 - t1, 'milliseconds.')
#     # return primes
#
# print(sieve(1000000))
#
#                 #OR
#
# def np_seive(n):
#     t1 = time() * 1000
#     B=np.ones(shape=n+1,dtype=bool)
#     B[0:2]=False
#     for i in range(2,n+1):
#         if B[i]:
#             B[i*i:n+1:i]=False
#     t2 = time() * 1000
#     print('np_sieve took', t2 - t1, 'milliseconds.')
#     # return np.arange(n+1)[B]
#
# print(np_seive(1000000))

##########################################
# A=ran.rand(5,2)
# A=ran.rand(10)
# print(A)

# A=ran.random(100000)
# print(np.mean(A))
# print(np.std(A))
# print(np.sum(A))
# print(np.median(A))

##########################################
# def get_std1(ls):
#     t1=time()
#     m=sum(ls)/len(ls)
#     ls2=[(i-m)**2 for i in ls]
#     sd=(sum(ls2)/len(ls2))**0.5
#     t2=time()
#     print('Python took ',t2-t1)
#
# def get_std2(A):
#     t1=time()
#     A2=(A-np.mean(A))**2
#     result=(np.mean(A2))**0.5
#     t2=time()
#     print('Numpy took ',t2-t1)
#
# def get_std3(A):
#     t1 = time()
#     result = np.std(A)
#     t2 = time()
#     print('np.std took', t2-t1)
#
# A=ran.rand(1000000)
# get_std1(A)
# get_std2(A)
# get_std3(A)

##########################################
# A=ran.randint(1,20,size=(3,4))
# print(A)
# # print(np.mean(A))
# print(np.mean(A,axis=0))
# print(np.mean(A,axis=1))

##########################################
# B=np.fromfunction(lambda r,c:c,shape=(4,5),dtype=np.int32)
# print(B)
# print(np.sum(B,axis=0))
# print(np.sum(B,axis=1))

##########################################
# B=np.fromfunction(lambda r,c:c,(4,5),dtype=np.int32)
# B_rows=np.sum(B,axis=1)
# B1=np.c_[B,B_rows]
# print(B1)
# B_rows=np.sum(B1,axis=0)
# print(B_rows)
# B1=np.r_[B1,[B_rows]]
# print(B1)

##########################################
def spreadsheet(A):
    AC=np.sum(A,axis=1)
    A2=np.c_[A,AC]
    AR=np.sum(A2,axis=0)
    return np.r_[A2,[AR]]

arr=np.arange(15).reshape(3,5)
print(arr)
print(spreadsheet(arr))
##########################################