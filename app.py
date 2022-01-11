import json
from difflib import SequenceMatcher  #Ima 3 parametra(prvi je None (to je isjunk, ako poredim vise stringova, onda to prosledim da bih ignorisao prazna mesta i slicno), "rainn", "rain", ostala dva parametra su stringovi, koje poredim). Dodam na kraju metodu ratio() koja mi izbacuje njihovu slicnost
from difflib import get_close_matches  #Ima 4 parametra(prvi je uneta rec, drugi je lista slicnih reci, tipa ["help", "mount", "rain"], treci je koliko ce da izbaci slicnih reci ako ih ima, a cetvrti vraca samo one reci kojima je ratio(slicnost) 0.6 ili veca)

data = json.load(open("data.json", "r"))

def foo(query):
    #Ovo je moglo da se uradi i pomocu try/except block-a

    if query in data:
        return data[query]
    elif query.title() in data:
        return data[query.title()]
    elif query.upper() in data:
        return data[query.upper()]
    elif len(get_close_matches(query, data.keys())) > 0:  #Koristim ovu metodu i dodjeljujem joj nase ime i key data i koristim len da vidim da li ima nesto u listi
        yn =  input(f"Did you mean {get_close_matches(query, data.keys())[0]} instead?. Enter Y if yes, or N if no: ")  #Prosledjujem ovu metodu, da vidim da li je to ta rec. Stavim u input da bih mogao da izbacim nesto ako je yes tj. no
        #return f"Did you mean %s instead?" % (get_close_matches(query, data.keys()))[0]
        if yn == "Y":
            return data[get_close_matches(query, data.keys())[0]]  #Ako je yn=="Y" izbaci mi podatak za tu rec
        elif yn == "N":
            return "Sorry, we don't know what you mean!"
        else:
            return "We didn't understand your entry!"
    else:
        return "Try again! The word doesen't exist. Please double check it!"

word = input("Enter your word: ")
output = foo(query=word.lower())  #Napravio varijablu za smestaj nase f-je

#Pomocu if/else naredbe proveravam da li je output list, ako jeste idem for petlju kroz sve, da bih izbacio odgovore jedno ispod drugog, a ako je string, samo idem print(output), da bi bilo lepo. A string je ako ima samo jedan element, ako je samo u navodnicima
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)