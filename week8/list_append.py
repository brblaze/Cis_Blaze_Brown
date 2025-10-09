#initnal value 
num1=input('enter an initial value ')
def append_to_llist(num1):
    Mylist=[]
    #add the initial vaue
    Mylist.append(num1)
    #done helps is keeps organize
    done=True
    while done:
        answer=input('Would you like to enter another value to append to the list? (y or n) ')
        if answer== 'y':
            Mylist.append(input('what number do you want to add? '))
#stopping statment
        else answer =='n':
            done=False 
            print(Mylist) 
append_to_llist(num1)