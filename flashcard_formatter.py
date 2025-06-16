def assign_difficulty(q):
    if len(q.split()) < 6:
        return "Easy"
    elif len(q.split()) < 12:
        return "Medium"
    return "Hard"
