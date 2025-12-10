#item catalog(i know i didnt need the numbers but it look better since they are also id numbers)
print('----------------------------------------------------')
print('                    PRODUCT CATALOG')
print('----------------------------------------------------')
print (' Item_ID# [           Item Name              ]  item ')
print ('                                              price')
print ('---------------------------------------------------')
print ('|1.       |  USB Drive (128 GB)                | $12.00')
print ('|2.       |  Mac Book Pro (15 Inch)            | $2900.00')
print ('|3.       |  Arduino1010 (with BlueTooth)      | $48.00')
print ('|4.       |  Ring Camera(wireless)             | $156.00')
print ('|5.       |  Smart TV(TCL 70 inch)             | $359.00')

#defined function 
def shopingcart():

#shopping Cart 
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
        #while loop to see if you want to shop or not
    done=True
    Checkin=input('do you want to add an item in your cart (y or n)? ')
    if Checkin =='y': 
        while done:
            if Checkin=="y":
                ANSWER= int(input("Choose a product ID from the product catalog to continue:(choose and ID#) "))
                for items in products:
                    #answer is important because i use is to keep the product id
                    if(items["Product_ID"]==ANSWER):
                        #this print only one dictionary
                        print(items)


               #print(items)
                print(shopingcart)
                answer=input("Do you want to add it to your cart? (y or n) ")

                #in this if statment there are while loops to make sure we pick the range 
                if answer=='y':
                    if ANSWER==1:
                        DONE=True
                        while DONE:
                            quantity=int(input("how many do you want? (qty 1000) "))
                            if quantity in range (1,1001):
                                shopingcart["USB"] += quantity
                                DONE=False
                            else:
                                print("invalid qautiity. Sorry we do not have that many items on hand. Please enter a valid quantity. ")
                    elif ANSWER==2:
                        DONE=True
                        while DONE:
                            quantity=int(input("how many do you want? (qty 45) "))
                            #here
                            if quantity in range (1,46):
                                shopingcart["MAC"] += quantity
                                DONE=False
                            else:
                                print("invalid qautiity. Sorry we do not have that many items on hand. Please enter a valid quantity. ")
                    elif ANSWER==3:
                        DONE=True
                        while DONE:
                            quantity=int(input("how many do you want? (qty 325) "))
                            if quantity in range (1,326):
                                shopingcart["ARDUINO"] += quantity
                                DONE=False
                            else:
                                print("invalid qautiity. Sorry we do not have that many items on hand. Please enter a valid quantity. ")
                    elif ANSWER==4:
                        DONE=True
                        while DONE:
                            quantity=int(input("how many do you want? (qty 98) "))
                            if quantity in range (1,99):
                                shopingcart["RING"] += quantity
                                DONE=False
                            else:
                                print("invalid qautiity. Sorry we do not have that many items on hand. Please enter a valid quantity. ")
                    elif ANSWER==5:
                        DONE=True
                        while DONE:
                            quantity=int(input("how many do you want? (qty 225) "))
                            if quantity in range (1,226):
                                shopingcart["SMART"] += quantity
                                DONE=False
                            else:
                                print("invalid qautiity. Sorry we do not have that many items on hand. Please enter a valid quantity. ")
                    else:
                        print("try again")

                    #these if statment allow the user to pick another product
                    print(shopingcart)
                    additon=input("Would you like to add another item? (y or n) ")
                    if additon=="n":
                        done=False
                    if additon=='y':
                        continue
                else:
                    answer =='n'
                    CHECKOUT=input('do you want to check out? (y or n)? ')
                    if CHECKOUT=='y':
                        done=False
                    else:
                        continue

        #this inital values the cart to start at 0
    cart_total=0
        #this for loop add the total price but also changes my shopping cart to a list
    for items in products:
        if items["Short_name"] in shopingcart and products:
            quantity=shopingcart[items["Short_name"]]
            total= quantity * items["Price"]
            cart_total+=total
        #basic information
    print(f'your total is ${cart_total} please input the following information. ')
    First_name=input("what is your first name? ")
    Last_Name=input("what is your last name? ")
    Address=input("what is your address? ")
    city=input("what is your city name? ")
    state=input("what is your states name? ")
    ZIP=input("what is your ZIP code? ")
    Email=input("what is your Email? ")
    Phone=input("what is your Phone number? ")
    print("thank you")
    DOME=True
    while DOME:
        ccNum=input(' What is your Credit Card Number?  ')
        #this revers the string to do go to the end
        CCNUM=ccNum[::-1]
        #this turns my credit number into values
        digits = [int(num) for num in CCNUM]
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
            DOME=False
            print("credit card number is valid.")
        else:
           print("credit card number not valid.  Try again please. ")
       
    valid_date=input("Enter the expiration date on your card: ")
    cvv=input("Please enter your CVV:")
    #invoice message
    print("-------------------------------------------------------------------------------------------------------------------")
    print('                                            Billing/shipping infomration:')
    print("-------------------------------------------------------------------------------------------------------------------")
    print(' ')
    print(f"Name: {First_name} {Last_Name}")
    print (f"Address: {Address}")
    print (f"City: {city}")
    print(f"State: {state}")
    print(f"ZIP code: {ZIP}")
    print(f'Email: {Email}')
    print(f"Phone number: {Phone}")
    print('')
    print("-------------------------------------------------------------------------------------------------------------------")
    print('                                           Shopping Cart Information')
    print("-------------------------------------------------------------------------------------------------------------------")
    print('')
    print(f'[SKU]                     quantity          Price           Description                  Total       ')
    print('*******************************************************************************************************************')
    for items in products:
        NAME=items["Short_name"]
        if shopingcart[NAME] >0:
            qty=shopingcart[NAME]
            price=items["Price"]
            TOTAL=qty*price
            print(f"{items['SKU']:10}          {qty:10}        {price:10.2f}       {items['Description']:25}      {TOTAL:10.2f}")
    print(cart_total)

    if Checkin =='n':
        print('ok have a good day. ')

#10 chareters long

shopingcart()
#i want to add a while loop so i can tell it done when the user is down shoping (Done)
#i want to add mod 10 check (Done)
#i want to add a calculator to calculate price (Done)
#I want to add mailing addres inputs (Done)
#qty can exceed stock(Done)
#add a while loop for Mod 10 check(Done)
#Check out(done)
# prompt user for CVV (DONE)
#fix credit card(DONE)
#reccetinformation()
#if say no in first prompt(done)
#for ""choose id not correct value bricks code(NO)
#error if enter credit dard number as a lettrer(NO)
#when asking for value for quanity and nothing is enter(NO)