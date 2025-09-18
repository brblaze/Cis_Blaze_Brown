num1= int(input('what number do you want to loop to ' ))

n=0
print (f"{num1}")
#while loop
while n <=100:
 n=n+1
 num1= int(input('pick another number '))
 print (f'{num1}')
 if num1>=101:
  print('Sorry, the number you entered is out of range')


