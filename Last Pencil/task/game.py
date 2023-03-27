from random import randint
num_pencils = -1
current_player = ""
human_player = "Ethan"
computer_player = "BOT"


def initialize_game():
    global num_pencils, current_player

    print("How many pencils would you like to use:")
    while True:
        raw_data = input()
        try:
            num_pencils = int(raw_data)
        except ValueError:
            print("The number of pencils should be numeric")
            continue

        if num_pencils == 0:
            print("The number of pencils should be positive")
            continue
        elif num_pencils < 0:
            print("The number of pencils should be numeric")
            continue

        break

    print(f"Who will be the first ({human_player}, {computer_player}):")
    while True:
        raw_data = input()
        if raw_data not in {human_player, computer_player}:
            print(f"Choose between {human_player} and {computer_player}")
            continue
        current_player = raw_data

        break


def display_pencils():
    print('|' * num_pencils)


def switch_player():
    global current_player

    current_player = human_player if current_player == computer_player else computer_player


def computer_take_pencil():
    global num_pencils, computer_player
    pencils_taken = 0
    print(f"{computer_player}'s turn:")

    # winning position
    if num_pencils % 4 == 0:
        pencils_taken = 3
    elif num_pencils % 4 - 3 == 0:
        pencils_taken = 2
    elif num_pencils % 4 - 2 == 0:
        pencils_taken = 1

    # losing position
    elif num_pencils == 1:
        pencils_taken = 1
    else:
        pencils_taken = randint(1, 3)

    print(pencils_taken)
    num_pencils -= pencils_taken


def player_take_pencil():
    global num_pencils, human_player

    print(f"{human_player}'s turn!")
    while True:
        raw_data = input()
        if raw_data not in {"1", "2", "3"}:
            print("possible values: '1', '2' or '3'")
            continue

        raw_data = int(raw_data)  # now we know for sure that it is an int
        if raw_data > num_pencils:
            print("Too many pencils were taken")
            continue

        num_pencils -= raw_data

        break


def turn():
    display_pencils()
    if current_player == computer_player:
        computer_take_pencil()
    else:
        player_take_pencil()


initialize_game()
while num_pencils > 0:
    turn()
    switch_player()
    if num_pencils == 0:
        print(f"{current_player} won!")  # Because whoever took it last lost, so other player won
