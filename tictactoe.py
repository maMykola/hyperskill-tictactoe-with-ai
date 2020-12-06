from ai import User, AIEasy, AIMedium
from app import Game


def start_game(first=None, second=None):
    player1 = get_player(first)
    player2 = get_player(second)

    if not player1 or not player2:
        raise TypeError

    Game(player1, player2).run()


def get_player(name):
    if name == 'user':
        return User()
    elif name == 'easy':
        return AIEasy()
    elif name == 'medium':
        return AIMedium()
    else:
        return None


def exec_command(command: str):
    args = command.split()

    if args[0] == "exit":
        raise SystemExit

    if args[0] == "start":
        start_game(*args[1:])


def main():
    while True:
        try:
            exec_command(input("Input command: "))
        except TypeError:
            print("Bad parameters!")
        except SystemExit:
            break


if __name__ == "__main__":
    main()
