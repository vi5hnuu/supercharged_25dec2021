# print('%s %d'%('vishnu',15))
# print('x','y')
# print('x','y',end=' ext ')
# print('x','y',sep=' ok ')
# print('x','y',sep=' ok ',end=' ext ')

##############################################
# import random
# print(random.randint(1,1))
##############################################
# print('vishnu\nkrishan')
# print("vishnu\nkrishan")
# print('''vishnu
#   krishan''')
# print("""vishnu
#   krisha\nn""")
##############################################
# a_list=[]
# while True:
#     s=input('Enter name :')
#     if not s:
#         break
#     a_list.append(s)
# print(a_list)
# print(sorted(a_list))
# print(sorted(a_list,reverse=True))
# print(a_list)
# print(a_list.sort())
# a_list.sort(reverse=True)
# print(a_list)
##############################################
# a,b,c=[1,2,3]
# aa,bb,cc=(1,2,3)
# print(a,b,c)
# print(aa,bb,cc)
##############################################
# temp_dict={'vishnu':20,'krishan':18}
# print(temp_dict['vishnu'])
# # print(temp_dict['vishn'])
# print(temp_dict.get('vishn','No such key'))
# print(temp_dict.get('vishn'))


# s=input('Enter a string :').split()
# s=list(input('Enter a string :'))
# wrd_counter={}
# for wrd in s:
#     wrd_counter[wrd]=wrd_counter.get(wrd,0)+1
# print(wrd_counter)
##############################################

# s=input('Enter a string :').split()
# ss=input('Enter a string :').split(maxsplit=2)
# x=input('Enter a string :').split('i',maxsplit=2)
# sss=input('Enter a string :').rsplit(maxsplit=2)
# print(s)
# print(ss)
# print(x)
# print(sss)
##############################################
# setA = {1, 2, 3, 4}
# setB = {3, 4, 5}
# setUnion = setA | setB # Assign {1, 2, 3, 4,5}
# setIntersect = setA & setB # Assign {3, 4}
# setXOR = setA ^ setB # Assign {1, 2,5}
# setSub = setA - setB # Assign {1, 2}
##############################################
# x=5
#
# def temp():
#     return x
#
# print(temp())

# x=5
# def temp():
#     x+=1
#     return x
#
# print(temp())

count = 10
# def funcA():
#     count = 20
#     print(count) # Prints 20, a local value.
#     # global count
#     # print(count)



# def funcA():
#     global count
#     print(count) # Prints 20, a local value.
#     count+=1
#     print(count)
# def funcB():
#     print(count) # Prints 10, the global value.
#
#
# def funC():
#     global m
#     m=15
#     print(m)
# funcA()
# funcB()
# funC()
# print(m)
##############################################