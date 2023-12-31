import json
import os
# help(os)

# print(os.getcwd())
# os.chdir('C:\\Users\\pc\\Downloads\\Telegram Desktop')
# if os.path.isfile('./x.mkv'):
#     print('File removed')
#     os.remove('./x.mkv')
# print(os.path.isfile('./x.mkv'))
# print(os.listdir())
# print(os.listdir('D:\sem3'+'\\'+os.listdir('D:\sem3')[0]))

#################################################################
# while True:
#     try:
#         fname=input('Enter file to read:')
#         f=open(fname,'r')
#         print(f.read())
#     except FileNotFoundError:
#         print('File {} not found'.format(fname))
#     else:
#         f.close()
#         break

#################################################################
# with open('Chapter_08.py','r') as f:
#     # lst=f.readline(5)
#     # lst=f.readline()
#     # lst=f.readlines()
#     lst=f.read(10)
#     for thing in lst:
#         print(thing,end='\n')
#         print('-'*50)
#################################################################
# with open('file.txt' ,'w') as f:
#     f.write('To be or not to be\n')
#     f.write('That is the question.\n')
#     f.write('Whether tis nobler in the mind\n')
#     f.write('To suffer the slings and arrows\n')
# with open('file.txt', 'r') as f:
#     print(f.read())

# with open('file.txt', 'r') as f:
#     s=' '
#     while s:
#         s=f.readline().rstrip('\n')
#         # s=f.readline()
#         # print(s,end='')
#         print(s)

# with open('file.txt', 'r') as f:
#     str_list = f.readlines()
#     for s in str_list:
#         print(s, end='')

#################################################################
import re
import operator
# stack = [] # Stack to hold the values.
# # Scanner object. Isolate each token and take
# # appropriate action: push a numeric value, but perform
# # operation on top two elements on stack if an operator
# # is found.
# scanner = re.Scanner([
# (r"[ \t\n]", lambda s, t: None),
# (r"-?(\d*\.)?\d+", lambda s, t:
# stack.append(float(t))),
# # (r"\d+", lambda s, t: stack.append(int(t))),
# (r"[+]", lambda s, t: bin_op(operator.add)),
# (r"[-]", lambda s, t: bin_op(operator.sub)),
# (r"[*]", lambda s, t: bin_op(operator.mul)),
# (r"[/]", lambda s, t: bin_op(operator.truediv)),
# (r"[\^]", lambda s, t: bin_op(operator.pow)),
# ])
# # Binary Operator function. Pop top two elements from
# # stack and push the result back on the stack.
# def bin_op(action):
#     op2, op1 = stack.pop(), stack.pop()
#     stack.append(action(op1, op2))
# def main():
#     while True:
#         input_str = input('Enter RPN line: ')
#         if not input_str:
#              break
#         try:
#             tokens, unknown =scanner.scan(input_str)
#             if unknown:
#                 print('Unrecognized input:', unknown)
#             else:
#                 print(str(stack[-1]))
#         except IndexError:
#             print('Stack underflow.')
# main()

