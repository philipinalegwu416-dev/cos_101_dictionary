words = {
      "dog": "kare", "cat": "mushika", "car": "mota", "bicycle": "keke", "chair": "kujira", "table": "tebur", "pen": "alƙalami", "paper": "takarda",
"household": "gidan", "market": "kasuwa", "shop": "shago", "river": "kogi", "mountain": "dutse", "rain": "ruwa", "fire": "wuta", "earth": "ƙasa",
"child": "yaro", "woman": "mace", "man": "namiji", "music": "kiɗa", "dance": "raye-raye", "laugh": "murna", "cry": " kuka", "light": "haske"

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