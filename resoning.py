from conversation_memory import get_memory

def generate_question():

    memory = get_memory()

    location = None
    time = None
    person = None

    # scan entire conversation
    for entry in memory:

        if entry["location"]:
            location = entry["location"]

        if entry["time"]:
            time = entry["time"]

        if entry["person"]:
            person = entry["person"]

    # reasoning logic
    if location and not time:
        return f"You said you were at {location}. What time exactly?"

    if location and time and not person:
        return f"So you were at {location} at {time}. Did anyone see you there?"

    if person:
        return f"What were you doing with {person} at the {location}?"

    return "Can you describe your movements more clearly?"