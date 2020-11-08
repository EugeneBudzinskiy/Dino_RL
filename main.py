from Game import GameEngine
from menu import GameMenu


def main():
    menu = GameMenu(GameEngine())
    menu.start_menu()


if __name__ == '__main__':
    main()
