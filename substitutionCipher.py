# This module enabled me to access the randint() method. I used this method
# to generate random numbers for each permutation in line 12 and avoided repetitions

import random

# Key generating function


def generate_key():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters_into_list = list(letters)
    key = {}  # A dictionary mapping letters to keys

    for letter in letters:
        key[letter] = letters_into_list.pop(
            random.randint(0, len(letters_into_list) - 1))

    return key

# Encrypting function


def encrypt(key, plaintext):
    cipher = ""
    for letter in plaintext:
        if letter in key:
            cipher += key[letter]
        else:
            cipher += letter
    return cipher


key = generate_key()
print(key)

plaintext = """
To the special classmate who decrypted this message I have a message for you I may never fully understand the struggles and challenges that you face but know that your presence makes a world of difference In Gods perfect timing everything will fall into place and all the pain and hardship will fade away replaced by beauty and joy Keep shining bright my friend The world is a better place with you in it

I will tell you a story about Thomas

In the small town of Willowbrook there lived a man named Thomas who was known for his cunning ways and sharp tongue Thomas had spent most of his life manipulating others for his own gain leaving a trail of broken relationships and shattered dreams in his wake He took pleasure in exploiting peoples weaknesses believing that kindness was a sign of weakness itself

However as Thomas grew older a sense of emptiness began to gnaw at him Despite his material wealth he felt a profound loneliness that no amount of money could fill His conscience long buried under layers of deceit started to stir reminding him of the pain he had caused others

One stormy night as Thomas sat alone in his lavish mansion he found himself reflecting on his life choices Memories of the people he had hurt flashed before his eyes each face etched with sorrow and betrayal He realized with a pang of regret that his actions had left a trail of devastation not only in the lives of others but also in his own soul

Thomas began by reaching out to those he had hurt offering heartfelt apologies and restitution where possible He spent hours listening to their grievances allowing himself to feel their pain and remorsefully acknowledging the harm he had caused His genuine contrition touched the hearts of many gradually earning him forgiveness and reconciliation

As Thomas walked the path of repentance he discovered unexpected blessings along the way He found solace in the forgiveness of others and his relationships began to heal as trust was slowly rebuilt With each act of kindness and humility he felt the heavy burden of guilt lifting from his shoulders replaced by a sense of inner peace he had long forgotten
From your friend and classmate John
"""
cipher = encrypt(key, plaintext.upper())

print(cipher)
