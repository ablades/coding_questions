def is_isogram(string):
    wordset = set()
    for char in string:
        char = char.lower()
        if char.isalpha():
            if char in wordset:
                return False
            else:
                wordset.add(char)

    return True
