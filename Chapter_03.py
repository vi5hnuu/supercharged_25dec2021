################################
# print(type('+98'.zfill(10)))
################################
# my_list = [1, 2, 3]
# print(my_list.remove(1))
# del my_list[1]
# print(my_list)
# print(my_list.clear())
# print(my_list)
# my_list.append(5)
# my_list.append(6)
# my_list.extend([1,2])
# print(my_list)
################################bad idea of copy
# a_list = [2, 5, 10]
# b_list = a_list
# print(id(a_list))
# print(id(b_list))
# b_list.append(100)
# a_list.append(200)
# b_list.append(1)
# print(a_list) # This prints [2, 5, 10, 100, 200,1]
################################
# a_list = [2, 5, 10]
# b_list = a_list.copy()
# print(id(a_list))
# print(id(b_list))
# b_list.append(100)
# a_list.append(200)
# b_list.append(1)
# print(a_list) # This prints [2, 5, 10, 200]
################################
# a_list = [2, 5, 10]
# b_list = a_list[:]
# print(id(a_list))
# print(id(b_list))
# b_list.append(100)
# a_list.append(200)
# b_list.append(1)
# print(a_list) # This prints [2, 5, 10, 200]
################################
################################
# temp=[11,22,33]
# # print(list(enumerate(temp)))
# print(list(enumerate(temp,start=1)))
# print(list(enumerate('vishnu')))  #enumerate(iterable)
# print(list(enumerate('vishnu',start=15)))  #enumerate(iterable)
################################
# my_list=[10,20,30,40,50,60]
# # my_list[2:6]=[300,400]
# # my_list[2:6]=[300,400,500]
# my_list[2:6]=[300,400,500,600] #size not matter
# my_list.insert(0,123)
# # my_list[0:0]=123
# my_list[0:0]=[[456]]
# print(my_list)

# # my_list[::2]=[1,3,5,7]  #size matters
# my_list[::2]=[1,3,5]
# print(my_list)
################################
#ok
# my_list=['a','a','a']
# my_list[0]='b'
# for x in my_list:
#     print(id(x),x)

#ok
# my_listt=['a']*3
# my_listt[0]='b'
# for x in my_listt:
#     print(id(x),x)

#not ok
# my_listt=[[1]]*3
# for x in my_listt:
#     print(x)
# my_listt[0][0]=5
# for x in my_listt:
#     print(id(x),x)

#ok
# my_listt=[[1],[1],[1]]
# for x in my_listt:
#     print(x)
# my_listt[0][0]=5
# for x in my_listt:
#     print(id(x),x)

####################deep copy############
# x=[[1,2,3],[1,2,3],[1,2,3]]
# for m in x:
#     print(id(m),m)
# #ok upto this
#
# #not ok
# print('-'*50)
# y=x.copy()
# for m in y:
#     print(id(m),m)
# x[0][0:3]=[1,2,3,4]
# print('-'*50)
# for m in y:
#     print(id(m),m)
#######
# from copy import  deepcopy
# x=[[1,2,3],[1,2,3],[1,2,3]]
# for m in x:
#     print(id(m),m)
# #ok upto this
#
# #ok  ===> address are same but they will change as soon as value changes
# print('-'*50)
# y=deepcopy(x)
# for m in y:
#     print(id(m),m)
# x[0][0:3]=[1,2,3,4]
# print('-'*50)
# for m in y:
#     print(id(m),m)

#######
# a_list = [1, 2, [5, 10]]
# b_list = a_list[:]  #deep copy of 1,2 ,[5,10] but ref of 5,10
# print(b_list)
# # a_list[0]=15
# # a_list[2]=12
# a_list[2][0]=0
# print(a_list)
# print(b_list)#changed

# from copy import deepcopy
# a_list = [1, 2, [5, 10]] #=>[data,data,reference]
# b_list = deepcopy(a_list)
# print(b_list)
# a_list[2][0]=0
# print(a_list)
# print(b_list)#NOT changed
################################
# print(None in [])
# a = [1, 2, 3]
# print(None in a) # This produces False
# print([] in a) # So does this.
# b = [1, 2, 3, [], None]
# print(None in b) # This produces True
# print([] in b) # So does this.
################################
# a_list=[10,20,40]
# a_list.insert(2,30)
# print(a_list)
# a_list.insert(100,33)
# print(a_list)
# a_list.insert(-100,44)
# print(a_list)
################################
# family_names=['Manisha','manisha','laxmi','krishan','vishnu']
# # family_names.sort()
# family_names.sort(key=lambda x:x.lower())
# print(family_names)
################################
# def ignore_case(s):
#     return s.casefold()
# a_list = [ 'john', 'paul', 'George', 'brian', 'Ringo' ]
# b_list = a_list[:]
# a_list.sort()
# b_list.sort(key=ignore_case)
# print(a_list)
# print(b_list)
################################
# the_stack=[]
#
# def push(v):
#     the_stack.append(v)
# def pop():
#     return the_stack.pop()
#
# def main():
#     s=input('Enter the RPN string :')
#     a_list=s.split()
#     for item in a_list:
#         if item in '+-*/':
#             if item=='-':
#                 push(pop()-pop())
#             if item=='+':
#                 push(pop()+pop())
#             if item=='*':
#                 push(pop()*pop())
#             if item=='/':
#                 push(pop()/pop())
#         else:
#             push(float(item))
#     print(pop())
# main()
################################
# import functools
# lst=[1,2,3,4,5,6]
# # print(list(map(lambda x:x**2,lst)))
# # print(list(map(lambda x:x%2==0,lst)))
# # print(list(filter(lambda x:x%2==0,lst)))
# print(functools.reduce(lambda x,y:x+y,lst))
################################
# a_list=[5,5,5,-20,2,-1,2]
# # my_set=set()
# # for i in a_list:
# #     if i>0:
# #         my_set.add(i)
# # print(my_set)
#
#
# my_set={i for i in a_list if i>0}
# print(my_set)

################################
# vals_list = [ ('pi', 3.14), ('phi', 1.618) ]
# my_dict={x:y for x,y in vals_list }
# print(my_dict)

key = [ 'pi', 'phi' ]
valu=[3.14,1.618]
my_dict={x:y for x,y in zip(key,valu) }
print(my_dict)
my_dict={y:x for x,y in my_dict.items()} #first have copy of mydict.items()
print(my_dict)
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################