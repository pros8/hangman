import random
spisok = ["кант",
          "хроника",
          "зал",
          "галера",
        "балл",
          "вес",
          "кафель",
          "знак",
          "Фильтр",
          "башня",
          "кондитер",
          "омар",
          "чан",
          "пламя",
          "банк",
          "тетерев",
          "муж",
          "камбала"]

def hangman():
    i = random.randint(0,18)
    word = spisok[i]
    wrong = 0
    stages = ["",
              "_____________              ",
              "|                          ",
              "|             |            ",
              "|             0            ",
              "|            /|\           ",
              "|            / \           ",
              "|                          "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong +=1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Вы лузер! Было загадано слово:\
 {}.".format(word))

hangman()
