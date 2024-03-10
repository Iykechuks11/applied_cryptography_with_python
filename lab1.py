import collections  # collection module has a counter method
# I used the regular expression module to remove any exiting spaces and punctuations.
import re


def get_ciphertext_letters_by_frequency(ciphertext):
    # Removes all the spacing and punctuation characters
    ciphertext_nopunc = re.sub(r"\W+", "", ciphertext)
    # ciphertext_nopunc = ciphertext_nopunc.upper()
    # Counts the number of letters in the ciphertext and returns in decending order a dictionary with the frequency of each letter in the cipher
    letter_freqs = collections.Counter(ciphertext_nopunc)
    print(letter_freqs)

    return [i[0] for i in letter_freqs.most_common()]


def reconstruct_key(ciphertext_letters):
    letters_ordered_by_freq = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "D", "L",
                               "U", "C", "M", "F", "Y", "W", "G", "P", "B", "V", "K", "X", "Q", "J", "Z"]
    print(ciphertext_letters, letters_ordered_by_freq)
    # print(sorted(zip(ciphertext_letters, letters_ordered_by_freq), key=lambda x: x[1]))
    return sorted(zip(ciphertext_letters, letters_ordered_by_freq), key=lambda x: x[1])


def get_manually_tweaked_key():
    return [
        ('r', 'I'), ('b', 'T'), ('s', 'H'),
        ('z', 'A'), ('q', 'J'), ('i', 'M'),
        ('g', 'O'), ('v', 'E'), ('h', 'N'),
        ('y', 'B'), ('a', 'U'), ('j', 'L'),
        ('f', 'P'), ('n', 'W'), ('c', 'S'),
        ('e', 'B'), ('p', 'K'), ('w', 'D'),
        ('t', 'G'), ('h', 'O'), ('l', 'Y'),
        ('o', 'V'), ('m', 'Q'), ('d', 'R'),
        ('x', 'C'), ('u', 'F')
    ]


def decipher(ciphertext, key):
    for x, y in key:
        ciphertext = ciphertext.replace(x, y)
    # print(ciphertext)
    return ciphertext


def print_ciphertext(ciphertext):
    print("\n===========")
    print("Ciphertext:")
    print("===========")
    print(ciphertext)


def print_deciphered_plaintext(type, key, plaintext):
    header = "{} Statistical Key Reconstruction:".format(type)
    print("=" * len(header), "\n", header, "\n", "=" * len(header))
    print("\n", "Key:", "\n")
    print(key, "\n")
    i = 0
    for x, y in key:
        print("{} = {},".format(y, x)),
        i += 1
        if not i % 5:
            print(i)
    print("\n", plaintext)


with open("lab1cipher.txt") as f:
    ciphertext = f.read()
    # ciphertext = ciphertext.upper()
    ciphertext_letters = get_ciphertext_letters_by_frequency(ciphertext)
    # print(ciphertext_letters)
    key = reconstruct_key(ciphertext_letters)
    print(key)
    print_deciphered_plaintext("Naive", key, decipher(ciphertext, key))
    key = get_manually_tweaked_key()
    # print(ciphertext)
    print_deciphered_plaintext(
        "Manually Tweaked", key, decipher(ciphertext, key))
    # decipher(ciphertext, key)
#
