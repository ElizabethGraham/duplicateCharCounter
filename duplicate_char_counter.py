def duplicate_count(text):
<<<<<<< HEAD
    char_dict = {}  # Dictionary where we store the Chars and their occurrence amount
    for x in text:
        if text.count(x) > 1 and x not in char_dict:  # If x occurs more than once and hasn't already been done
                char_dict.update({x:text.count(x)})  # Add the key and value to char_dict{}
    return char_dict

def main():
    user_input = input("Text input: ")
    for letter, occurrences in duplicate_count(user_input).items():
        print("Letters: {}, Occurrences: {}".format(letter, occurrences))



if __name__ == "__main__":
    main()
=======
    duplicates = []
    count = 0
    user_input = text.lower()
    for x in user_input:
        if user_input.count(x) > 1 and x not in duplicates:
            duplicates.append(x)
            count += 1
    return count
>>>>>>> origin/master
