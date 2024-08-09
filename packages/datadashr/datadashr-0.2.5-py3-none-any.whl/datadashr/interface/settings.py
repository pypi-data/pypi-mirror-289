import panel as pn
import json

class SettingsPage:
    def __init__(self):
        self.db_connections = pn.widgets.TextAreaInput(name='Database Connections', placeholder='Enter DB connections JSON')
        self.save_button = pn.widgets.Button(name='Save', button_type='primary')
        self.view = self.create_view()

    def create_view(self):
        return pn.Column(
            pn.pane.Markdown("# Settings"),
            self.db_connections,
            self.save_button,
        )

    def save_settings(self, event):
        db_connections = self.db_connections.value
        self.save_db_connections(db_connections)

    def save_db_connections(self, db_connections):
        try:
            db_config = json.loads(db_connections)
            with open('db_connections.json', 'w') as f:
                json.dump(db_config, f, indent=4)
            print("Database connections saved successfully.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
