# class x:
#     def __init__(self):
#         self.name='vishnu'
#
# name=x() #multable
# name2=name
# print(id(name))
# print(id(name2))
# print((name.name))
# print((name2.name))
# name.name='krishan'
#
# print(name2.name)
# print(name.name)
# print(id(name.name))
# print(id(name2.name))

###########################
# lst=[1,2]
# x,y=lst.pop(),lst.pop()
# print(x,y)

###########################
# dict={'x':10}
# # # print(dict.pop('x'))
# # # print(dict)
# print(dict['x'])
# print(dict.__getitem__('x'))
# dict['y']=12
# dict.__setitem__('z',13)
# print(dict)

###########################
# class x:
#     m=15
#     def __init__(self):
#         print(x.m)
#
# obj=x()
# print(x.__dict__)
# print(obj.__dict__)
# x.m=20
# print(x.__dict__)
# print(obj.__dict__)
# obj.m=21 #on fly
# print(x.__dict__)
# print(obj.__dict__)


#can i make class variable private
class x:
    __m=15 #private cant be accessed outside the class now
    def __init__(self):
        print(x.__m)
        print('HEY')
obj=x()
print(x.__dict__)
print(obj.__dict__)
# x.m=20 #on fly new class variable
# print(x.__dict__)
# print(obj.__dict__)
# obj.m=21
# print(x.__dict__)
# print(obj.__dict__)

###########################
###########################
###########################