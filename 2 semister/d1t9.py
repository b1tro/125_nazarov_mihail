def delaemZabor(nedoZabor):
    nedoZabor = nedoZabor.lower()
    chet = False
    zabor = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in nedoZabor:
        if letters.count(i)!=0:
            if chet:
                i = i.upper()
                chet = False;
            else:
                i = i.lower()
                chet = True;
            zabor+=i
        else:
            zabor += i
    return(zabor)
pokaNeZabor = str(input("Из чего строить будем?\n"))
print(delaemZabor(pokaNeZabor))