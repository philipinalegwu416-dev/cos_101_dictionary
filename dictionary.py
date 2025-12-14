words = {
        "Hello":"szia",
        "Thankyou":"Köszönöm",
        "yes":"Igen",
        "No":"Nem",
        "Please":"Kèrem",
        "book":"Könyv",
        "water":"Vìz",
        "bread":"Kenyèr",
        "house":"Ház",
        "person":"Ember",
        "friend":"Barát",
        "love":"Szeretet",
        "time":"Idö",
        "day":"Nap",
        "night":"Éjszaka",
        "work":"Munka",
        "money":"Pénz",
        "school":"Iskola",
        "good":"Jó",
        "beautiful":"Szép",
        }
print("Translate Words form English to Hungarian")
print("choose a word to be translated from the Available words")

for word in words.keys():
    print ( "-", word)

while True:
    word = input("Enter word to be translated: ").lower().strip()

    if word in words:
        print(f" '{word}' means '{words[word]}' ")
        break
    else:
        print(f"sorry {word} is not in the Dictionary")
        break