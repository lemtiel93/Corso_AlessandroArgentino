def area_triangolo(base , altezza):
    return (base * altezza) / 2 

def area_quadrato (lato):
    return lato ** 2

def area_rettangolo(base, altezza):
    return base * altezza

def inserisci_numero_positivo():
    while True:
        try:
            n = int(input("Inserisci numero positivo"))
            if n > 0:
                return n
        except:
            print("Inserisci numero positivo")
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

lista_aree = []

while True:
    try:
        area = int(input("quale area vuoi salvare? triangolo (1) quadrato (2) rettangolo (3)"))
        
        if area == 1:
            
            lista_aree.append(area_triangolo(inserisci_numero_positivo(),inserisci_numero_positivo()))
        elif area == 2:
            lista_aree.append(area_quadrato(inserisci_numero_positivo()))
        elif area == 3:
            lista_aree.append(area_rettangolo(inserisci_numero_positivo(),inserisci_numero_positivo()))
        else:
            continue
        if vuoi_continuare():
            continue
        else:
            break
    except:
        continue
        
print(lista_aree)
    
        
    