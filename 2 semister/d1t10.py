def checker(friends, nickname):

    if friends.count(nickname) !=0:
        print("Ты – свой. Приветствую, любезный", nickname)
    else:
        print("Тут ничего нет. Еще есть вопросы?")

friends = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']
nickname = str(input("Назови свое имя!"))
checker(friends,nickname)


