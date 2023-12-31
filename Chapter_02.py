# # s = '45'
# s = '45.0'
# # n = int(s)
# x = float(s)
# print(s,x,sep='\n')
# # print(s,n,x,sep='\n')

####################################
# print(int('12',10))
# print(int('111',2))
# print(int('f',16))
####################################
# dog1_str = 'Rover' # Assignment  #immutable
# dog2_str = dog1_str # Create alias for.
# print(dog1_str == dog2_str)# True!
# print(dog1_str == 'Rover') # True!
# print(id(dog1_str))
# print(id(dog2_str))
# dog1_str='vishnu'
# print(dog1_str)
# print(dog2_str)
# print(id(dog1_str))
# print(id(dog2_str))


# dog1_str = 12 # Assignment  #immutable
# dog2_str = dog1_str # Create alias for.
# print(dog1_str == dog2_str)# True!
# print(dog1_str == 12) # True!
# print(id(dog1_str))
# print(id(dog2_str))
# dog1_str=13
# print(dog1_str)
# print(dog2_str)
# print(id(dog1_str))
# print(id(dog2_str)) #==old id(dog1_str)
####################################
# def compare_no_case(str1,str2):
#     # return  str1.casefold()==str2.casefold() #for wider unicode
#     return  str1.lower()==str2.lower()
#
# print(compare_no_case('cat','CAT'))
####################################
# print('vishnu'*2)
# print(['vishnu']*2)
####################################
# temp=['vishnu'] #mutable     #imutable iniitially create reference
# # temp1=temp[:]
# temp1=temp
# print(id(temp))
# print(id(temp1))
# print(temp)
# print(temp1)
# temp[0]='krishan'
# print(id(temp))
# print(id(temp1))
# print(temp)
# print(temp1)
# temp=['krishan']
# print(id(temp))
# print(id(temp1))
# print(temp)
# print(temp1)
####################################
# print('vishnu'[10:1])
####################################
# print(' ' in 'cat') # Prints false
# print('' in 'cat') # Prints True #empty string
# print([] in [1, 2, 3]) # Prints False
####################################
# temp=['b','a','c']
# temp.sort() #they expect iterable
# print(temp)
# print(sorted('c,ab')) #they expect iterable
# print(sorted(list('c,ab'))) #they expect iterable
####################################
# print(bin(15))
# print(hex(15))
# print(oct(15))
####################################
# print('__init__'.isidentifier())
# print('2__init__'.isidentifier())
####################################
# print('ViSHanU'.swapcase())
####################################
# temp='vishnu'
# print(temp.startswith('vish'))
# print(temp.startswith('ish',1))
# print(temp.startswith('ish',1,55))
# print(temp.startswith('ish',1,2))
# print(temp.endswith('hnu'))
# print(temp.endswith('hnu',-3))
# print(temp.endswith('ish',-5,55))
# print(temp.endswith('sh',-4,2))

####################################
temp='vishnu kumar kumar kumar vishnu'
#temp='vishnu kumar vishnu'.split() #count work differenetly on list
# print(temp)
# print(temp.count('vishnu'))
# print(temp.count('vishnu',1)) #invalid second arg if temp is list
# print(temp.count('vishnu',1,55)) #invalid second, third arg if temp is list

# print(temp.find('kumar',5)) #raise no exp
# print(temp.find('kumar',5,55))
# print(temp.index('kumar',6)) #raise exp
# print(temp.index('kumar',6,55)) #return first found
# print(temp.rindex('kumar',6)) #return first found from reverse
# print(temp.rindex('kumar',6,55))
# print(temp)
# print(id(temp))
# print(temp.replace('kumar','KUMAR',2)) #only return new string as string is immutable
# print(id(temp))
# print(temp)
####################################
# stooge_list = 'Moe   Larry Curly Shemp'.split(' ')
# print(stooge_list)
####################################
# print('   vishun   '.strip())
# print('   vishun   '.lstrip())
# print('   vishun   '.rstrip())

# print('###vishun###'.strip('#'))
# print('###vishun###'.lstrip('#'))
# print('###vishun###'.rstrip('#'))

print('vishnu'.ljust(20,'*'))
print('vishnu'.rjust(20,'*'))
print('vishnu'.center(20,'*'))
print('98'.zfill(20))
print('+98'.zfill(20))
print('vishnu'.zfill(20))

####################################
