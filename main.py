from Game import GameEngine

engine = GameEngine()


def main():
    engine.menu.set_process_func(process)
    engine.menu.start_menu()


def process():
    if engine.is_human:
        while engine.is_running:
            engine.render()

            action = engine.get_action_from_key_check()
            engine.step(action)

    else:
        for i_episode in range(100):
            engine.setup()

            for t in range(1000):
                # engine.render()
                engine.step('jump')

                if not engine.is_alive:
                    print(t)
                    break


if __name__ == '__main__':
    main()
