words = {
    "come": "bia",
    "stand": "kwuo",
    "sit": "nọdụ",
    "god": "chineke",
    "morning": "ụtụtụ",
    "night": "abalị",
    "we/us": "anyị",
    "water": "mmiri",
    "drink": "ṅụọ",
    "leave": "pụọ",
    "understand": "ghọta",
    "how": "kedu",
    "long time": "ogologo oge",
    "school": "ụlọ akwụkwọ",
    "take": "were",
    "tomorrow": "echechi",
    "write": "dee",
    "car": "ụgbọala",
    "how was your day": "kedu ka ụbọchị gị siri bụrụ",
    "did you sleep well": "ị rahụrụ ụra nke ọma?",
    "yes": "ee",
    "i want": "achọrọ m",
    "everything": "ihe niile",
    "mother": "nne"
}

print("Translate Words from English to Igbo")
print("Choose a word from the list below:\n")

for word in words:
    print("-", word)

while True:
    word = input("\nEnter word to be translated: ").lower()

    if word in words:
        print(f"'{word}' means '{words[word]}'")
        break
    else:
        print(f"Sorry, '{word}' is not in the dictionary. Try again.")
        break