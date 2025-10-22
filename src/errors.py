class TableNotInTemplateError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class HeaderNotInTemplateError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)