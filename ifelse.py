#a = 13
a = 6
if a>10:
    print("i will do task a")
else:
    print("i will do task b") 


    #example 2
money = int(input("Please provide the money : "))
if money == 10 :
    print("I will buy an ice cream")
else:
    print("i'll buy a mango dolly")

#example 3 (use of elif)

pocketMoney = int(input("Please provide the pocket money : "))
if pocketMoney < 10 :
    print("I will buy an ice cream")
elif pocketMoney < 20:
    print("i will buy an mangdolly")
else:
    print("I will buy an cone")