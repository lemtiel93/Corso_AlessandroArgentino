def decoratore(funzione):
    def wrapper():
        nome , numero = funzione()
        for i in range(2,numero):
            if numero % i == 0:
                return i
            return True
    return wrapper
        
        

    
@decoratore
def inserisci_nome_numero():
    nome = input("Inserisci nome: ")
    numero = int(input("Inserisci numero: "))
    return nome,numero
    
print(inserisci_nome_numero())
    



        

    
    
    
        