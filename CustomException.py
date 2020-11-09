class SaveNNException(Exception):
    def __init__(self):
        self.message = 'Trying to save untrained Neural Network'
        super().__init__(self.message)


class LoadNNException(Exception):
    def __init__(self, incorrect_path=''):
        self.message = 'Trying to load not existing file with weights'
        self.incorrect_path = incorrect_path
        super().__init__(f"{self.message} : '{self.incorrect_path}'")
