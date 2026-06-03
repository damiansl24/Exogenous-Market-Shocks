class MustHaveTwoIndices(Exception):
    '''
    Exception raised when covariance is given a dataframe that does not only 
    contain 2 indices.
    '''

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InvalidDataNaN(Exception):
    '''
    Exception raised when loading a dataset from yfinance library and the 
    dataset includes NaN values
    '''

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

        def __str__(self):
            return self.message

class InvalidDataZN(Exception):
    '''
    Exception raised when loading a dataset from the yfinance library and the 
    dataset includes zero or negative values.
    '''
    def __init__(self, message):
    self.message = message
    super().__init__(self.message)

    def __str__(self):
        return self.message
