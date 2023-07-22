from radiobuttonApp.runner import CreateCalcButton


def run_app():
    creator = CreateCalcButton()
    creator.create_gui()


if __name__ == "__main__":
    run_app()
