def search_substr(subst, st):
    subst.lower()
    st.lower()
    if subst.count(st) == 0:
        print("Мимо!")
    else:
        print("Есть контакт!")

subst = str(input("Введи че-нить\n"))
st = str(input("Введи че-нить еще\n"))
search_substr(subst, st)