import panel as pn

class HomePage:
    def __init__(self, chat_interface):
        self.chat_interface = chat_interface
        self.view = self.create_view()

    def create_view(self):
        return pn.Column(
            self.chat_interface,
            # Add content here
        )
