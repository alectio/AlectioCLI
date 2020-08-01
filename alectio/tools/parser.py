"""
Parse YAML files and perform sanity checks on the files.
"""
import yaml



class ParseStrategyYaml():
    """
    parse strategy yaml
    """
    def __init__(self, path):
        self._path = path
        self._required_fields = ["mode", "query_strategy", "type", "resource"]
        self._valid_query_strategies = ["random", "confidence", "margin", "entropy"]
        self._valid_modes = ["simple", "expert"]
        self._qs_list = []
        self._experiment_mode = None
        self._object = self.parse_yaml(path)
        print(self._object)
        self.sanity_checks()


    def query_strategies_sanity(self, experiment_mode, query_strategy):
        """
        query strategies formated in the yaml
        """

        # check if the list of query strategies are valid 
        # [{'confidence': ['lowest']}] simple for non random

        # edge case for random
        # if query_strategy[0]
        print("########")
        qs_names = list(query_strategy.keys())
        print(qs_names)
        for qs in qs_names:
            if not qs in self._valid_query_strategies:
                return f"Invalid query strategy {qs}"

        # check against the mode, each mode will have a variable amount of query strats
        if experiment_mode == "simple":
            qs_name = qs_names[0]
            if qs_name == "random":
                print("random qs")
                return
            else:
                return         
        else:   
            return 
        # expert mode

        return 

    
    def sanity_checks(self):
        """
        perform specific file checks
        """
        # perform general sanity checks 
        # super().general_sanity_checks()
        print("here 0")
        yaml_object = self._object
        print(yaml_object)

        # check for outer keys
        for key in list(yaml_object.keys()):
            if key == "resource":
                continue
            elif key not in self._required_fields:
                return f"Invalid key: {key}" 
        print("here 1")
        # perform checks on the mode: either simple or expert 
        experiment_mode = self._object['mode']
        if not experiment_mode in self._valid_modes:
            return f"Invalid mode: {experiment_mode}"
        print("here 10")
        self._mode = experiment_mode
        qs_list = self._object['query_strategy']
        print("this is my qs list")
        print(qs_list)

        self.query_strategies_sanity(experiment_mode, qs_list)

        return 

    def experiment_mode(self):
        """
        experiment mode used in the yaml,
        must be the same as when the experiment was created.
        """
        return self._experiment_mode


    def query_strategy_list(self):
        """
        list of query strategies the user intends to use 
        """
        return self._qs_list

    
    def parse_yaml(self, path):
        """
        parse yaml file the
        :params: path - path to yaml file.
        """
        with open(path, 'r') as stream:
            data = yaml.safe_load(stream)
        return data 



     