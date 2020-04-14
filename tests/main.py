from random import randint

def get_guess_from_player_from_keyboard():
    n = 0
    def inner():
        nonlocal n
        if n==0:
            n += 1
            return int(input('Ваша первая догадка: '))
        return int(input('Ваша следующая догадка: '))
    return inner
get_guess_from_player_from_keyboard = get_guess_from_player_from_keyboard()

class PlayerInputGetter:
    def __init__(self):
        self.n = 0
    def __call__(self):
        if self.n == 0:
            self.n += 1
            return int(input('Ваша первая догадка: '))
        return int(input('Ваша следующая догадка: '))
#get_guess_from_player_from_keyboard = PlayerInputGetter()

def main():
    x = randint(1, 100)
    print('Хаха! Я загадал число!')
    a = get_guess_from_player_from_keyboard()
    b = get_guess_from_player_from_keyboard()
    while b != x:
        if abs(a-x)>abs(b-x):
            print('Горячее!')
        else:
            print('Холоднее...')
            print('Ну ты и лох!')
        a = b
        b = get_guess_from_player_from_keyboard()
    print(f'Победа! Я и правда загадал {x}!')

if __name__ == '__main__':
    main()
