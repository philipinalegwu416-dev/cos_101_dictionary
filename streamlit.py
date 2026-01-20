import streamlit as st

st.title("African Language Dictionary")


choice = st.selectbox("Select Language", ("Hausa", "Yoruba", "Zulu", "Igbo", "Igala"))


hausa = {
    "hello": "sannu", "water": "ruwa", "food": "abinci", "house": "gida",
    "mother": "uwa", "father": "uba", "friend": "aboki", "name": "suna",
    "sun": "rana", "moon": "wata", "school": "makaranta", "book": "littafi"
}

yoruba = {
    "hello": "bawo", "water": "omi", "food": "ounje", "house": "ile",
    "mother": "iya", "father": "baba", "friend": "ore", "name": "oruko",
    "sun": "orun", "moon": "osupa", "school": "ile iwe", "book": "iwe"
}

zulu = {
    "hello": "sawubona", "water": "amanzi", "food": "ukudla", "house": "indlu",
    "mother": "umama", "father": "ubaba", "friend": "umngane", "name": "igama",
    "sun": "ilanga", "moon": "inyanga", "school": "isikole", "book": "incwadi"
}

igbo = {
    "hello": "ndewo", "water": "mmiri", "food": "nri", "house": "ulo",
    "mother": "nne", "father": "nna", "friend": "enyi", "name": "aha",
    "sun": "anwu", "moon": "onwa", "school": "ulo akwukwo", "book": "akwukwo"
}

igala = {
    "hello": "aneje", "water": "ama", "food": "uja", "house": "uno",
    "mother": "nne", "father": "apa", "friend": "oyi", "name": "izina",
    "sun": "ogene", "moon": "ogida", "school": "uno ekpulu", "book": "ekpulu"
}


dictionaries = {
    "Hausa": hausa,
    "Yoruba": yoruba,
    "Zulu": zulu,
    "Igbo": igbo,
    "Igala": igala
}

selected_dict = dictionaries[choice]

your_word = st.text_input("Enter English word (e.g., water, hello, house)").lower().strip()

if st.button("Search"):
    if your_word in selected_dict:
        st.success(f"The translation in {choice} is: **{selected_dict[your_word]}**")
    else:
        st.error("Word not found. Please try words like: hello, water, food, mother, father.")
