def count_free(places):
    free = 0
    for i in places:
        free += i.count(".")
    return free

def subtask5(n_row,places,passangers_stand,free):
    passangers_sit = 0
    # сначала в любом случае нужно рассадить так, чтобы было симметрично с теми кто уже сидит
    for i in range(n_row):
        for j in range(3):
            if places[i][j] != places[i][5-j]:
                places[i][j] = 'X'
                places[i][5-j] = 'X'
                passangers_stand-=1
        passangers_sit+= places[i].count('X')
    
    # проверка на возможность рассадки
    if passangers_sit + passangers_stand > free or passangers_stand%2 == 1 or passangers_stand < 0:
        return 'Impossible'
    
    # дозаполняем рассадку
    for i in range(n_row):
        for j in range(3):
            if places[i][j] == '.' and passangers_stand > 0:
                places[i][j] = 'X'
                places[i][5-j] = 'X'
                passangers_stand-=2
    res =''
    for row in places:
        for letter in row:
            res+=letter
        res+='\n'
    return res

def simetrical_fly(n_row:int, places:list, passangers_stand:int):

    free = count_free(places)
    #busy = 6*n_row - free

    return subtask5(n_row,places,passangers_stand,free)
        






test1 = ('1 0', 'X.XX.X')
test2 = ('2 1', 'X.XX.X', '..X...')

tests = [test1, test2]

for test in tests:
    input_list = list(map(int,test[0].split()))
    n = input_list[0]
    m = input_list[1]
    places = []
    for i in range(n):
        s = list(test[i + 1])
        places.append(s)
    print('начало теста')
    print('test - ', test)
    print(simetrical_fly(n,places,m))
    print('конец теста')