def area_triangolo(base , altezza):
    return (base * altezza) / 2 

def area_quadrato (lato):
    return lato ** 2

def area_rettangolo(base, altezza):
    return base * altezza

def inserisci_numero_positivo():
    while True:
        try:
            n = int(input("Inserisci numero positivo: "))
            if n > 0:
                return n
        except:
            print("Errore Inserisci numero positivo ")
            continue

def vuoi_continuare ():
    while True:
        continuare = input("Vuoi continuare? y/n")
        if continuare == 'n':
            return False
        elif continuare =='y':
            return True
        else:
            continue

def scelta_area():
    while True:
        try:
            a = int(input("quale area salvare? triangolo (1) quadrato (2) rettangolo (3)"))
            if 1<= a <= 3:
                return a
        except:
            print("Inserisci numero da 1 a 3")
            continue
    

lista_aree = []

while True:
    try:
        area = scelta_area()
        
        if area == 1:
            lista_aree.append(area_triangolo(inserisci_numero_positivo(),inserisci_numero_positivo()))
        elif area == 2:
            lista_aree.append(area_quadrato(inserisci_numero_positivo()))
        elif area == 3:
            lista_aree.append(area_rettangolo(inserisci_numero_positivo(),inserisci_numero_positivo()))
        
        if vuoi_continuare():
            continue
        else:
            break
    except:
        continue

if lista_aree:        
    print(lista_aree)
else:
    print("lista vuota")
    
        
    