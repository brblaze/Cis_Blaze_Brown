numberofgrades= int(input('How many grades do you want to grade ' ))

n=0
print (f"{numberofgrades}")
#while loop
while n < numberofgrades:
 n=n+1
 grades=int(input('enter this grade for this assiment '))
 print (f'{grades}')
 if n<= numberofgrades:
  print ('You are done grading')