"""
Parse YAML files and perform sanity checks on the files.
"""
import yaml


class ParseYaml:
    def __init__(self, path):        
        self._valid_resources = ["Project", "Experiment", "Strategy"]
        self._object = self.parse_yaml(path)

    def parse_yaml(self, path):
        """
        parse yaml file the
        :params: path - path to yaml file.
        """
        with open(path, 'r') as stream:
            data = yaml.safe_load(stream)
        return data 


    def general_sanity_checks(self):
        """
        perform general sanity checks on the file
        """
        if not 'Resource' in list(self._object.keys()):
            raise "Resource key not found"

        resource = self._object['resource']
        if not resource in self._valid_resources:
            raise "Resource not found, specify Project, Experiment, Strategy"
        self._resource = resource
        return 


class ParseStrategyYaml(ParseYaml):
    """
    parse strategy yaml
    """
    def __init__(self, path):
        self._path = path
        self._required_fields = ["mode", "query_strategy"]
        self._valid_query_strategies = ["random", "confidence", "margin", "entropy"]
        self._valid_modes = ["simple", "expert"]
        self._qs_list = []
        self._experiment_mode = None
        super().__init__(path)


    def sanity_checks(self):
        """
        perform specific file checks
        """
        # perform general sanity checks 
        super().general_sanity_checks()
        yaml_object = self._object

        # check for outer keys
        for key in list(yaml_object.keys()):
            if key not in self._required_fields:
                raise f"Invalid key: {key}" 

        # perform checks on the mode: either simple or expert 
        experiment_mode = self._object['mode']
        if not experiment_mode in self._valid_modes:
            raise f"Invalid mode: {experiment_mode}"
        
        self._mode = experiment_mode

        return 

    def query_strategies_sanity(self, experiment_mode, query_strategy):
        """
        query strategies formated in the yaml
        """
        if experiment_mode == "simple":
            return 
        else:   
            return 
        # expert mode

        return 

    def experiment_mode(self):
        """
        experiment mode
        """
        return self._experiment_mode




     