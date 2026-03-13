def generate_followup(analysis):

    location = analysis.get("location")
    time = analysis.get("time")
    person = analysis.get("person")

    if location:
        return f"You said you were at {location}. Which {location} exactly?"

    if time:
        return f"You mentioned {time}. Can you explain what you were doing at that time?"

    if person:
        return f"You mentioned {person}. What was your interaction with them?"

    return "Can you explain that in more detail?"