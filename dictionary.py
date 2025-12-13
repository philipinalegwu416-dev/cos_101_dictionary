
english_to_hausa = {
    "house": "gida",
    "water": "ruwa",
    "food": "abinci",
    "book": "littafi",
    "school": "makaranta",
    "sun": "rana",
    "moon": "wata",
    "star": "tawo",
    "boy": "yaro",
    "girl": "yarinya",
    "father": "uba",
    "mother": "uwa",
    "friend": "aboki",
    "work": "aiki",
    "road": "hanya",
    "go": "tafi",
    "come": "zo",
    "sleep": "bari",
    "name": "suna",
    "tree": "itace"
}
print ("G-squad language dictionary")
print ("Hi There 👋")
print ("Available English word you can translate to ")
for word in english_to_hausa.keys():
    print("-", word )
while True:
    word = input("What English word do you want to translate to Hausa ").lower().strip()
    
    if word in english_to_hausa:
        print (f"The hausa  translation of {word} is: '{english_to_hausa[word]}'")
    else:
        print (f"sorry, '{word}' is not in the dictionary")
    continue

#keep asking  until user enter the valid word
'''while word not in english_to_hausa:
    print (f" '{word}' not in dictionary")
    word = input(" please Enter a valid word").lower().strip()
    
    print (f"the hausa translation of {word} is: '{english_to_hausa [word]}'")
    break

