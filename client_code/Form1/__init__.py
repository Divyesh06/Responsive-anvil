from ._anvil_designer import Form1Template
from .. import Module1
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    @Module1.on_mobile
    def mobile_func(self):
        self.button_1.font_size=2