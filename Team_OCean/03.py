# Задание 3:
        # Напишите программу, которая измеряет длину введенной строки.
        # Если строка длиннее десяти символов, то выносится предупреждение.
        # Если короче, то к строке добавляется столько символов *, чтобы ее длина составляла десять символов, после чего новая строка должна выводиться на экран.
###################################################################


stroka=input()
if len(stroka)>10:
    print('preduprejdenie')
else:
    for i in range(len(stroka),10):
        stroka+="*"
    print(stroka)