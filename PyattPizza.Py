class orders:
    orderlist = []
class Pizza:
    pizzassold =0


    def __init__(self,SizeP,priceP,toppingsP,customername,Customeraddress):

        self.size=SizeP
        self.price=priceP
        self.Toppings=toppingsP
        self.customername =customername
        self.customeraddress = Customeraddress


    def sellpizza(self):
        Pizza.pizzassold += 1
        orders.orderlist.append(Pizza)
    def computeavg(self):

         print(sum(Pizza.price)/orders.orderlist.count())

    def displayproduct(self):
        print(orders.orderlist[int()])



P1 = Pizza.sellpizza(large,30,pepperoni,Jake,123Norfsidelongbeach)
Pizza.displayproduct(1)
P2 = Pizza.sellpizza(small,20,bacon,leon,123anywherelane)
Pizza.displayproduct(2)
P3 = Pizza.sellpizza(medium ,25,everything,333Uptownblvd)
Pizza.displayproduct(3)

Pizza.computeavg()
