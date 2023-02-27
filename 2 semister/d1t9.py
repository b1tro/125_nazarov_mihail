def delaemZabor(nedoZabor):
    chet = False
    zabor = ''
    for i in nedoZabor:
        if chet:
            i = i.upper()
            chet = False;
        else:
            i = i.lower()
            chet = True;
        zabor+=i
    return(zabor)

pokaNeZabor = str(input("Что-нибудь введи"))
print(delaemZabor(pokaNeZabor))