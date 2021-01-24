# English-Theasarus


This is a Python-based English thesaurus that provides the definiton of a word the user enters, provided the word is present in the data.json file. If a user enters 
the word "Rain", instead of printing not found, the program asks the user whether they meant "rain" and then provides the definiton for rain(using the difflib library)

Click on the images folder to view images: 

a. all_correct.png: The user enters a word that exists in the dictionary

b. first_letter.png: The user enters a word where the first letter is in caps like Bird. The program converts the word into all lowercase and prints the definiton for the word "bird"

c.all_caps.png: The user enters an acronym or name of country. If word is present in data.json, definition is returned.

d. difflib.png: The user enters a word like rainn. The program uses the difflib library to geenrate a list of words close to rainn. Since rain is closest to rain, the definition of rain is printed.

e. no_word.png: The user enters a word for which no defintion exists. 


Clone this repo: https://github.com/md499/English-Theasarus.git
 
