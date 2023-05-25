#игра кнб
import random
 
def get_player_choice():
    choice = input("Выберите ваш ход (камень, бумага, ножницы, ящерица или спок): ")
    while choice.lower() not in ['камень', 'бумага', 'ножницы', 'ящерица', 'спок']:
        choice = input("Ошибка! Выберите из вариантов (камень, бумага, ножницы, ящерица или спок): ")
    return choice.lower()
 
def get_computer_choice():
    choices = ['камень', 'бумага', 'ножницы', 'ящерица', 'спок']
    return random.choice(choices)
 
def determine_winner(player_choice, computer_choice):
    rules = {
        'камень': ['ножницы', 'ящерица'],
        'бумага': ['камень', 'спок'],
        'ножницы': ['бумага', 'ящерица'],
        'ящерица': ['спок', 'бумага'],
        'спок': ['камень', 'ножницы']
    }
    if player_choice == computer_choice:
        return "Ого, ничья!"
    elif computer_choice in rules[player_choice]:
        return "Мегахарош. Вы победили!"
    else:
        return "Ну ничо, все бывает. :("
 
def play_game():
    print("Добро пожаловать в игру Камень Ножницы Бумага Ящерица спок")
    print("Как играть:")
    print("Камень бьет ножницы и ящерицу")
    print("Бумага обматывает камень и очерняет спока")
    print("Ножницы режут бумагу и отрезают голову ящерице")
    print("Ящерица ест бумагу и травит спока")
    print("спок ломает ножницы и испаряет камень")
 
    play_again = True
    while play_again:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print("Вы выбрали вариант: " + player_choice)
        print("Компуктер выбрал вариант:  " + computer_choice)
        print(determine_winner(player_choice, computer_choice))
        play_again = input("Хочешь сыграть еще? (да/нет): ").lower() == 'да'
 
play_game()