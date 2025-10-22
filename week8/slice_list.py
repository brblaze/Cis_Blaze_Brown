#months list
months=["january","feburary", "march", "April", "May", "June","July", "August", "september", "October","November", "December" ]
#start and end statement 
start=int(4)
end=int(6)
def slice_list(months):
     mylist=(months[start: end])
     print(mylist)
slice_list(months)