import random

money = 200


#flip a coin game
def flip_coin(coin,bet):

  if money<0:
      print('you dont have enough money to play')
      return 0
  
  if (bet<=0) or not (coin=="Heads" or coin=="Tails"):
    print("your parameter is wrong")
    return 0
  result = random.randint(1,2)
  
  if (result == 1) and (coin == "Heads"):
    print("You won "+str(bet)+" shekel, and you have in total "+str(money+bet)+" shekel")
    return bet
  
  elif (result == 2) and (coin == "Tails"):
      print("You won "+str(bet)+" shekel, and you have in total "+str(money+bet)+" shekel")
      return bet
  
  else:
        print("You lost "+str(bet)+" shekel, and you habve in total "+str(money-bet)+" shekel")
  return -bet


#cho_han game
def cho_han(bet,money2):
  
  #check parameters

  if money<0:

      print('you dont have enough money to play')
      return 0
  
  if (money2<=0) or not (bet=="Even" or bet=="Odd"):
    
    print("your parameter is wrong")
    return 0
  
  dice1=random.randint(1,6)
  print("first cube result is ",dice1)
  dice2=random.randint(1,6)
  print("first cube result is ",dice2)
  sum1=dice1+dice2
  print("the sum of the cube is ",sum1 )
  
  if (sum1%2==0 and bet=="Even") or (sum1%2!=0 and bet=="Even"):
    print("you bet that the result will be ",bet," number, and you right so you won  ",money2," shekel, and you have in total ", money+money2)
    return money2
  else:
     print("you bet that the result will be ",bet," number, and you wrong so you lost  ",money2," shekel, and you have in total ", money-money2)
     return -money2
  # basic example hot to use random, cards pack


def milchama(bet):

  if money<0:
      print('you dont have enough money to play')
      return 0

  cards_pack=[]
  
  for i in range(1,14):
    cards_pack.append(i)
  
  for i in range(1,14):
    cards_pack.append(i)

  card_1=random.choice(cards_pack)
  cards_pack.remove(card_1)
  print("The first player took ",card_1, )
  card_2=random.choice(cards_pack)
  cards_pack.remove(card_2)
  print("The seconed player took ",card_2)
  
  if (card_1>card_2):
    print("player 1 won ",bet)
    print("you have in total ",money+bet)
    return bet
  
  elif (card_1<card_2):
    print("player 2 won", bet)
    print("you have in total ",money-bet)
    return -bet
  
  else:
    print("it's a tie")
    print("you have in total ",money)
    return 0
    
def rouletta(bet,money2):

    # you can bet on: Odd/Even, Black,Red,number, 
    #37=00
    if money<0:
      print('you dont have enough money to play')
      return
      
    print("before the game you have", money, "shekel")
    num=random.randint(0,37) 
    black=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    red=[]
    #fill red num list
    for i in range(37):
      if (i not in black):
        red.append(i)
    
    if (money2 <= 0):
      print("you need to bet on a positive amount of money")
    
    if num==37:
      print("the result is 00")
    else:
      print("The result is ",num)

    #winnig check:
    if (bet=='Odd') and (num%2!=0):
      print("you bet on odd, and you right, you won", money2*2)
      return money2*2

    elif (bet=='Even') and (num%2==0):
      print("you bet on Even, and you right, you won", money2*2)
      return money2*2

    elif (bet=='Red') and (num in red):
      print("you bet on red and you won", money2*2)
      return money2*2

    elif (bet=='Black') and (num in black):
      print("you bet on black and you won", money2*2)
      return money2*2

    elif (bet==num):
      print("you bet on the right number!!, you won ",money2*35)
      return money2*35
    else:
      print("your bet is", bet, " didn't match, you lost the money you bet on")

      return -money2


money+=flip_coin("Heads",50)
money+=cho_han("Even",20)
money+=milchama(70)
money+=rouletta("Odd",40)
money+=rouletta("Even",100)
money+=rouletta("Red",50)
money+=rouletta(5,50)
print("you have ",money," shkel" )







