def decoratore(funzione):
    def wrapper():
        print("prima dell'esecuzione")
        funzione()
        print("Dopo l'esecuzione")
    return wrapper

@decoratore
def saluta():
    print("ciao")

saluta()