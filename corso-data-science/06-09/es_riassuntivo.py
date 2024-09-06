def intro_alla_programmazione():
    print("Hello, World!")

def uml():
    print("Sono un modello standardizzato")

def condizioni(bool):
    if bool is True:
        print("Condizione Vera")
    else:
        print("Condizione Falsa")
        
def liste():
    lista = ['Questa','è','una','lista']
    print(lista)

def tutto_il_resto():
    lista = ['Questa é una lista', 'ciclata','con un for e un range','che parla anche di task','metodologia agile',' e UX/UI designer']
    for char in range(len(lista)):
        print(lista[char])

# Questo decoratore controlla se il numero positivo è compreso tra 1 e 5
def decoratore_intervallo(funzione):
    def wrapper():
        while True:
                print("Inserisci numero tra 1 e 5")
                numero = funzione()
                if  1 <= numero <= 5:
                    return numero
                else:
                    print("errore")
            
    return wrapper
        

@decoratore_intervallo
def inserisci_numero_positivo():
    while True:
        try:
            n = int(input("Inserisci numero positivo: "))
            if n > 0:
                return n
        except:
            print("Errore Inserisci numero positivo ")
            continue

def scelta():
    print("Intro alla programmazione (1) \numl (2) \ncondizioni (3) \nliste (4) \ntutto il resto (5)")
    scelta = inserisci_numero_positivo()
    
    if scelta == 1:
        intro_alla_programmazione()
    elif scelta == 2 :
        uml()
    elif scelta == 3 :
        condizioni(True)
    elif scelta == 4:
        liste()
    elif scelta == 5:
        tutto_il_resto()
    
scelta()


    

