word= input('What word do you want to ues? ')
def revers(word):
    reverse = (word)[::-1]
    return reverse
if revers(f"{word}")==word:
    print(f'{word} is a paldrome, therefore is true')
else:
    print (f'{word} is not a paldrome, therefore is false ')