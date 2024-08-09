import panel as pn
from datadashr.interface.main import App


def main():
    app = App()
    pn.serve({'/': app.serve}, show=True, title='Datadashr')


if __name__ == '__main__':
    main()
