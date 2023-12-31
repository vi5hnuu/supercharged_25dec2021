# family_names='vishnu'\
#              'krishan'
# print(family_names)
#
# print('vishnu''krishan')
####################################
# str_list = []
# n = ord('a')
# for i in range(n, n + 26):
#     str_list += chr(i)
# alphabet_str = ''.join(str_list)
# print(alphabet_str)
#
# z=[]
# z+='ibc' # ibc is trated as list
# # z+=5 #error
# print(z)
####################################
# a=5
# b=5
# print(a is b) #address not content

# a=[5]
# b=[5]
# print(a is b)
# b=a
# print(a is b)
# a[0]=15
# print(a is b)

####################################
# # a,b=5,6,7 #error
# a,*b=5,6,7
# print(a,b)
#
# a,*b,c=(5,6,7,8,9,10)
# print(a,b,c)
#
# a,*b,c=(5,10)
# print(a,b,c)

# sttr='vishnuvkkv'
# print(sttr.replace('v',''))
# print(sttr.replace('v','',2))
####################################
# print(2<3<5)
# print(2<4<3)
# print(0 or 5)
# print(0 and 5)

####################################
# a, b, c = 5, 10, 15
# if 0 < a <= c > b > 1:
#     print('All these comparisons are true!')
#     print('c is equal or greater than all the rest!')
#
# a = b = c = d = e = 100
# if a == b == c == d == e:
#     print('All the variables are equal to each other.')
####################################
# for i in range(1,11): print(i)
# for i in range(1,11): print(i);print(i*i) #no indentation required
# a = 1; b = 2; c = a + b; print(c)
####################################
# one,two,three,four,five=range(1,6)
# print(one,two,three,four,five)

# import enum
# help(enum)
####################################
# def quad(a, b, c):
#     '''Quadratic Formula function.
#     This function applies the Quadratic Formula
#     to determine the roots of x in a quadratic
#     equation of the form ax^2 + bx + c = 0.
#     '''
#     determin = (b * b - 4 * a * c) ** .5
#     x1 = (-b + determin) / (2 * a)
#     x2 = (-b - determin) / (2 * a)
#     return x1, x2
#
# help(quad)
# print(dir(quad))
# print(quad.__sizeof__())
# print(vars(quad))
####################################
# a=[1,2]
# print(id(a[0]),id(a[1])) #non continuous memory
####################################
# def avg(a_list):
#     '''To calculate avg'''
#     x=(sum(a_list)/len(a_list))
#     return x
#
# print(type(avg))
# new_avg=avg
# print(new_avg([1,2,3]))
#
#
# def func_info(func):
#     print('Name of the function :',func.__name__)
#     print('Function documentation :')
#     help(func)
# func_info(new_avg)

####################################
# a,*b,c=1,2,3,4,5,6
# print(a,b,c)
# def my_var_func(*args):
#     print(args,type(args))
#     print('The number of args is', len(args))
#     for item in args:
#         print(item)
#
# my_var_func(1,2,3,4,5)
####################################
import time


# def fun_name_info(func):
#     def wrapper():
#         t1=time.time()
#         ret_val=func()
#         t2=time.time()
#         print('Time taken :',(t2-t1)*1000)
#         return ret_val
#     return wrapper
#
# def summ():
#     return sum([1,2,3])

# def fun_name_info(func):
#     def wrapper():
#         t1=time.time()
#         ret_val=func()
#         t2=time.time()
#         print('Time taken :',(t2-t1)*1000)
#         return ret_val
#     return wrapper
#
# @fun_name_info
# def summ():
#     return sum([1,2,3])
#
# print(summ())

# def fun_name_info(func):
#     def wrapper(*args,**kwargs):
#         t1=time.time()
#         ret_val=func(*args,**kwargs)
#         t2=time.time()
#         print('Time taken :',(t2-t1)*1000)
#         return ret_val
#     return wrapper
#
#
# def summ(*args,**kwargs):
#     print(args)
#     print(kwargs['a'])
#     return sum(args)
#
# # print(fun_name_info(summ)([1,2,3,4,5],a=10))  #args=([1,2,3,4,5],)  sum(args) ?
# print(fun_name_info(summ)(*[1,2,3,4,5],a=10))
# print(summ(*[1,2,3,4,5],a=10))
####################################
# def print_even():
#     for n in range(2,11,2):
#         print(n)  #can we replace it with reuturn ?

# def print_even():
#     for n in range(2,11,2):
#             yield n #kind of returning and saving the state
# for x in print_even(): #iterator
#     print(x)
# print('-'*50)
# gen_obj=print_even()
# print(gen_obj.__next__())
# print(next(gen_obj))
#
# # print(list(print_even()))
# # print(type(print_even()))
#
#
# str='vishnu' #iterable
# # print(next(str)) #wrong
#
# print('__next__' in dir(str))
# print('__next__' in dir(gen_obj))


# def even():
#     for x in range(2,20,2):
#         yield x
#
# x=list(even())
# xx=list(even())
# print(x)
# print(xx)
#
# m=even()
# x=list(m)
# xx=list(m)
# print(x)
# print(xx)
####################################
# import sys
# for thing in sys.argv:
#     print(thing)
# print(sys.argv)
####################################

####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################