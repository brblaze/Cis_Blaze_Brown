# start and end statment to find the locational value 
start=int(input('where do you want to start (0-3) '))
end= int(input('where do you want to end (0-3) '))
def slice_my_string():
    numbers=["1","2","3","4"]
   #list statement 
    mylist=(numbers[start: end])
    print(mylist)
    #return the list
    return mylist
slice_my_string()