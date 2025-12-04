#item catalog(i know i didnt nered the numbers but it look better since they are also id numbers)
print('----------------------------------------------------')
print('                    PRODUCT CATALOG')
print('----------------------------------------------------')
print (' Itme_ID# [           Item Name              ]  item ')
print ('                                              price')
print ('---------------------------------------------------')
print ('|1.       |  USB Drive (128 GB)                | $12.00')
print ('|2.       |  Mac Book Pro (15 Inch)            | $2900.00')
print ('|3.       |  Arduino1010 (with BlueTooth)      | $48.00')
print ('|4.       |  Ring Camera(wireless)             | $156.00')
print ('|5.       |  Smart TV(TCL 70 inch)             | $359.00')
def shopingcart():

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
                "Product_name":"USB Drive (128 GB)",
                "Short_name":"USB",
                "Product_ID":1,
                "SKU": "usb_k981",
                "Price": 12.00,
                "Description": "usb 128 gb drive",
                "Qty_on_hand":1000,
            },
            { 
                "Product_name":"Mac_Boo_pro_15_inch",
                "Short_name":"MAC",
                "Product_ID":2,
                "SKU": "mbpro_490",
                "Price":2900.00,
                "Description": "Mac Book Pro 15 inch.",
                "Qty_on_hand":45,
    
            },
            {
                "Product_name":"Arduino_1010_with_blue_tooth",
                "Short_name":"ARDUINO",
                "Product_ID":3,
                "SKU": "chip_1010",
                "Price":48.00,
                "Description": "Arduino microprocessor",
                "Qty_on_hand":325,
            },
            { 
                "Product_name":"ring Camera (wireless)",
                "Short_name":"RING",
                "Product_ID":4,
                "SKU": "cam_78",
                "Price":156.00,
                "Description": "Ring Camera. Model 78.",
                "Qty_on_hand":98,
            },
            {
                "Product_name":"Smart_TV_TCL_70_inch",
                "Short_name":"SMART",
                "Product_ID":5,
                "SKU": "smt_tv_100",
                "Price":359.00,
                "Description": "TCL Smart TV",
                "Qty_on_hand":225,
            }
        ]

    #for key,value in products.items():
        #if Answer==product_ID print 
        done = True
        while done:
            ANSWER= int(input("Choose a product ID from the product catalog to continue:(choose and ID#) "))
            for items in products:
                if(items["Product_ID"]==ANSWER):
                    print(items)

       #print(items)
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
                contue=input("Would you like to add another item? (y or n) ")
                if contue=="n": 
                    done=False
        cart_total=0
        for items in products:
            if items["Short_name"] in shopingcart and products:
                quanity=shopingcart[items["Short_name"]]
                total= quanity * items["Price"]
                cart_total+=total
        print(f'your total is ${cart_total} please input the following information. ')
        First_name=input("what is your first name? ")
        Last_Name=input("what is your last name? ")
        Address=input("what is your address? ")
        city=input("what is your city name? ")
        state=input("what is your states name? ")
        ZIP=input("what is your ZIP code? ")
        Email=input("what is your Email? ")
        Phone=input("what is your Phone number? ")

        ccNum=input('Ok. Thank you. What is your Credit Card Number?  ')
        #this revers the string to do go to the end 
        CCNUM=ccNum[::-1]
        #this turns my credit number into values
        digits = [int(num) for num in CCNUM if num.isdigit()]
        total=0
        #for loop
        for i, num1 in enumerate(digits):
            #if statments to double the even numbers
                if i % 2 == 1:
                    N=num1*2
                    n=int(N)
                    #if the numbers are to big they will be -9
                    if n>9:
                        n-=9
                #this adds everything together 
                else:
                    n=num1
                total+= n
        #prints total
    #print stantment with if and else
        if total %10==0:
            print("credit card number is valid")
        else:
            print("credit card number not valid")


    




    
shopingcart()
#i want to add a while loop so i can tell it done when the user is down shoping (Done)
#i want to add mod 10 check (Done)
#i want to add a calculator to calculate price (Done) 
#I want to add mailing addres inputs (Done)
#qty can exceed stock()
#add a while loop for Mod 10 check()
#add duplication for or a way to check out after saying no()

        