"""
Parse YAML files and perform sanity checks on the files.
"""
import yaml


class ParseYaml:
    def __init__(self, path):
        self._path = path
        self._object = self.parse_yaml(path)
        if not 'Resource' in list(self._object.keys()):
            raise "Resource not found"
        self._resource = self._object['Resource']
        

    def parse_yaml(self, path):
        with open(path, 'r') as stream:
            data = yaml.safe_load(stream)
        return data 


    def general_sanity_chekcks(self):
        """
        
        """
        return 



     