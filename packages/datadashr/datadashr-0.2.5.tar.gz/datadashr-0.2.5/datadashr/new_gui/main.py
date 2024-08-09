# main.py
import asyncio
from nicegui import ui, app
from datadashr.new_gui.header import header
from datadashr.new_gui.settings import LIGHT_GREY
from langchain_community.chat_models import ChatOllama
from datetime import datetime
from typing import List, Tuple
from uuid import uuid4
from datadashr.new_gui.settings_page import settings_page
from datadashr.new_gui.chat_page import chat_page

messages: List[Tuple[str, str, str, str]] = []

app.title = 'DataDashr'
app.layout = 'wide'
app.add_static_files('/static', 'static')


@ui.page('/')
async def main():
    header()
    await chat_page()


@ui.page('/settings')
async def settings():
    header()
    await settings_page()


ui.run(title='DataDashr')
