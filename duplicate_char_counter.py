def duplicate_count(text):
    duplicates = []
    count = 0
    user_input = text.lower()
    for x in user_input:
        if user_input.count(x) > 1 and x not in duplicates:
            duplicates.append(x)
            count += 1
    return count
