watchlist= []
symbol= input("Please type in the tickers of the stocks you want on your watchlist:")
if symbol != '':
    while symbol != '':
        watchlist.append(symbol)
        symbol= input("If you would like to input another ticker, please do so. Otherwise, hit enter:")

else:
    print("You did not enter a ticker")

def convert2str(watchlist):
    watchliststr = " "
    return (watchliststr.join(watchlist))
watchliststr = convert2str(watchlist)

def removePunctuation(watchliststr):
    punctuation = '.,:;!?@#$%^&*()'
    for mark in punctuation:
        watchliststr =watchliststr.replace(mark,'')
    symbols=watchliststr.lower().strip().split()
    return symbols
watchlist2= removePunctuation(watchliststr)

def convert2str(watchlist2):
    watchliststr2= ''
    return (watchliststr2.join(watchlist2))
watchliststr2 = convert2str(watchlist2)


watchlistfinal=[]
for i in watchliststr2:
    if i not in watchlistfinal:
        watchlistfinal.append(i)
watchlistfinal=sorted(watchlistfinal)
print("Watchlist =",watchlistfinal)


Uinput=input("Type something here and I will replace the vowels with numbers: ")
def numberize(Uinput):
    vowels= 'aeiou'
    numbers= ['1','2','3','4','5']
    i=0
    for k in range(len(Uinput)):
        while i <=4:
            for k in vowels[i]:
                Uinput= Uinput.replace(k, numbers[i])
            i+=1
    numberstr= Uinput.lower().strip().split()
    return numberstr
numbervowel= numberize(Uinput)

numberstr= ' '
(numberstr.join(numbervowel))
numberstr=convert2str(numbervowel)
print(numberstr)

def anagramcheck():
    words1= input("type your first phrase here:")
    words2= input("type your second phrase here:")
    punctuation= '.,:;!?@#$%^&*()'
    for character in punctuation:
        words1= words1.replace(character,'')
        words2= words2.replace(character,'')
        words1= words1.lower()
        words2= words2.lower()
    anagramBool = True
    for letter in words2:
        if letter not in words1:
            anagramBool = False
    return(anagramBool)
    print(words1)
    print(words2)
    print(anagramBool)
anagramOutcome = anagramcheck()
print("The outcome is:", anagramOutcome)

