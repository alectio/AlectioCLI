"""
Base for all incomming objects.
"""

# there may need to be an iterable for incomming objects
class BaseAttribute:
    def __init__(self, objects, id):
        self._objects = objects
        self._id = id # id associated with the base class

    @property
    def id(self):
        """
        id associated with the base class
        """
        return self._id 

    @property
    def objects(self):
        """
        objects associated with the class
        """
        for key, value in self._objects.items():
            print(key, ' : ', value)
            
        return self._objects

    #TODO: convert camel case to snakecase, and use these attributes as the parent class + gettr methods

