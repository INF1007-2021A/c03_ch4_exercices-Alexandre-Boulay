#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(x) -> bool:
    if len(x)%2==0:
        return("La chaine de caractères est paire")
    else:
        return("La chaine de caractère est impaire")


def remove_third_char(no3) -> str:
    return(no3[:2]+no3[3:])


def replace_char(string: str, old_char: str, new_char: str) -> str:
    return string.replace(old_char, new_char)



def get_nb_char(string: str, char: str) -> int:
    nb=-1
    for letter in string:
        if letter==char:
            nb+=1
    return(nb)



def get_nb_words(sentence: str) -> int:
    nb_mots=1
    for char in sentence:
        if char==" ":
            nb_mots+=1
    return(nb_mots)


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
