from menu import GameMenu
from Game import GameEngine
from config import HUMAN


def main():
    menu = GameMenu(GameEngine(HUMAN))
    menu.start_menu()


if __name__ == '__main__':
    main()
