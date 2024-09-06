def decoratore(funzione):
    def wrapper(stringa):
        stringa_compressa = funzione(stringa)
        if len(stringa_compressa) == len (stringa):
            return stringa
        else:
            return stringa_compressa
    return wrapper 

@decoratore
def comprimi_stringa(stringa):
    new_stringa = ''
    count = 1
    for i in range(1, len(stringa)):
        if stringa[i - 1] == stringa[i]:
            count +=1
        else:
            new_stringa += stringa[i - 1] + str(count)
            count = 1
    new_stringa += stringa[-1] + str(count)
    return new_stringa


print(comprimi_stringa("aabbcc"))