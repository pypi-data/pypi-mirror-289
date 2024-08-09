from nicegui import ui


def other_page(container):
    container.clear()
    with container:
        ui.label('This is the other page').style('padding: 10px;')

