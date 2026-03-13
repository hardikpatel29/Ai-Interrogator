def calculate_suspicion(text):
    if not text :
        return 0

    suspicion = 0

    if "don't know" in text.lower() or "dont know" in text.lower():
        suspicion += 10

    if "maybe" in text.lower():
        suspicion += 5

    return suspicion