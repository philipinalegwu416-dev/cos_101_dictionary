import streamlit as st

choice = st.selectbox("language",("Hausa", "Yoruba", "Zulu", "Igbo", "Igala"))

hausa = {
    "house": "gida", "water": "ruwa", "food": "abinci", "book": "littafi",
    "school": "makaranta", "sun": "rana", "moon": "wata", "star": "tawo",
    "boy": "yaro", "girl": "yarinya", "father": "uba", "mother": "uwa",
    "friend": "aboki", "work": "aiki", "road": "hanya", "go": "tafi",
    "come": "zo", "sleep": "bari", "name": "suna", "tree": "itace"
}

igala = {
    "hello": "Aneje", "thank you": "Ameyo", "water": "Ama", "food": "Uja",
    "mother": "Nne", "father": "Apa", "house": "Uno", "book": "Ekpulu",
    "school": "Uno ekpulu", "child": "Omo", "sun": "Ogene", "moon": "Ogida",
    "star": "Ukwu", "love": "Ifunanya", "god": "Ojo", "friend": "Oyi",
    "name": "Izina", "market": "Uloja"
}

yoruba = {
    "hello": "bawo", "come": "ma bo", "go": "lo", "water": "omi", "food": "ounje",
    "mother": "iya", "father": "baba", "house": "ile", "book": "iwe",
    "school": "ile iwe", "child": "omo", "sun": "orun", "moon": "osupa",
    "star": "irawo", "love": "ife", "god": "olorun", "friend": "ore",
    "name": "oruko", "market": "oja", "good morning": "E kaaro",
    "good afternoon": "E kaasan", "good evening": "E kurole", "good night": "O daaro"
}

zulu = {
    "hello": "sawubona",
    "come": "woza",
    "go": "hamba",
    "water": "amanzi",
    "food": "ukudla",
    "mother": "umama",
    "father": "ubaba",
    "house": "indlu",
    "book": "incwadi",
    "school": "isikole",
    "child": "ingane",
    "sun": "ilanga",
    "moon": "inyanga",
    "star": "inkanyezi",
    "love": "uthando",
    "god": "uNkulunkulu",
    "friend": "umngane",
    "name": "igama",
    "market": "imakethe",
    "good morning": "sawubona",
    "good afternoon": "sawubona",
    "good evening": "sawubona",
    "good night": "ulale kahle"
}

if choice == "hausa":
    dictionary = hausa
elif choice == "yoruba":
    dictionary = yoruba
elif choice == "igbo":
    dictionary = igbo
elif choice == "igala":
    dictionary = igala
elif choice == "zulu":
    dictionary = zulu

your_word = st.text_input("Enter your word").lower()

if st.button("search"):
    if your_word in dictionary:
        st.title(search_dictionary(your_word, dictionary))
    else:
        st.error("Your word is not in the dictionary")