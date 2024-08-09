from nicegui import ui

def render():
    ui.label('Welcome to the Dashboard')
    ui.button('Back to Home', on_click=lambda: ui.open('/'))
