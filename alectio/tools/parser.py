"""
Parse YAML files and perform sanity checks on the files.
"""
import yaml

from alectio.exceptions import YAMLFieldNotFound, InvalidYAMLField, InvalidYAMLFieldType


class ParseStrategyYaml():
    """
    parse strategy yaml
    """
    def __init__(self, path):
        self._path = path
        self._required_fields = ["mode", "query_strategy", "type", "resource"]
        self._valid_query_strategies = ["random", "confidence", "margin", "entropy"]
        self._valid_modes = ["simple", "expert"]
        self._valid_intervals = ["lowest", "highest"]
        self._valid_experiment_type = ["manual_al", "regular_al"]
        self._qs_list = []
        self._experiment_mode = None
        self._experiment_type = None
        self._object = self.parse_yaml(path)
        #print(self._object)
        self.sanity_checks()


    def query_strategies_sanity(self, experiment_mode, query_strategy):
        """
        query strategies formated in the yaml
        """
        qs_names = list(query_strategy.keys())
        for qs in qs_names:
            _qs = qs
            if "_" in _qs:
                _qs = _qs.split("_")[0]
            if not _qs in self._valid_query_strategies:
                raise InvalidYAMLField("qs", qs)

        # check against the mode, each mode will have a variable amount of query strats
        if experiment_mode == "simple":
            qs_name = qs_names[0]
            query_strategy_object = query_strategy[qs_name]   
            self.simple_fields_sanity(qs_name, query_strategy_object)
            print("passed simple tests")

        else:  
            print("starting expert tests")
            self.expert_fields_sanity(qs_names, query_strategy)
            print("finished expert tests")
        return 


    '''
    query_strategy:
        confidence:
            n_rec: 100
            over: 0.5
            under: 0.6
        margin:
            n_rec: 400
            over: 0.5
            under: 0.6
        confidence_1:
            n_rec: 400
            over: 0.4
            under: 0.6
    '''
    def expert_fields_sanity(self, qs_list, qs_objects):
        """
        check expert fields for:
            - uniqueness (no QS top level key can be the same)
            - valid data type
            - completeness
        """
        #check for uniqueness of qs_object key names

        if not len(set(qs_list)) == len(qs_list):
            #duplicate names exist
            print(f"make sure all your QS's under the query_strategy key have unique names, for example confidence_1, confidence_2, etc")
            return

        for qs in qs_objects:
            obj = qs_objects[qs]
            print(qs, "->", obj)

            if "random" in qs:
                if not "n_rec" in qs_objects[qs].keys():
                    print(f"n_rec must be a key of", qs)
                    return
                if not isinstance(qs_objects[qs]["n_rec"], int):
                    print(f"n_rec must be an integer, right now it is", type(qs_objects[qs]["n_rec"]))
                    return 
            else:
                # verification of n_rec
                if not "n_rec" in qs_objects[qs].keys():
                    print(f"n_rec must be a key of", qs)
                    return
                if not isinstance(qs_objects[qs]["n_rec"], int):
                    print(f"n_rec must be an integer, right now it is", type(qs_objects[qs]["n_rec"]))
                
                #verification of over
                if not "over" in qs_objects[qs].keys():
                    print(f"You need to supply the over key for {qs}")
                    return
                if not isinstance(qs_objects[qs]["over"], float):
                    print(f"over must be an float, right now it is", type(qs_objects[qs]["over"]))
                
                #verification of under
                if not "under" in qs_objects[qs].keys():
                    print(f"You need to supply the under key for {qs}")
                    return
                if not isinstance(qs_objects[qs]["over"], float):
                    print(f"over must be an float, right now it is", type(qs_objects[qs]["over"]))

                #verification that under > over

                if not qs_objects[qs]["under"] > qs_objects[qs]["over"]:
                    print(f"under key must be greater than over key for {qs}")
                    return
        
        # all sanity checks have passed, we can add the QS objects to our qs list. 
        self._qs_list.extend(qs_objects)
        return 


    def simple_fields_sanity(self, qs, qs_object):
        """
        check fields for simple qs 
        :params: qs - query strat
        :params: qs_object - query object
        """
        qs_object_keys = list(qs_object.keys())
        query_strategy_object = qs_object
        query_strategy_object['qs'] = qs

        # generic fields that apply to random and other qs 
        if not 'n_rec' in qs_object_keys:
            raise YAMLFieldNotFound("n_rec")

        # check if it is the correct type
        n_rec = qs_object['n_rec']

        if not isinstance(n_rec, int):
            raise InvalidYAMLFieldType("n_rec", int)

        query_strategy_object['nRec'] = n_rec
        del query_strategy_object['n_rec']

        if not qs == "random":
            if not 'type' in qs_object_keys:
                raise YAMLFieldNotFound("type")

            type = qs_object['type']
            if not type in self._valid_intervals:
                raise InvalidYAMLField("type", type)

            query_strategy_object['type'] = type

        # query strat fields are good, can use.   
        self._qs_list.append(query_strategy_object)

        return 

   
    def sanity_checks(self):
        """
        perform file sanity checks to make sure the data 
        """
        yaml_object = self._object
        print(yaml_object)
        # check for outer keys
        for key in list(yaml_object.keys()):
            if key == "resource":
                continue
            elif key not in self._required_fields:
                raise YAMLFieldNotFound(key)

        # perform checks on the mode: either simple or expert 
        experiment_mode = self._object['mode']
        experiment_type = self._object['type']

        if not experiment_mode in self._valid_modes:
            raise InvalidYAMLField("type", experiment_mode)
        
        if not experiment_type in self._valid_experiment_type:
            raise InvalidYAMLField("type", experiment_type)


        self._experiment_mode = experiment_mode
        self._experiment_type = experiment_type

        qs_list = self._object['query_strategy']

        self.query_strategies_sanity(experiment_mode, qs_list)

        return 


    def parse_yaml(self, path):
        """
        parse yaml file the
        :params: path - path to yaml file.
        """
        with open(path, 'r') as stream:
            data = yaml.safe_load(stream)
        return data 


    @property
    def experiment_mode(self):
        """
        experiment mode used in the yaml,
        must be the same as when the experiment was created.
        """
        return self._experiment_mode

    @property
    def qs_list(self):
        """
        list of query strategies the user intends to use 
        """
        return self._qs_list

    @property
    def experiment_type(self):
        """
        the experiment type for the yaml
        """
        return self._experiment_type

     
# if __name__ == "__main__":
#     parser = ParseStrategyYaml("../../tests/test_files/expert_multiple_strat.yaml")