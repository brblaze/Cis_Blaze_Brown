#item catalog(i know i didnt nered the numbers but it look better since they are also id numbers)
print('----------------------------------------------------')
print('                    PRODUCT CATALOG')
print('----------------------------------------------------')
print (' Itme_ID# [           Item Name              ]  item ')
print ('                                              price')
print ('---------------------------------------------------')
print ('|1.       |  USB Drive (128 GB)                | $12.00')
print ('|2.       |  Mas Book Pro (15 Inch)            | $12.00')
print ('|3.       |  Arduino1010(with blue tooth)      | $12.00')
print ('|4.       |  Ring Camera(wireless)             | $12.00')
print ('|5.       |  Smart TV(TLC 70 inch)             | $12.00')
def shopingcart():
    ANSWER= int(input("Choose a product ID from the product catalog to continue:(choose and ID#) "))
    shopingcart={
        "USB":0,
        "MAC":0,
        "ARDUINO":0,
        "RING":0,
        "SMART":0,
    }

#dictinarey with the details of a product
    products=[
        {
            "product name":"USB Drive (128 GB)",
            "product_ID":1,
            "SKU": "usb_k981",
            "price": 12.00,
            "description": "usb 128 gb drive",
            "qty on hand":1000,
        },
        { 
            "product name":"Mac_Boo_pro_15_inch",
            "product_ID":2,
            "SKU": "mbpro_490",
            "price":2900.00,
            "description": "Mac Book Pro 15 inch.",
            "qty on hand":45,
    
        },
        {
            "product name":"Arduino_1010_with_blue_tooth",
            "product_ID":3,
            "SKU": "chip_1010",
            "price":48.00,
            "description": "Arduino microprocessor",
            "qty on hand":325,
        },
        { 
            "product name":"ring Camera (wireless)",
            "product_ID":4,
            "SKU": "cam_78",
            "price":156.00,
            "description": "Ring Camera. Model 78.",
            "qty on hand":98,
        },
        {
            "product name":"Smart_TV_TCL_70_inch",
            "product_ID":5,
            "SKU": "smt_tv_100",
            "price":359.00,
            "description": "TCL Smart TV",
            "qty on hand":225,
        }
    ]

    for key,value in products[0].items():
        #if Answer==product_ID print 
       print(key)
       print(value)
    print(shopingcart)

    answer=input("Do you want to add it to your cart? (y or no) ")


    if answer=='y':
        if ANSWER==1:
            quanity=int(input("how many do you want? (qty 1000) "))
            shopingcart["USB"] += quanity
        elif ANSWER==2:
            quanity=int(input('how many do you want? (qty 45) '))
            shopingcart["MAC"] += quanity
        elif ANSWER==3:
            quanity=int(input('how many do you want? (qty 325) '))
            shopingcart["ARDUINO"] += quanity
        elif ANSWER==4:
           quanity=int(input('how many do you want? (qty 98) '))
           shopingcart["RING"] += quanity
        elif ANSWER==5:
            quanity=int(input('how many do you want? (qty 225) '))
            shopingcart["SMART"] += quanity
        else:
            print("try again")
        print(shopingcart)
    
shopingcart()
#i want to add a while loop so i can tell it done when the user is down shoping ()
#i want to add mod 10 check ()
#i want to add a calculator to calculate price () 
#I want to add mailing addres inputs ()

        