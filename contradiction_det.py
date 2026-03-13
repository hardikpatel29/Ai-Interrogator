from conversation_memory import get_memory

def detect_contradiction(analysis):

    memory = get_memory()

    for past in memory:

        if analysis["location"] and past["location"]:
            if analysis["location"] != past["location"]:
                return f"Earlier you said you were at {past['location']}, now you say {analysis['location']}. Why?"

    return None