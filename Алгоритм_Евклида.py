a = int(input()) #Входное значение а
b = int(input()) #Входное значение b
while b != 0: #Цикл пока b не равен 0
    a, b = b, a % b #переменной 'a' присваевается значение переменной 'b', переменной 'b' присваевается остаток от ('a' / 'b')
print('НОД', a) #Найбольщий общий делитель