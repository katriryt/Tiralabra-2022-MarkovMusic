from ui.ui import UI


class Main:
    """Purpose of this class is to initialize the key databases and to start the application.
    Also other basic settings required by the application are initialized.
    """

#    print("starting in the main class")
    ui = UI()
    ui.start()


if __name__ == "__main__":
    #    print("if main name - starting the spell checkers")
    spell_checker = Main()
