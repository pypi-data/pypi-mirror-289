from nicegui import ui, app


def send():
    prompt = app.storage.client.get("prompt")
    personality = app.storage.client.get("personality")
    ui.notify(
        f"Prompt: {prompt}, Personality: {personality}",
        type="info"
    )


@ui.page('/')
def index():
    with ui.grid(columns=16).classes("w-3/4 place-self-center gap-4"):
        ui.markdown("# 🚀 My Gemini Chatbot").classes("col-span-full")
        ui.input(label="Prompt").bind_value(app.storage.client, "prompt").classes("col-span-10")
        ui.select(
            options=["Default", "Santa Claus"],
            value="Default",
            label="Personality"
        ).bind_value(app.storage.client, "personality").classes("col-span-6")
        ui.button("Send to Gemini", on_click=send).classes("col-span-full")

        with ui.card().classes("col-span-full"):
            ui.markdown("## Gemini Response")
            ui.separator()
            ui.label("Send your prompt to Gemini and see the response here.")


ui.run()