zulu_dictionary = {
    "hello": "sawubona",
    "goodbye": "hamba kahle",
    "please": "ngicela",
    "thank you": "ngiyabonga",
    "yes": "yebo",
    "no": "cha",
    "water": "amanzi",
    "food": "ukudla",
    "house": "indlu",
    "friend": "umngane",
    "love": "uthando",
    "family": "umndeni",
    "happy": "jabula",
    "sad": "dumele",
    "dog": "inja",
    "cat": "ikati",
    "child": "umntwana",
    "mother": "umama",
    "father": "ubaba",
    "school": "isikole"
}

# Function to translate words to Zulu
def translate_to_zulu(word):
    return zulu_dictionary.get(word.lower(), "Translation not found.")

# Main program
print("Enter an English word to translate into Zulu:")
word = input()

translation = translate_to_zulu(word)
print(f"The translation of '{word}' in Zulu is '{translation}'.")