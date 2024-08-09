# header.py
from nicegui import ui
from datadashr.new_gui.settings import PRIMARY_RED, PURE_WHITE


def header():
    with ui.header(elevated=True, fixed=True).style(
            f'background-color: {PRIMARY_RED}; display: flex; align-items: center; justify-content: space-between'):
        with ui.row():
            ui.image('https://www.datadashr.com/wp-content/uploads/2024/07/4.png').style(
                'width: 50px; height: 50px; object-fit: contain;')
        with ui.row():
            with ui.link(target='https://discord.gg/BspqGDePNm', new_tab=True):
                ui.icon('discord', color='white', size='md').style('margin-left: 10px;')
            with ui.link(target='https://www.datadashr.com', new_tab=True):
                ui.icon('public', color='white', size='md').style('margin-left: 10px;')
            with ui.link(target='https://docs.datadashr.com', new_tab=True):
                ui.icon('school', color='white', size='md').style('margin-left: 10px;')

            with ui.button(icon='menu').props('flat color=white').style('margin-left: 30px;'):
                with ui.menu() as menu:
                    ui.menu_item('Chat', on_click=lambda: ui.navigate.to('/'))
                    ui.menu_item('Settings', on_click=lambda: ui.navigate.to('/settings'))
                    ui.separator()
                    ui.menu_item('Close', on_click=menu.close)