#################################################################
# stack = [] # Stack to hold the values.
# # Scanner object. Isolate each token and take
# # appropriate action: push a numeric value, but perform
# # operation on top two elements on stack if an operator
# # is found.
# scanner = re.Scanner([
# (r"[ \t\n]", lambda s, t: None),
# (r"-?(\d*\.)?\d+", lambda s, t:
# stack.append(float(t))),
# # (r"\d+", lambda s, t: stack.append(int(t))),
# (r"[+]", lambda s, t: bin_op(operator.add)),
# (r"[-]", lambda s, t: bin_op(operator.sub)),
# (r"[*]", lambda s, t: bin_op(operator.mul)),
# (r"[/]", lambda s, t: bin_op(operator.truediv)),
# (r"[\^]", lambda s, t: bin_op(operator.pow)),
# ])
# # Binary Operator function. Pop top two elements from
# # stack and push the result back on the stack.
# def bin_op(action):
#     op2, op1 = stack.pop(), stack.pop()
#     stack.append(action(op1, op2))
#
# def open_rpn_file():
#     '''Open-source-file function. Open a named
#     file and read lines into a list, which is
#     returned.
#     '''
#     while True:
#         try:
#             fname = input('Enter RPN source: ')
#             f = open(fname, 'r')
#             if not f:
#                 return None
#             else:
#                 break
#         except:
#             print('File not found. Re-enter.')
#     a_list = f.readlines()
#     return a_list
#
# def main():
#     a_list=open_rpn_file()
#     if not a_list:
#         print('Bye')
#         return
#
#     for a_line in a_list:
#         a_line=a_line.strip()
#         if a_line:
#             tokens,unknown=scanner.scan(a_line)
#             if unknown:
#                 print('Unregognized input')
#             else:
#                 print(str(stack[-1]))
# main()
#################################################################
# import re
# import operator
# # Provide a symbol table; values of variables will be
# # stored here.
# sym_tab = { }
# stack = [] # Stack to hold the values.
# # Scanner: Add items to recognize variable names, which
# # are stored in the symbol table, and to perform
# # assignments, which enter values into the sym. table.
# scanner = re.Scanner([
# (r"[ \t\n]", lambda s, t: None),
# (r"[+-]*(\d*\.)?\d+", lambda s, t:stack.append(float(t))),
# (r"[a-zA-Z_][a-zA-Z_0-9]*", lambda s, t:stack.append(t)),
# (r"\d+", lambda s, t: stack.append(int(t))),
# (r"[+]", lambda s, t: bin_op(operator.add)),
# (r"[-]", lambda s, t: bin_op(operator.sub)),
# (r"[*]", lambda s, t: bin_op(operator.mul)),
# (r"[/]", lambda s, t: bin_op(operator.truediv)),
# (r"[\^]", lambda s, t: bin_op(operator.pow)),
# (r"[=]", lambda s, t: assign_op()),
# ])
# def assign_op():
#     '''Assignment Operator function: Pop off a name
#     and a value, and make a symbol-table entry.
#     Remember to look up op2 in the symbol table if it is a string.
#     '''
#     op2, op1 = stack.pop(), stack.pop()
#     if type(op2) == str: # Source may be another var!
#         op2 = sym_tab[op2]
#     sym_tab[op1] = op2
# def bin_op(action):
#     '''Binary Operation evaluator: If an operand is
#     a variable name, look it up in the symbol table
#     and replace with the corresponding value, before
#     being evaluated.
#     '''
#     op2, op1 = stack.pop(), stack.pop()
#     if type(op1) == str:
#         op1 = sym_tab[op1]
#     if type(op2) == str:
#         op2 = sym_tab[op2]
#     stack.append(action(op1, op2))
# def main():
#     a_list = open_rpn_file()
#     if not a_list:
#         print('Bye!')
#         return
#     for a_line in a_list:
#         a_line = a_line.strip()
#         if a_line:
#             tokens, unknown = scanner.scan(a_line)
#             if unknown:
#                 print('Unrecognized input:', unknown)
#     print(str(stack[-1]))
# def open_rpn_file():
#     '''Open-source-file function. Open a named
#     file and read lines into a list, which is
#     returned.
#     '''
#     while True:
#         try:
#             fname = input('Enter RPN source: ')
#             if not fname:
#                 return None
#             f = open(fname, 'r')
#             break
#         except:
#             print('File not found. Re-enter.')
#     a_list = f.readlines()
#     return a_list
# main()

#################################################################
# with open('my.dat','wb') as f:
#     f.write(b'\x01\x02\x03\x10')
# with open('my.dat','rb') as f:
#     bss=f.read()
#     for i in bss:
#         print(i)
#     if(f.seekable()):
#         f.seek(0,0)
#         print(list(f.read()))

