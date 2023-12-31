import re
# pattern=r'\d\d\d-\d\d\d-\d\d\d\d' #123-456-789123465 pass
# pattern=r'\d\d\d-\d\d\d-\d\d\d\d$' #123-456-78915 fail
# pattern=r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d$' #123 456 7891 or 123-456-7891 etc
# s=input('Enter phone number :')
# print(re.match(pattern,s))
# if re.match(pattern,s):
#     print('Number accepted')
# else:
#     print('Number rejected')
#

# pattern=r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d' #123 456 7891 or 123-456-7891 etc
# s=input('Enter phone number :')
# print(re.fullmatch(pattern,s))
# if re.fullmatch(pattern,s):
#     print('Number accepted')
# else:
#     print('Number rejected')

####################################
# str=r'vishnu\n'
# print(str)

####################################
# reg=re.compile(r'ca*b$') #compile the pattern
#
# def test_item(s):
#     if re.match(reg,s):
#         print('Accepted')
#     else:
#         print('Rejected')
#
# test_item('caab')
# test_item('caaxxb')
####################################
# if re.match('m*ack','MACK the knife',re.IGNORECASE):
# if re.match('m*ack','MACK the knife',re.I):
# if re.match('m*ack','MACK the knife',re.I | re.DEBUG):
#     print('Match found')
####################################
# # if re.match(r'[+*^/-]','^'):
# if re.match(r'[^+*^/-]','^'):
#     print('success')
# else:
#     print('Failed')
####################################
# Each and every character must be an uppercase or lowercase letter,
# digit, or underscore (_), or one of the following punctuation
# characters: @, #, $, %, ^, &, *, or !.
# The minimum length is eight characters total.
# It must contain at least one letter.
# It must contain at least one digit.
# It must contain one of the accepted punctuation characters.

# pat1=r'(\w|[@#$%^&*!]){8,}$'
# pat2=r'.*\d'
# pat3=r'.*[a-zA-Z]'
# pat4=r'.*[@#$%^&*!]'
#
# def verify_password(s):
#     b=(re.match(pat1,s) and re.match(pat2,s) and re.match(pat3,s) and re.match(pat4,s))
#     return bool(b) # as it return object   i.e  x= 5 and 2 ==>x=2
#
# print(verify_password('Vishu@123'))
####################################
pat=r'(a+)(b+)(c+)'
m=re.match(pat,'abbcccee')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
# for x in range(m.lastindex+1):
#     print(x,' {}'.format(m.group(x)))

# print(m.group(0))
# print(m.groups()) #start=1
# # print(m.groupdict())
# print(m.start(0),m.end(0))
# print(m.start(1),m.end(1))
# print(m.span(0))
# print(m.span(1))
# print(m.lastindex)
####################################
# m=re.search(r'\d{2,}','1 set of 23 owls , 999 doves')
# print(m.group(0),m.span())
# print(m.group(),m.span())
# # print(m.groups(),m.span()) #start 1

# m=re.findall(r'\d{2,}','1 set of 23 owls , 999 doves check 99 32 233')
# print(m)

# s='1 set of 23 owls, 999 doves. 9 2 3'
# # m=re.search(r'\d+',s)
# # print(m.group())
# m=re.findall(r'\d+',s)
# print(m)

####################################
# s='what is 1,000.5 times 3 2,000?'
# print(re.findall(r'\d[0-9,.]*',s))

####################################
# s='I do not use sophisticated multisyllabic words!'
# print(re.findall(r'\w{6,}',s))

####################################
# s='12 15+3 100 - *'
# print(re.findall('[+*/-]|\w+',s))

####################################
# pat=r'\d{1,3}(,\d{3})*(\.\d*)?'
# pat=r'(\d{1,3}(,\d{3})*(\.\d*)?)'
# print(re.search(pat,'12,000 monkeys and 55.5 cats.'))
# print(re.search(pat,'12,000 monkeys and 55.5 cats.').lastindex)
# print(re.search(pat,'12,000 monkeys and 55.5 cats.').group(0))
# print(re.search(pat,'12,000 monkeys and 55.5 cats.').group(1))
# print(re.findall(pat,'12,000 monkeys and 55.5 cats.'))

####################################
# pat=r'(\w+) \1'
# # m=re.search(pat,'pattern found the the ok found')
# # m=re.search(pat,'pattern found the The ok found')
# m=re.search(pat,'pattern found the The ok found',re.I)
# print(m.group(0),m.span(0))
####################################
# s='Get me a new dog to befriend my dog.'
# s2=re.sub('dog','cat',s)
# print(s2)

# s='The the cow jumped over over the moon.'
# s2 = re.sub(r'(\w+) \1', r'\1', s, flags=re.I)
# print(s2)

####################################
# pat=r'\d{1,3}(?:,\d{3})*(?:\.\d*)?'
# print(re.findall(pat,'12,000 monkeys and 55.5 cats.'))

####################################
# the_line = '<h1>This is an HTML heading.</h1>'
# # pat=r'<.*>'
# pat=r'<.*?>'
# print(re.findall(pat,the_line))

####################################
# s = r'''<h1>This is the first heading.</h1>
# <h1>This is the second heading.</h1>
# <b>This is in bold.</b>'''
#
# # pat=r'<.*?>'
# pat=r'<.*>'
# # lst=re.findall(pat,s)
# lst=re.findall(pat,s,re.DOTALL)
# print(len(lst),lst,sep='\n')

