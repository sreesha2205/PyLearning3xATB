letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']


def filter_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


result = filter(filter_vowel, letters)
print(list(result))

# filter only works with true or false