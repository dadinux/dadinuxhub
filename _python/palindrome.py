#!/usr/bin/env python3

def palindrome():
    import re

    print('Scopri se la frase è palindroma')
    
    stringa = input('Inserisci una parola o una frase:  ')

    stringa = stringa.replace(chr(32),"")
    lunga = len(stringa)
    
    new_stringa = ""
    conta = 0
    for i in stringa:
        new_stringa = new_stringa + stringa[lunga - conta - 1]
        conta = conta + 1
    
    if stringa == new_stringa:
        print("Il testo è palindromo")
    else:
        print("Il testo non è palindromo")


            
palindrome()
