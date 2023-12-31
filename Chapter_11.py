import random

# def do_trails(n):
#     hits=[0]*10
#     for i in range(n):
#         a=random.randint(0,9)
#         hits[a]+=1
#
#     for i in range(10):
#         fss='{}: {}\t {:.3}'
#         print(fss.format(i,hits[i],hits[i]/(n/10)))
#
# do_trails(100)

#########################################################
# def play_game():
#     n = random.randint(1, 50)
#     while True:
#         guess=int(input('Enter Guess :'))
#         if guess==0:
#             print('Exiting the game.')
#             break
#         if guess==n:
#             print('Success ! you win.')
#             break
#         elif guess<n:
#             print('Too low.')
#         else:
#             print('Too high.')
#
# while True:
#     play_game()
#     ans=input('Play again (Y or N):')
#     if not ans or ans in 'Nn':
#         break


#########################################################
# kings_list = ['John', 'James', 'Henry', 'Henry', 'George']
# print(random.shuffle(kings_list))
# print(kings_list)

#########################################################
# ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# suits = ['clubs', 'diamonds', 'hearts', 'spades']  # only for class
# class Deck():
#     def __init__(self,size):
#         self.card_list=[i for i in range(size)]
#         random.shuffle(self.card_list)
#         self.current_card=0
#         self.size=size
#
#     def deal(self):
#         if self.size-self.current_card<1:
#             random.shuffle(self.card_list)
#             self.current_card=0
#             print('Reshufling...!!!')
#         self.current_card+=1
#         return self.card_list[self.current_card-1]
#
# my_deck=Deck(52)
# for i in range(13):
#     for i in range(4):
#         d=my_deck.deal()
#         r=d%13
#         s=d//13
#         print(ranks[r],' of ',suits[s])
#     print()

#########################################################
# ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# suits = ['clubs', 'diamonds', 'hearts', 'spades']  # only for class
# class Deck():
#     def __init__(self,size):
#         self.card_list=[i for i in range(size)]
#         self.card_in_play_list=[]
#         self.discard_list=[]
#         random.shuffle(self.card_list)
#
#     def deal(self):
#         if len(self.card_list)<1:
#             random.shuffle(self.discard_list)
#             self.card_list=self.discard_list
#             self.discard_list=[]
#             print('Reshuffling...!!!')
#         new_card=self.card_list.pop()
#         self.card_in_play_list.append(new_card)
#         return new_card
#
#     def new_hand(self):
#         self.discard_list+=self.card_in_play_list
#         self.card_in_play_list.clear()
# my_deck=Deck(52)
# for i in range(13):
#     for i in range(4):
#         d=my_deck.deal()
#         r=d%13
#         s=d//13
#         print(ranks[r],' of ',suits[s])
#     print()

#########################################################
# class Deck():
#     def __init__(self,n_deck=1):
#         self.no_of_deck=n_deck
#         self.card_list=[[num+suit for suit in '\u2665\u2666\u2663\u2660'
#             for num in 'A23456789TJQK']
#                 for deck in range(n_deck)]
#         self.card_in_play_list=[]
#         self.discard_list=[]
#         for i in range(self.no_of_deck):
#             random.shuffle(self.card_list[i])
#
#     def show(self):
#         for x in range(self.no_of_deck):
#             for i in range(52):
#                 print(self.card_list[x][i],end=' ',sep='\t')
#                 if (i+1)%13==0:
#                     print()
#             print('-'*40)
#
# x=Deck(3)
# x.show()

#########################################################
def pr_normal_char(n):
    hits=[0]*20
    for i in range(n):
        x=random.normalvariate(100,30)
        j=int(x/10)
        if 0<=j<20:
            hits[j]+=1

    for i in hits:
        print('*'*int(i*320/n))

pr_normal_char(30)
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################