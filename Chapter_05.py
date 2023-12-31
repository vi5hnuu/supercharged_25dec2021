# a,b=10,11
# c=a+b
# print('%d plus %d equals %d.'%(a,b,c))

# tupl=10,20,30
# print('Answers are %d %d %d'%tupl)
# print('Answers are %s %s %s'%tupl)

########################################
# h1=int('e9',16)
# h2=int('10',16)
# print('The result is %x'%(h1+h2))

########################################
# print('This is the right justification %12d'%(15))
# print('This is the left justification %-12d'%(15))
# print('My name is %5s.' % 'vishnu')
# print('My name is %5.2s.' % 'vishnu')
# print('My name is %-5.2s.' % 'vishnu')
# print('This is the left justification %-12.5d'%(15))
#
# # x=12,y=5
# x=12
# y=5
# print('This is the left justification %-*.*d'%(x,y,15))

########################################
# print(format(150**200,','))
# print(format('vishnu','20'))
# print(format('vishnu','20'))
# print(format(55,'20'))
# print(format('vishnu','6.3'))
# print(format(3.141516,'6.3'))

########################################
# print('{} plus {} equals {}.'.format(25, 75, 100))
# print('{1} plus {0} equals {2}.'.format(25, 75, 100))
# print('{x} plus {y} equals {z}.'.format(x=25, y=75, z=100))
# print('Set = {{{}, {}}}'.format(1, 2))
#
# fss = 'The items are {3}, {1}, {0}.'
# print(fss.format(10, 20, 30, 40))  #excess arguement
#
# print('{0}, {0}, {1}, {1}'.format(100, 200))
# # { [position] [!r|s|a] [: spec ] }
#
# lst=[10,11,12]
# print('a={0[0]} b={0[1]} c={0[2]}'.format(lst))
# print('a={a[0]} b={a[1]} c={a[2]}'.format(a=lst))

########################################
# print(10)
# print(str(10))
# print(repr(10))
#
# test_str='Here is a \nNew line'
# print(test_str)
# print(repr(test_str))
#
# print('{}'.format(test_str))
# print('{!r}'.format(test_str))
#
# print('{1!r} loves {0!r}'.format('vishnu\t','krishan'))
# print('{1!a} loves {0!a}'.format('vishnu\t','krishan'))
# print('{1!s} loves {0!s}'.format('vishnu\t','krishan'))

########################################
# print(format(32000.3,'*<+15,.3f'))
#
# n1,n2=777.2,999
# print('**{:0>+10,.2}**{:2}**'.format(n1,n2))
# print('**{:0<+10,.2}**{:2}**'.format(n1,n2))
# print('**{:m^+10,.2}**{:2}**'.format(n1,n2))
# print('**{:0=+10,.2}**{:2}**'.format(n1,n2)) #for numeric data only
#
# print(format('Lady','@>7'))
#
# print('results>{: },{:+},{:-}'.format(-25, -25,-25))
# print('results>{: },{:+},{:-}'.format(-25, -25,+25))
# print('results>{: },{:},{:}'.format(-25, -25,+25)) #it won't change sign
# print('results>{: },{:+},{:}'.format(25, 25,+25)) #show - by default but not +

# print('{:0>+10,} {:+010,}'.format(25,25))
# print('{1:+010,}'.format(25,26))

# pi=3.14159265
# phi=1.618
# # fss='{:.2} + {:.2} = {:.2}'
# fsss='{:.3} + {:.3} = {:.3}'
# fss='{:010,.3f} + {:010,.3f} = {:010,.3f}'
# print(fss.format(pi,phi,pi+phi))
# print(fsss.format(pi,phi,pi+phi))

# fss='{:10.2f}'
# for x in [22.7,3.1415,555.5,29,1010.013]:
#     print(fss.format(x))

# print('{:#b} {:b} {:b}'.format(5,6,16))
# print('{0:#o}, {0:#x}, {0:#X}'.format(63))
# print('{0:.2%}, {0:.2%}, {0:.2%}'.format(0.9))
########################################
# def calc_binary():
#     print('Enter values in binary only')
#     b1=int(input('Enter b1 :'),2)
#     b2=int(input('Enter b2 :'),2)
#     print('Total is :{:#b}'.format(b1+b2))
#     print('{:#b} + {:#b} = {}'.format(b1,b2,b1+b2))
#
# calc_binary()
########################################
print('Here is a num :{:{}.{}}'.format(1.2345,10,4))
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################