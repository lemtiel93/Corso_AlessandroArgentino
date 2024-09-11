def media(lista):
    sum = 0
    for element in lista:
        sum += element
    return sum / len(lista)

dizionario_voti = {}
while True:
    nome = input("Inserisci nome: ")
    voti = []
    while True:
        voto = input("Inserisci voto o 's' per terminare ")
        if voto =='s':
            break
        else:
            voti.append(int(voto))
            
    dizionario_voti[nome] = { 'media' :media(voti)
                             , 'voti' : voti}
    
    check = input("vuoi continuare (y) o stampare media (media)? ")
    if check== 'media':
        for elemento  in dizionario_voti:
            print(f"Nome: {elemento} Media : {dizionario_voti[elemento]['media']}")
        break
