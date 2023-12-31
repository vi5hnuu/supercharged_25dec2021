# print(0.1+0.1+0.1)
# print(round(0.1+0.1+0.1,2))
# print(0.6+0.3+0.1)
# print((0.6+0.3+0.1)/2)
import decimal
from decimal import Decimal

# my_decimal=Decimal()
# print(my_decimal)
# my_decimal=Decimal(1.2359)
# print(my_decimal)
# my_decimal=Decimal('1.2359')
# print(my_decimal)

# print(0.1+0.1+0.1-0.3)

# d1,d3=Decimal('0.1'),Decimal('0.3')
# print(d1+d1+d1-d3)
#
# d1, d3 = Decimal('0.10'), Decimal('0.30')
# print(d1+d3)
#
# d1, d3 = Decimal('0.50'), Decimal('0.50')
# print(d1+d3)
# print(d1*d3)

# d=Decimal('15.700')
# print(d)
# d2=d.normalize()
# print(d2)
#
# d1=Decimal('15.000')
# print(d1)
# d3=d1.normalize()
# print(d3)
# print(d2==d3)
# print(d1==d3)


# d=Decimal('15.0')
# print(d.as_tuple()) # DecimalTuple(sign=0, digits=(1, 5, 0), exponent=-1)
#
# d2=Decimal((0,(1,5,0),-1))
# print(d2)

# print(decimal.getcontext())

####################################
# total=Decimal('0.00')
# while True:
#     s=input('Enter amount in dollars and cents #.## :')
#     if not s:
#         break
#     d=Decimal(s)
#     d=round(d,2)
#     total+=d
# print('The sum is {}'.format(total))

#####################################


class Money():
    default_curr='USD'
    exch_dict = {
        'USDCAD': Decimal('0.75'), 'USDEUR':
            Decimal('1.16'),
        'CADUSD': Decimal('1.33'), 'CADEUR':
            Decimal('1.54'),
        'EURUSD': Decimal('0.86'), 'EURCAD':
            Decimal('0.65')
    }
    def __init__(self,v='0',units=''):
        self.dec_amt=Decimal(v)
        if not units:
            self.units=Money.default_curr
        else:
            self.units=units

    def __str__(self):
        s=str(self.dec_amt)+' '+self.units
        return s

    def __repr__(self):
        s=('Money('+str(self.dec_amt)+' '+self.units+')')
        return s

    def __add__(self, other):
        if self.units != other.units:
            r=Money.exch_dict[self.units+other.units]
            m1=self.dec_amt
            m2=other.dec_amt*r
            m=Money(m1+m2,self.units)
        else:
            m=Money(self.dec_amt+other.dec_amt,self.units)
        m.dec_amt=round(m.dec_amt,2)
        return m
#
# m=Money('15.99')
# print(m)
# print(m.__str__())
# print(m.__repr__())

# us_m=Money('1','USD')
# ca_m=Money('1','CAD')
# print(us_m+ca_m)

#############using money class to build calculator
# def money_calc():
#     '''Money addition calculator.
#     Prompt for a series of Money objects until empty
#     string is entered; then print results of the
#     running total.
#     '''
#     n=0
#     while True:
#         s=input('Enter money value :')
#         s=s.strip()
#         if not s:
#             break
#         a_list=s.split()
#         d=a_list[0]
#         if (len(a_list)>1):
#             m=Money(d,a_list[1])
#         else: #money with default USD currency
#             m=Money(d)
#         if n==0:
#             amt=m
#             Money.default_curr=m.units
#         else:
#             amt+=m
#         n+=1
#     print('Total is ',amt)
#
# money_calc()

#####################################
from fractions import Fraction

# fr1=Fraction(1,2)
# fr2=Fraction(2,4)
# fr3=Fraction(100/200)
# if fr1==fr2==fr3:
#     print('They are all equal')
# print('The fractions are %s %s %s'%(fr1,fr2,fr3))

# fr1=Fraction(5)
# print(fr1)
#
# fr2=Fraction(0.5)
# print(fr2)
#
# fr2=Fraction(0.1)
# print(fr2)
#
# #sol1
# fr2=Fraction('0.1')
# print(fr2)
#
# #sol2
# fr2=Fraction(0.1).limit_denominator(1000)
# print(fr2)

# fr1=Fraction(1,2)
# fr2=Fraction(1,3)
# fr3=Fraction(5,12)
# print(fr1+fr2+fr3)

# fr1=Fraction(1,100)
# print(fr1,' times 50 ',fr1*50)

# fr1=Fraction('1/7')
# print(fr1)
#
# fr1+=Fraction('3/4')
# print(fr1)
# print(fr1.numerator)
# print(fr1.denominator)

#####################################
# total=Fraction('0')
# while True:
#     s=input('Enter fractions (Press enter to quit) :')
#     s=s.replace(' ','')
#     if not s:
#         break
#     total+=Fraction(s)
#
# print('The total is %s'%total)

#####################################
# # z = 2.5 + 1.0j
# z = complex(2.5,1.0)
# print(z.real,z.imag)
# print(z)
# print(type(z.imag))
# print(type(z.real))
# print(type(z))

#####################################