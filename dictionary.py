words = {
    "mother": "iya",
    "water": "omi",
    "yes": "bẹẹni",
    "school": "ile-iwe",
    "come": "wa",
    "everything": "gbogbo nkan",
    "drink": "mu",
    "night": "alẹ",
    "god": "Ọlọrun",
    "stand": "duro",
    "how was your day": "bawo ni ọjọ rẹ ṣe ri",
    "take": "gba",
    "morning": "owurọ",
    "sit": "joko",
    "we/us": "awa",
    "leave": "lọ",
    "car": "ọkọ ayọkẹlẹ",
    "tomorrow": "ọla",
    "understand": "ye",
    "write": "kọ",
    "how": "bawo",
    "i want": "mo fẹ",
    "long time": "o ti pẹ",
    "did you sleep well": "ṣe o sun daadaa"
}

print("Translate Words from English to Yoruba")
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
