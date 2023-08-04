

class RadioValueException(Exception):
    def __init__(self, message='check radio values'):
        self.message = message
        super().__init__(self.message)
