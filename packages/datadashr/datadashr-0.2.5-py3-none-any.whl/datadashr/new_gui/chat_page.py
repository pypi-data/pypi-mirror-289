# chat_page.py
from nicegui import ui
from datetime import datetime
from uuid import uuid4
from langchain_community.chat_models import ChatOllama
from datadashr.new_gui.settings import LIGHT_GREY

async def chat_page():
    user_id = str(uuid4())
    avatar = f'https://robohash.org/{user_id}?bgset=bg2'
    llm = ChatOllama(model='llama3', streaming=True)

    async def send() -> None:
        question = text.value
        text.value = ''

        with message_container:
            ui.chat_message(text=question, name='You', sent=True, avatar=avatar, stamp=datetime.now().strftime('%H:%M'))
            response_message = ui.chat_message(name='Datadashr', sent=False, avatar='https://www.datadashr.com/wp-content/uploads/2024/07/2.png', stamp=datetime.now().strftime('%H:%M'))
            spinner = ui.spinner(type='dots')

        response = ''
        async for chunk in llm.astream(question):
            response += chunk.content
            response_message.clear()
            with response_message:
                ui.html(response)
            ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')
        message_container.remove(spinner)

    ui.add_css(r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}')

    with ui.column().classes('w-full max-w-2xl mx-auto flex-grow items-stretch') as message_container:
        pass

    with ui.footer().style(f'background-color: {LIGHT_GREY}'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
        ui.add_css('''
            .custom-input .q-field__control {
                border-color: red !important;
            }
        ''')
        with ui.row().classes('w-full no-wrap items-center'):
            with ui.avatar().on('click', lambda: ui.navigate.to('/')):
                ui.image(avatar)
            text = ui.input(placeholder='message').on('keydown.enter', send).props('rounded outlined').classes('flex-grow custom-input')
