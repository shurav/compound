import math
def compound(A, principal, rate, numCompounds):
    years = (math.log(A/principal,1+rate/numCompounds))/numCompounds
    return years
item = input("What you want to buy? ")
money = float(input("How much is it? "))
p = float(input("How much can you afford to pay for the " + item + "? "))
if(p >= money):
    print("You could afford it and there is no need to invest money in a bank account")
else:
    print("You need to invest money in your bank account")
    r = float(input("At what rate do you want to invest it? (Enter as a percentage) "))
    n = int(input("How many times do you want to compound it? "))
    t = compound(money, p, (r/100), n)
    print("It would take " + str(t) + " years for you to afford the " + item)
