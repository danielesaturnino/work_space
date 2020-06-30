idConsumazione = [1.00, 1.95, 2.05, 1.40, 1.50]
soldiInseriti = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00, 5.00, 10.00]
resto = 0
for i in range (idConsumazione.__len__, soldiInseriti.__len__):
    resto = soldiInseriti-idConsumazione
    if resto <= 0:
        print ("non hai inserito abbastanza soldi")
    else:
        print ("tieni il resto", resto)