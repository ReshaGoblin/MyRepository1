a=int(input()) # Размерность массива
for j in range(0, a): # Цикл for количество итерации в зависимости от размера массива
    mas=input().split() #Создаем список со входными значениями  
    if j==a-1: # Если введена последняя строка то выполнить следующее
        for i in range(0, a): # Цикл for количество итерации в зависимости от размера массива
           mas[i]=int(mas[i]) # В списке mas объектам задаем int тип данных
           print(mas[i]+a, end=' ') # Выводим ответ
print()          
