class MustHaveTwoIndices(Exception):
    '''Exception raised when covariance is given a dataframe that does not only contain 2 indices.'''

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
