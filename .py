# *** QUESTION-1 *** #
productnum = eval(input("Enter the number of your products: "))
my_dict={}
count=0
for i in range (productnum):
  productname = input("Enter the name of your product: ")
  productprice = eval(input("Enter the price of your product: "))
  my_dict[productname]=productprice
#now to get the price from the dictionary
while True:
  productname = input("Enter the name of your product to get the price: ")
  if productname in my_dict:
    print("the price of your product is: ", my_dict[productname], "$")
    count+=1
    if count==productnum:
      break
  else:
    print("invalid product")
     
     <----------------------------->
    
 # *** QUESTION-2 *** #
productnum = eval(input("Enter the number of your products: "))
my_dict={}
for i in range (productnum):
  productname = input("Enter the name of your product: ")
  productprice = eval(input("Enter the price of your product: "))
  my_dict[productname]=productprice
amount = eval(input("Enter The Dollar Amount: "))
for key, values in my_dict.items():
  if int(values)<amount:
    print("Product less than the entered amount is= ", key,"-", values, "$")
    
    <--------------------------------------->
  
  # *** QUESTION-3***
# part a
days = {'January':31, 'February':28, 'March':31, 'April':30,
'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30, 'December':31}
month_name = input("Enter the month name: ")
print("Number of days in the month are: ", days[month_name])
# part b
sorted_year ={key:days[key] for key in sorted(days)}
print(sorted_year.keys())
# part c
for keys, values in days.items():
  if int(values) == 31:
    print(keys)
# part d

<------------------------------------------->

# *** Question- 4 *** #
data = {"leena91": "hys668", "starboy6": 665802, "nousername": "no username",
        "anonymous": 123098, "deadname": "bnhyuijk9", "coolboi56": 78210, 
        "gamergirl101": "koolit94", "zuza317" : 5555877,
        "dababy._." : "null", "firehouse" : "idkmate10"}
username=input("Please Enter your username: ")
if username not in data:
  print("invalid user")
elif username in data: 
   password=input("Enter your password: ")
   if username in data and data[username]==password:
     print("You are logged in")
   if username in data and data[username]!=password:
     print("Wrong password")
     
   <-------------------------------------------->
   
   # *** QUESTION - 6 *** #
team_num = int(input("Enter the number of teams: "))
team_dict={}
wins = 0
loses = 0
for i in range (team_num):
  team_name = input("emter the name of your team: ")
  matches_won = int(input("Enter the matches won: "))
  matches_lost = int(input("enter the matches lost: "))
  wins+=1
  loses+=1
  team_dict[team_name]=matches_won, matches_lost
  print(team_dict)
     
   <-------------------------------------->
   
   
 # ***** QUESTION -7 **** #
matrix_5= [1,2,3,4,5,
           5,6,7,4,5,
           6,7,8,0,3,
           4,2,1,5,6,
           7,8,9,0,5]
matrix_dict={}
for num in range(len(matrix_5)):
        key = matrix_5[num]
        value = matrix_5.count(key)
        matrix_dict.update({key:value})
print(matrix_dict)
     
     <-------------------------------------------->
  
# **** QUESTION - 8 *** #
import random

cards_total ={"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10}
cards = 3
player1Card =[]
player2Card =[]
for card in range(cards):
    c1 =random.choice(list(cards_total.values()))
    c2= random.choice(list(cards_total.values()))
    player1Card.append(c1)
    player2Card.append(c2)
print(player1Card,player2Card)

if sum(player1Card) > sum(player2Card):
    print("Player 1 wins with ",sum(player1Card)," Against Player 2 with",sum(player2Card))
elif sum(player2Card) > sum(player1Card):
    print("Player 2 wins with ",sum(player2Card)," Against Player 1 with",sum(player1Card))
  
  <---------------------------------------->
  
  # **** QUESTION - 14 **** #
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
for dict  in  range(len(d)):
     data =d[dict ]
     for keys,values in data.items():
         if keys == "phone" and values[-1] == "8":
             print(data)
         if keys == "email" and values =='':
            print(data)
  
  
  
  
  
  
  
  
  
  
  
  








