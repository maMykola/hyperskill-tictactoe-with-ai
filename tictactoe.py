from game.ai import User, AIEasy, AIMedium, AIHard
from game.app import Game


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
    elif name == 'hard':
        return AIHard()
    else:
        return None


def exec_command(command: str):
    args = command.split()

    if args[0] == "start":
        start_game(*args[1:])
    elif args[0] == "exit":
        raise SystemExit
    else:
        raise TypeError



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
