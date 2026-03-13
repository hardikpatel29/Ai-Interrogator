memory = []

def store_response(text, analysis):

    entry = {
        "text": text,
        "location": analysis["location"],
        "time": analysis["time"],
        "person": analysis["person"]
    }

    memory.append(entry)

def get_memory():
    return memory