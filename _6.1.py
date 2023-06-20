N = int(input("Введите целое число N:"))

Count = N
Count_Zero = 0

while Count > 0:
    
        N1 = int(input("Введите целое число:"))
        Count -= 1
        if N1 == 0:
            Count_Zero += 1
print('Вы ввели', Count_Zero, 'нуля/нулей')