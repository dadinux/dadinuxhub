somma = 0


for i in range(100):
    
    if somma <= 100:
        somma = somma + i
        print("La somma parziale è: " + str(somma))
    else:
        break

print("La somma definitiva è: " + str(somma))