####################################
# s = '''Here is a single sentence.Here is
# another sentence, ending in a period.And
# here is yet another.'''
# # pat=r'.*?[.?!]'  #what if 'here is 23.23 hey'
# pat=r'[A-Z].*?[.!?](?=[A-Z]|$)'
# print(re.findall(pat,s,re.DOTALL|re.MULTILINE))
# print(len(re.findall(pat,s,re.DOTALL|re.MULTILINE)))
####################################
# s='''See the U.S.A. today. It's right here, not'''
# pat=r'[A-Z].*?[.!?] [A-Z]|$'
# m=re.findall(pat,s,flags=re.DOTALL)

####################################
# pat1=r'(\w|[!@#$%^&*+-]){8,12}$'
# pat2=r'(?=.*[a-zA-Z])'
# pat3=r'(?=.*\d)'
# pat4=r'(?=.*[!@#$%^&*+-])'
# pat=pat4+pat3+pat2+pat1
# print(pat)
# passwd='HenryThe5!'
# if re.match(pat,passwd):
#     print('Success')
# else:
#     print('Failed')
####################################
# # pat=r'abc(?=abc)'
# pat=r'abc(?!abc)'
# # pat=r'(?=abc)abc'
# # s = 'The abc magic abc of abcabc.'
# s = 'The abcabc magic abc of abcabc.'
# print(re.findall(pat,s))

# pat = r'abc(?!abc)'
# s = 'The magic of abcABC.'
# m = re.findall(pat, s, flags=re.I)
# print(m)

####################################
# pat = r'[A-Z].*?[.!?](?! [a-z]|\w)'
# s = '''See the U.S.A. today. It's right here, not
# a world away. Average temp. is 70.5. It's fun!'''
# m = re.findall(pat, s, flags=re.DOTALL)
#
# for i in m:
#     print('->', i)

####################################
# pat=r'(?P<first>\w+) (?P<last>\w+)' #Capital P
# s='vishnu kumar'
# match=re.match(pat,s)
# # print(bool(re.match(pat,s)))
# # print(match.group('first'))
# # print(match.group('last'))
# print('Last :{} First :{}'.format(match.group('last'),match.group('first')))

####################################
# pat=r'(?P<first>\w+) (?P<mid>\w\. )?(?P<last>\w+)' #Capital P #watch out for spaces
# name1='vishnu k. prajapat'
# name2='vishnu prajapat'
# reg=re.compile(pat)
# match1=reg.match(name1)
# match2=reg.match(name2)
# print(match1.group('first'))
# print(match1.group('mid'))
# print(match1.group('last'))
# print('-'*50)
# print(match2.group('first'))
# print(match2.group('mid'))
# print(match2.group('last'))

####################################
# pat = r'(?P<word>\w+) (?P=word)'
# m = re.findall(pat, 'The the dog.', flags=re.I)
# print(m)

####################################
# # pat=r'(, *)|( +)'
# pat=r', *| +'
# lst=re.split(pat,'3, 5  7  8,10,  11')
# print(lst)
####################################
# pat=r', *| +'
# s = '3 2 * 2 15 * + 4 +'
# lst=re.split(pat,s)
# print(lst)
####################################
# def sc_oper(scanner,tok):return  tok
# def sc_int(scanner,tok):return  int(tok)
# def sc_float(scanner,tok):return  float(tok)
#
# scanner=re.Scanner([
#     (r'[*+/-]',sc_oper),
#     (r'\d+\.\d*',sc_float),
#     (r'\d+',sc_int),
#      (r'\s+',None)]
# )
#
# print(scanner.scan('3 2. 2.5 0.5  3+'))
# print(scanner.scan('32 6.67+ 10 5- *'))
####################################
# the_stk=[]
# scanner=re.Scanner([
#     (r'[+*/-]',lambda s,t:bin_op(t)),
#     (r'\d+\.\d*',lambda s,t:the_stk.append(float(t))),
#     (r'\d+',lambda s,t:the_stk.append(int(t))),
#     (r'\s+',None)
# ])
#
# def bin_op(tok):
#     op2,op1=the_stk.pop(),the_stk.pop()
#     the_stk.append(eval(str(op2)+tok+str(op1)))
#
# def main():
#     input_str=input('Enter the RPN string :')
#     tokens,unknown=scanner.scan(input_str)
#     print(tokens)
#     print(unknown)
#     if unknown:
#         print('Unrecognized input :',unknown)
#     else:
#         print('Answer is ',the_stk.pop())
# main()
####################################
import operator

the_stk=[]
scanner=re.Scanner([
    (r'[+]',lambda s,t:bin_op(operator.add)),
    (r'[-]',lambda s,t:bin_op(operator.sub)),
    (r'[*]',lambda s,t:bin_op(operator.mul)),
    (r'[/]',lambda s,t:bin_op(operator.truediv)),
    (r'\d+\.\d*',lambda s,t:the_stk.append(float(t))),
    (r'\d+',lambda s,t:the_stk.append(int(t))),
    (r'\s+',None)
])

def bin_op(func):
    the_stk.append(func(the_stk.pop(),the_stk.pop()))

def main():
    input_str=input('Enter the RPN string :')
    tokens,unknown=scanner.scan(input_str)
    print(tokens)
    print(unknown)
    if unknown:
        print('Unrecognized input :',unknown)
    else:
        print('Answer is ',the_stk.pop())
main()
####################################
####################################
####################################
####################################