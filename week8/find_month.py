def search():
    months=["january","feburary", "march", "April", "May", "June","July", "August", "september", "October","November", "December" ]
    #search statment
    search= input('what month are you looking for? ')
    if (search) in months:
        print (f'we fond {search} in the months list. Search successful!. ')
    else:
        print (f'We could not find {search} in the months list.' )
search()
