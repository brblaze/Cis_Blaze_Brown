import math
base= input('what is the base of the triangle ')
hight= input('what is the Hight of the triangle ')
truebase= int(base)**2
Truehight=int(hight)**2
add=int(truebase)+int(Truehight)
hypoteneuse=math.sqrt(add)
print(f'{hypoteneuse}')
