import math
#base= input('what is the base of the triangle ')
#hight= input('what is the Hight of the triangle ')
#truebase= int(base)**2
#Truehight=int(hight)**2
#add=int(truebase)+int(Truehight)
#hypoteneuse=math.sqrt(add)
#print(f'{hypoteneuse}')

def message1():
    x = input ('please enter the value of the base ')
    y = input ('please enter the value of the hight')
    c= int(x)**2+int(y)**2
    hypo= math.sqrt(c)
    print(f'{hypo}')
message1 ()
