import json 
from difflib import get_close_matches

data = json.load((open("data.json")))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
       
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]


    elif len(get_close_matches(w, data.keys())) > 0:
        choice = input("Did you mean %s instead? Enter Y if yes or N is no." % get_close_matches(w, data.keys())[0])
        if choice.lower() == 'y':
            return data[get_close_matches(w, data.keys())[0]]        

        elif choice.lower() == 'n':
            return "The word does not exist. Please double check."
            
        else:
            return "We didn't understand your entry."

    else: 
        return "The word does not exist. Please double check."


word = input("Enter word: ")

output= translate(word)


if type(output) == list:
    for x in output: 
        print(x)
else: 
    print(output)
