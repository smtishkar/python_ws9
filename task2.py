from random import randint

def game(num2gess: int, tries: int):

    def guessing_game():
        for _ in range(tries):
            if num2gess == int(input('Введите число: ')):
                return True
        return False
    return guessing_game

def gaming(func):
    def wrapper(num2gess: int, tries: int):
        if not 100 >= num2gess >= 1:
            num2gess = randint(1, 100)
        if not 10 >= tries >= 1:
            tries = randint(1, 10)
        return func(num2gess, tries)
    return wrapper

@gaming
def guees_num(num2guess: int, tries: int):
    print(num2guess, tries)
    for _ in range(tries):
        if num2guess == int(input("Введите число: ")):
            return True
    return False


if __name__ == "__main__":
    print(guees_num(101, 11))