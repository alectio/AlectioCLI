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


class YAMLFieldNotFound(Exception):
    '''
    raise excpetion when the field is no found in the yaml 
    '''
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        message = f"Field not found for {self.val}"
        return message

class InvalidYAMLField(Exception):
    '''
    raise excpetion when the field field is invalid
    '''
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
    def __str__(self):
        message = f"Field not found for {self.key}: {self.val}"
        return message


class InvalidYAMLFieldType(Exception):
    '''
    raise excpetion when the field field is invalid
    '''
    def __init__(self, key, type):
        self.key = key
        self.type = type
    
    def __str__(self):
        message = f"Field {self.key} must be {self.type}"
        return message


 


