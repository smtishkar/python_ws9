def game(num2guess: int, tryes: int):
    def guessing_game():
        for _ in range(tryes):
            if num2guess == int(input('введите число: ')):
                return True
        return False
    return guessing_game

# def gaming(func):
    # def wrapper(num2guess: int, tryes: int):


if __name__ == '__main__':
    process = game(10, 3)
    print(process())