#################################################################
# import struct
# from struct import pack,unpack,calcsize
#
# def write_num(fname,n):
#     with open(fname,'wb') as f:
#         bss=pack('h',n)
#         f.write(bss)
#
# def read_num(fname):
#     with open(fname,'rb') as f:
#         bss=f.read(calcsize('h'))
#         t=struct.unpack('h',bss)
#         return t[0]
#
#
# write_num('silly.dat',125)
# print(read_num('silly.dat'))

#################################################################
# import struct
# from struct import pack,unpack,calcsize
#
# def write_floats(fname,x,y,z):
#     with open(fname,'wb') as f:
#         bss=pack('fff',x,y,z)
#         f.write(bss)
#
# def read_num(fname):
#     with open(fname,'rb') as f:
#         # bss=f.read(calcsize('fff'))
#         bss=f.read(calcsize('3f'))
#         t=struct.unpack('fff',bss)
#         return t
#
#
# write_floats('silly.dat',1,20.2,5.78)
# print(read_num('silly.dat'))

#################################################################
# import struct
# from struct import pack,unpack,calcsize
#
# def write_fixed_str(fname,n,s):
#     with open(fname,'wb') as f:
#         bss=pack(str(n)+'s',s.encode('utf-8'))
#         f.write(bss)
#
# def read_fixed_str(fname,n):
#     with open(fname,'rb') as f:
#         bss=f.read(n)
#         return bss.decode('utf-8')
#
# write_fixed_str('king.d', 13, "I'm Henry the VIII I am!")
# print(read_fixed_str('king.d', 13))
#################################################################
# from struct import pack,unpack,calcsize
#
# def write_var_str(fname,s):
#     with open(fname,'wb') as f:
#         n=len(s)
#         fmt = 'h' + str(n) + 's'
#         bss=pack(fmt,n,s.encode('utf-8'))
#         f.write(bss)
#
# def read_var_str(fname):
#     with open(fname,'rb') as f:
#         bss=f.read(calcsize('h'))
#         n=unpack('h',bss)[0]
#         bss = f.read(n)
#         return bss.decode('utf-8')
#
# write_var_str('silly.dat', "I'm Henry the VIII I am!")
# print(read_var_str('silly.dat'))

#################################################################
# from struct import pack, unpack, calcsize
#
# def write_rec(fname,name,addr,rating):
#     with open(fname,'wb') as f:
#         bname=name.encode('utf-8')
#         baddr=addr.encode('utf-8')
#         bss=pack('9s10sf',bname,baddr,rating)
#         f.write(bss)
#
# def read_rec(fname):
#     with open(fname,'rb') as f:
#         bss=f.read(calcsize('9s10sf'))
#         bname,baddr,rating=unpack('9s10sf',bss)
#         name=bname.decode('utf-8').rstrip('\x00')
#         addr=baddr.decode('utf-8').rstrip('\x00')
#         return name,addr,rating
#
# write_rec('goofy.dat', 'Cleo', 'Main St.', 5.0)
# print(read_rec('goofy.dat'))
#################################################################
# import struct
#
# with open('junk.dat','wb+') as f:
#     bstr=struct.pack('hhh',1,2,100)
#     datlen=f.write(bstr)
#     f.seek(0,0)
#     bstr=f.read(struct.calcsize('hhh'))
#     a,b,c=struct.unpack('hhh',bstr)
#     print(a,b,c)

#################################################################
# import pickle
#
# with open('goo.dat','wb+') as f:
#     pickle.dump([1,2,3],f)
#     pickle.dump('Hello!',f)
#     pickle.dump(3.141592,f)
#
#     f.seek(0,0)
#     a=pickle.load(f)
#     b=pickle.load(f)
#     c=pickle.load(f)
#     print(type(a),a)
#     print(type(b),b)
#     print(type(c),c)

#################################################################
import shelve
nums=shelve.open('numdb')
nums['pi']=(3.141592,False)
nums['phi']=(2.1828,False)
nums['perfect']=(6,True)
nums.close()

nums=shelve.open('numdb')
for thing in nums.items():
    print(thing[0],thing[1])
nums.close()
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################