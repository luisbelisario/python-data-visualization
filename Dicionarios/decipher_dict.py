def count_letters(word_list):

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
    print(letter_count)

    for k in letter_count.keys():
        for i in range(len(word_list)):
            word = word_list[i]
            for l in word:
                if k == l:
                    letter_count[k] += 1
    print(letter_count)

    highestValue = 0
    highestLetter = ''
    for k, v in letter_count.items():
        if v > highestValue:
            highestValue = v
            highestLetter = k
    print(highestLetter)
    print(highestValue)


monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
monty_words = monty_quote.split(' ')
print(monty_words)

count_letters(monty_words)
