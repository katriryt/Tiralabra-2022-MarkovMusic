from ui.ui import UI


class Main:
    """Purpose of this class is to initialize and start the application.
    """

    ui = UI()
    ui.start()


if __name__ == "__main__":
    spell_checker = Main()
