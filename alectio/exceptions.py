"""
exceptions for alectio repository
"""

class APIKeyNotFound(Exception):     
    '''
    raise exception when api key is not set
    '''
    def __str__(self):
        message = "Alectio API Key not found"
        return message


class ModelNotFound(Exception):
    '''
    raise exceptions when the model path does not match the original checksum
    '''
    def __init__(self, val):
        self.val = val

    def __str__(self):
        message = f"Model not found for checksum: {self.val}"
        return message



class ModelExceedsChanges(Exception):
    '''
    raise exceptions when the model path does not match the original checksum
    '''
    def __init__(self, val):
        self.val = val

    def __str__(self):
        message = f"Model cannot be fully changed {self.val}"
        return message



