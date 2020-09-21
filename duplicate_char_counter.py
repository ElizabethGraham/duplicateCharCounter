def duplicate_count(text):
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
