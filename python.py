#
Games = [["", "", ""] for i in range(3)]
Games[0][1] = " "
Games[0][2] = " "
Games[0][0] = " "
def xgame():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(Games[i])
        print(f"{i} {row_info}")


def ask():
    while True:
        game = input("      Ваш ход: ").split()

        if len(game) != 2:
            print(" Введите 2 координаты. ")
            continue

        x, y = game

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа. ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y > 2:
            print(" Координаты вне диапазона. ")
            continue
        if Games[x][y] != "":
            print(" Клетка занята. ")

        return x, y


num = 0
while True:
   num += 1

   xgame()

   if num  % 2 == 1:
       print(" Ходит крестик. ")
   else:
       print(" Ходит нолик. ")

   x, y = ask()

   if num  % 2 == 1:
       Games[x][y] = "x"
   else:
       Games[x][y] = "0"

   if num == 9:
       print(" Ничья. ")
       break


ask()
xgame()
