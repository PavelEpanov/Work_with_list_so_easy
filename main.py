def main():
    mylist = []
    track = 1
    sum = 0

    for i in range(6):
        mylist.append(int(input(f"Введи число {track}: ")))
        track += 1


    for line in mylist:
        sum += line


    print(mylist)

    print(min(mylist), " - Минимальное число")
    print(max(mylist), " - Максимальное число")
    print(f"{sum} - Сумма списка")
    print(f"{sum /6} - Среднее арифметическое списка")
main()