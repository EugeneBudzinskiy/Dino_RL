class SaveNNException(Exception):
    def __init__(self):
        self.message = 'Trying to save untrained Neural Network'
        super().__init__(self.message)
