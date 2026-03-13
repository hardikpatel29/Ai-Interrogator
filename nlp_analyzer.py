import spacy

nlp = spacy.load("en_core_web_sm")


def analyze_input(text):

    doc = nlp(text)

    location = None
    time = None
    person = None

    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:
            location = ent.text
        elif ent.label_ == "TIME":
            time = ent.text
        elif ent.label_ == "PERSON":
            person = ent.text

    # manual location detection
    locations = ["home","gym","office","mall","restaurant","park","party"]

    words = text.split()

    if len(words) == 1 and words[0].isalpha():
        person = words[0]

    for word in locations:
        if word in text.lower():
            location = word

    return {
        "location": location,
        "time": time,
        "person": person
    }