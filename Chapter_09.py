import random
import math

# class car:
#     accel=3.0
#     mpg=25
#
# car1=car()
# car2=car()
# car2.accel=50
#
# print(car1.accel)
# print(car1.mpg)
# print('-'*30)
# print(car2.accel)
# print(car2.mpg)
# print('-'*30)
# print(car.accel)
# print(car.mpg)
# print('-'*30)
# print(car.__dict__)
# print(car1.__dict__)
# print(car2.__dict__)

########################################
# class x:
#     pass
#
# obj1=x()
# print(obj1.__dict__)
# print(x.__dict__)
#
# obj1.name='vishnu'
# obj1.age=20
#
# print(obj1.__dict__)
# print(x.__dict__)
#
# obj2=x()
# print(obj2.__dict__)  #those attributs(self) are only for that objects created on the fly
# print(x.__dict__)

########################################
# class dog:
#     def __init__(self,name,breed,age):
#         self.name=name
#         self.breed=breed
#         self.age=age
#
# top_dog=dog('Handsome dan','bulldog','10')
# print(top_dog) #mutable

########################################
# class Mammal:
#     def __init__(self, name, size):
#         print('In mammal')
#         self.name = name
#         self.size = size
#     def speak(self):
#         print('My name is',self.name)
#     def call_out(self):
#         self.speak()
#         self.speak()
#         self.speak()
# class Dog(Mammal):
#     def __init__(self,name,size,breed):
#         print('In Dog')
#         super().__init__(name,size)
#         self.breed=breed
#     def speak(self):
#         print('ARF!!')
# class Cat(Mammal):
#         def speak(self):
#             print('Purrrrrrr!!!!')
#
# dog1=Dog('bulldog',12,'xyz')
# print(dog1.__dict__)
# print(Dog.__dict__)
# print(Mammal.__dict__)

########################################
# class point:
#     big_prime_1=1200556037
#     big_prime_2=2444555677
#
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#
#     def __str__(self):
#         s=str(self.x)+' , '
#         s+=str(self.y)
#         return s
#
#     def __repr__(self):
#         s='point('+str(self.x)+' , '
#         s+=str(self.y)+')'
#         return s
#
#     def __hash__(self):
#         n=self.x*self.big_prime_1
#         return (n+self.y)%self.big_prime_2
#
#     def __bool__(self):
#         return self.x and self.y
#
# pt=point(3,4)
# # pt1=point(3,4)
# # print(pt<pt1)
# print(repr(pt))
# print(str(pt))
# print(pt.__dict__)
# print(point.__dict__)

########################################
# class Dog:
#     def __init__(self,n):
#         self.n=n
#
#     def __eq__(self, other):
#         return  self.n==other.n
#
#     def __lt__(self, other):
#         return self.n<other.n
#
#     def __le__(self, other):
#         return self.n<=other.n
#
# d1=[Dog(x) for x in range(10)]
# random.shuffle(d1)
#
# for x in d1:
#     print(x.n,end=' ')
# print()
# print('-'*30)
# d1.sort()
# for x in d1:
#     print(x.n,end=' ')

########################################
###############
# class x:
#     pass
#
# m=x()
# print(type(m))
# print(type(m)==x)

###############
# class Dog:
#     def __init__(self,d):
#         self.d=d
#
#     def __gt__(self, other):
#         if type(other)==Dog:
#             return self.d>other.d
#         else:
#             return self.d>other
#
#     def __lt__(self, other):
#         if type(other)==Dog:
#             return self.d<other.d
#         else:
#             return self.d<other
#
#     def __repr__(self):
#         return "Dog(" + str(self.d) + ")"
#
# d1, d5, d10 = Dog(1), Dog(5), 10 #print(d5) call __repr__
# a_list = [50, d5, 100, d1, -20, d10, 3]
# a_list.sort()
# print(a_list)

#######################################
# import fractions
#
# f=fractions.Fraction(1,2)
# print(1+f) #call Fraction.__add__
# print(f+1) #call Fraction.__radd__

