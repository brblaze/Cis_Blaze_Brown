#first two lines is my start and edd statment 
start=int (input('Enter the numberfor your first month '))
end=int (input('Enter the number for your last month '))
def months_of_years():
    #list of montrhs 
    months= ["january","feburary", "march", "April", "May", "June","July", "August", "september", "October","November", "December" ]
    #print statment 
    print(f'{months[start: end]}')
months_of_years()