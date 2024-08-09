from nicegui import ui

def render():
    ui.label('Welcome to the Home Page')
    ui.button('Go to Dashboard', on_click=lambda: ui.open('/dashboard'))
