def alt_cap(text):
    new_string = ""
    for i in range(len(text)):
        character = text[i]
        if i%2 == 0:
            new_string = new_string + character.upper()
        else:
            new_string = new_string + character.lower()
    return new_string

old_string = input("What do you want to have be capitalize alternatively? ")

print(alt_cap(old_string))