#!/usr/bin/env python3

def function():

    import math

    a = int(input("Inserisci il primo intero: "))
    b = int(input("Inserisci il secondo intero: "))
    c = int(input("Inserisci il terzo intero: "))

    # a è divisibile per 2?
    # a è divisibile per 5?
    # b è divisibile per 2?
    # b è divisibile per 5?
    # c è divisibile per 2?
    # c è divisibile per 5?

## SOMMA
    if ( a%2 ) == 0 or ( a%5 ) == 0: a1 = a
    else: a1 = 0
    
    if ( b%2 ) == 0 or ( b%5 ) == 0: b1 = b
    else: b1 = 0
    
    if ( c%2 ) == 0 or ( c%5 ) == 0: c1 = c
    else: c1 = 0
    
    res1 = a1 + b1 + c1

## PRODOTTO
    if ( a%2 ) == 0 and ( a%5 ) == 0: a2 = a
    else: a2 = 1
    
    if ( b%2 ) == 0 and ( b%5 ) == 0: b2 = b
    else: b2 = 1
    
    if ( c%2 ) == 0 and ( c%5 ) == 0: c2 = c
    else: c2 = 1
    
    res2 = a2 * b2 * c2

## MEDIA
    if ( a%2 )!=0 and ( b%5 )!=0:
        a3 = a
        n1 = 1
    else: 
        a3 = 0
        n1 = 0

    if ( b%2 )!=0 and ( b%5 )!=0:
        b3 = b
        n2 = 1
    else:
        b3 = 0
        n2 = 0

    if ( c%2 )!=0 and ( c%5 )!=0:
        c3 = c
        n3 = 1
    else:
        c3 = 0
        n3 = 0

    print("Somma: " + str(res1))
    print("Prodotto: " + str(res2))

    if n1==0 and n2==0 and n3==0 :
        print("La media non è calcolabile") 
    else:    
        res3 = (a3 + b3 + c3) / (n1 + n2 + n3)
        print("Media: " + str(res3))

function()