########################################
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
#     def __add__(self, other):
#         return Point(self.x + other.x,self.y + other.y) #return reference #mutable
#
#     def __sub__(self, other):
#         ''' Return the distance between points.'''
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return (dx * dx + dy * dy) ** 0.5
#
#     def __mul__(self, n):
#         newx=self.x*n
#         newy=self.y*n
#         return Point(newx,newy)
#
#     def __neg__(self):
#         newx=-self.x
#         newy=-self.y
#         return Point(newx,newy)
#
#     def __trunc__(self):
#         newx = self.x.__trunc__() #truncate function of int class
#         newy = self.y.__trunc__()
#         return Point(newx, newy)
#
# # pt1 = Point(10, 15)
# # # pt2=pt1 #refere to same object #alias
# # # pt2 = -pt1 # because of - it make new object and give that address to it(remember run time checking)
# # pt2 = pt1.__neg__()
# # print(pt2.x,pt2.y,sep='\t')
#
# # pt1 = Point(5.5, -6.6)
# # pt2 = math.trunc(pt1)
# # print(pt2.x, ', ', pt2.y, sep='')

########################################
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#
#     def __int__(self):
#         return int(self.x)+int(self.y)  #__int__ of respective(value in x or y) class
#
#     def __float__(self):
#         return float(self.x)+float(self.y)  #__float__ of respective(value in x or y) class
#
# p = Point(1, 2.5)
# print(int(p))
# print(float(p))

########################################
# class Stack:
#     def __init__(self):
#         self.__mylist=[]
#
#     def append(self,v):
#         self.__mylist.append(v)
#
#     def push(self,v):
#         self.__mylist.append(v)
#
#     def pop(self):
#         return self.__mylist.pop()
#
#     def peek(self):
#         return  self.__mylist[-1]
#
#     def __len__(self):
#         return len(self.__mylist)
#
#     def __contains__(self, item):
#         return self.__mylist.__contains__(item)
#
#     def __getitem__(self, index):
#         return self.__mylist[index]
#
#     def __setitem__(self, key, value):
#         self.__mylist[key]=value
#
#         def __iter__(self):
#             self.current = 0
#             return self
#
#
#         def __next__(self):
#              if self.current < len(self.__mylist):
#                 self.current += 1
#                 return self.__mylist[self.current - 1]
#             else:
#                 raise StopIteration
#
# st = Stack()
# st.push(10)
# st.push(20)
# st.push(30)
# st.push(40)
# print('Size of stack is:', len(st))
# print('First elem is:', st[0])
# print('The top of the stack is:', st.peek())
# print(st.pop())
# print(st.pop())
# print(st.pop())
# print('Size of stack is:', len(st))
# st[0]=12
# print('First elem is:', st[0])

                    # OR

# class Stack(list):
#     def push(self,v):
#         self.append(v)
#
#     def peek(self):
#         return  self[-1]
#
#     def __iter__(self):
#         self.current=0
#         return self
#
#     def __next__(self):
#         if self.current<len(self):
#             self.current+=1
#             return  self[self.current-1]
#         else:
#             raise  StopIteration


#
#
# st = Stack()
# st.push(10)
# st.push(20)
# st.push(30)
# st.push(40)
# print('Size of stack is:', len(st))
# print('First elem is:', st[0])
# print('The top of the stack is:', st.peek())
# print(st.pop())
# print(st.pop())
# print(st.pop())
# print('Size of stack is:', len(st))
# st[0]=12
# print('First elem is:', st[0])

########################################
# n = 5
# # if isinstance(n, int):
# #     print('n is an integer or derived from it.')
#
# if isinstance(n,(int,float)):
#     print('n is numeric.')

########################################
# print(NotImplemented)

########################################
# class Dog:
#     pass
# d=Dog()
# setattr(d,'breed','gread dane')
# print(getattr(d,'breed'))
# print(d.breed)
#
# d.__name='vishnu' #created private varible on fly(another method other than set and get attributes)
# print(d.__dict__)
# print(Dog.__dict__)

########################################