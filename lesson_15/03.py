letters = 'AbltOJFHgtlbgndfWLFNT'

letters_new = ''
for letter in letters:
    if letter.upper() != letter:
        letters_new += letter

print(letters_new)
