# -*- coding: utf-8 -*-
"""
MOON5: Cipher and Decipher Utility
"""

import json
from os import listdir
from random import choice

# Load settings
SETTINGS_PATH = "settings.json"
with open(SETTINGS_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)


# Load word lists
WORD_LIST_PATH = data["word_lst_pth"]
KEY_LIST_PATH = data["key_lst_pth"]
OUTPUT_DIR = data["OUTPUT_DIR"]

word_list = open(WORD_LIST_PATH, "r", encoding="utf-8").read().splitlines()

key_list = open(KEY_LIST_PATH, "r", encoding="utf-8").readlines()
key_list = [key.replace("\n", "") for key in key_list]

def cipher(text, word_list, key_list):
    """Encrypt a given text using the word list and key list."""
    
    text = text.lower()
    cipher_dict = {word_list[i]: key_list[i] for i in range(len(word_list))}
    
    return " ".join(cipher_dict.get(word, word) for word in text.split(" "))

def decipher(text, word_list, key_list):
    """Decrypt a given text using the key list and word list."""
    decipher_dict = {key_list[i]: word_list[i] for i in range(len(key_list))}
    
    return " ".join(decipher_dict.get(word, word) for word in text.split(" "))

def cipher_file(input_file, output_file):
    """Encrypts lines in the input file and writes them to the output file."""
    encrypted_sentences = []
    keys_lst = []

    with open(input_file, 'r', encoding='utf-8') as input_file:
        input_file = input_file.read().splitlines()

        for line in input_file:
            # Sélectionne un fichier de clé aléatoire
            key_pth = f"{OUTPUT_DIR}{choice(listdir(OUTPUT_DIR))}"
            key_lst = open(key_pth, "r", encoding="utf-8").readlines()
            key_lst = [key.replace("\n", "") for key in key_lst]

            # Ajoute le chemin du fichier de clé utilisé
            keys_lst.append(key_pth)

            # Chiffre la ligne et l'ajoute à la liste des résultats
            encrypted_sentences.append(cipher(line, word_list, key_lst))
    
    # Écrit le texte chiffré dans le fichier de sortie
    with open(output_file, 'w', encoding='utf-8') as output_file:
        for sentence in encrypted_sentences:
            output_file.write(sentence + "\n")
    
    return keys_lst


def decipher_file(input_file, key_lst):
    """Decrypts lines in the input file using the corresponding keys."""
    with open(input_file, 'r', encoding='utf-8') as input_file:
        encrypted_lines = input_file.read().splitlines()

    # Parcourt chaque ligne chiffrée et la clé correspondante
    for line, key_path in zip(encrypted_lines, key_lst):
        key_list = open(key_path, "r", encoding="utf-8").readlines()
        key_list = [key.replace("\n", "") for key in key_list]
        print(decipher(line, word_list, key_list))


# Chiffrement
keys_used = cipher_file("et.txt", "output_file.txt")
print(keys_used)
# Déchiffrement
decipher_file("output_file.txt", keys_used)




"""if __name__ == "__main__":
    message = "bonjour tous le monde je dit que je suis une phrase de test"
    print("Original Message:", message, "\n")

    encrypted_text = cipher(message, word_list, key_list)
    print("Encrypted Text:", encrypted_text, "\n")

    decrypted_text = decipher(encrypted_text, word_list, key_list)
    print("Decrypted Text:", decrypted_text)
"""

