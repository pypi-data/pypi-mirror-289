from nicegui import ui


def dark_page(container):
    container.clear()
    with container:
        ui.label('This is the dark page').style('color: white; padding: 10px; background-color: #333;')


