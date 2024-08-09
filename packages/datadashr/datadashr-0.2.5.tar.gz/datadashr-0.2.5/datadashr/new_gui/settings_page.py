# settings_page.py
from nicegui import ui
from typing import Any, Dict
from uuid import uuid4
from config_manager import ConfigManager

config_manager = ConfigManager()

async def settings_page():
    with ui.column().classes('w-full max-w-2xl mx-auto flex-grow items-stretch') as settings_container:
        ui.label('Settings').classes('text-2xl mb-4')

        ui.button('Add MySQL Connection', on_click=add_mysql_connection).props('rounded').classes('w-full mb-4')
        ui.button('Add MongoDB Connection', on_click=add_mongodb_connection).props('rounded').classes('w-full mb-4')

        for conn in config_manager.get_all_items('mysql_connections'):
            display_existing_connection(conn, 'mysql_connections')

        for conn in config_manager.get_all_items('mongodb_connections'):
            display_existing_connection(conn, 'mongodb_connections')

async def add_mysql_connection():
    conn_id = str(uuid4())
    connection_ui = create_connection_inputs(conn_id, 'mysql_connections')
    display_connection(connection_ui, 'mysql_connections')

async def add_mongodb_connection():
    conn_id = str(uuid4())
    connection_ui = create_connection_inputs(conn_id, 'mongodb_connections')
    display_connection(connection_ui, 'mongodb_connections')

def create_connection_inputs(conn_id: str, table: str) -> Dict[str, Any]:
    if table == 'mysql_connections':
        connection_ui = {
            'id': conn_id,
            'name': ui.input('Connection Name').props('outlined').classes('w-full mb-4'),
            'host': ui.input('Host').props('outlined').classes('w-full mb-4'),
            'user': ui.input('User').props('outlined').classes('w-full mb-4'),
            'password': ui.input('Password', type='password').props('outlined').classes('w-full mb-4'),
            'database': ui.input('Database').props('outlined').classes('w-full mb-4'),
            'save_button': None,
        }
    elif table == 'mongodb_connections':
        connection_ui = {
            'id': conn_id,
            'name': ui.input('Connection Name').props('outlined').classes('w-full mb-4'),
            'uri': ui.input('URI').props('outlined').classes('w-full mb-4'),
            'database': ui.input('Database').props('outlined').classes('w-full mb-4'),
            'save_button': None,
        }
    connection_ui['save_button'] = ui.button('Save', on_click=lambda: save_new_connection(connection_ui, table)).props('rounded').classes('w-full')
    return connection_ui

def display_connection(connection_ui: Dict[str, Any], table: str):
    with ui.card().classes('w-full mb-4'):
        ui.label(f"Connection ID: {connection_ui['id']}")
        for key, input_field in connection_ui.items():
            if key != 'save_button':
                input_field.classes('w-full mb-4')
        connection_ui['save_button'].classes('w-full')

def display_existing_connection(connection_data: Dict[str, str], table: str):
    conn_id = connection_data['id']
    connection_ui = create_connection_inputs(conn_id, table)
    for key, input_field in connection_ui.items():
        if key != 'save_button':
            input_field.value = connection_data[key]
    display_connection(connection_ui, table)

async def save_new_connection(connection_ui: Dict[str, Any], table: str):
    conn_data = {key: input_field.value for key, input_field in connection_ui.items() if key != 'save_button'}
    conn_data['id'] = connection_ui['id']
    config_manager.add_item(table, conn_data)
    ui.notify(f'{table} connection saved!')

async def update_existing_connection(conn_id: str, connection_ui: Dict[str, Any], table: str):
    conn_data = {key: input_field.value for key, input_field in connection_ui.items() if key != 'save_button'}
    conn_data['id'] = conn_id
    config_manager.update_item(table, conn_id, conn_data)
    ui.notify(f'{table} connection updated!')
