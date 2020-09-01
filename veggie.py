class cust:
    def customer():
        shop={'vegetable bill':{'onion':23,'tomato':43,'carrot':20,'brinjal':15}}
        for topic,info in shop.items():
            print("The vegetables available are:")
            print("====================")
            for key in info:
                print(key+':',info[key])
            print("===================")
        def products_bought(p1,p2):
            print("***The total amount to be paid is:{}***".format((shop['vegetable bill'][p1])*q1+(shop['vegetable bill'][p2])*q2))
            print("=====THANK YOU=====")
        print("vegetable bill")

        p1=str(input("1."))
        q1=int(input("quantity of p1="))
        p2=str(input("2."))
        q2=int(input("quantity of p2="))
        products_bought(p1,p2)
    customer()
    
        
