"""
Project Interface
"""
from gql import gql

from alectio.api.base_attribute import BaseAttribute
from alectio.api.experiment import Experiment

from alectio.tools.utils import extract_id
from alectio.tools.fragments import EXPERIMENTS_QUERY_FRAGMENT

class Project(BaseAttribute):
    def __init__(self, client, attr, id):
        self._client = client
        self._attr = attr # project attributes 
        self._id = id
        self._experiments = {}
        super().__init__(self._attr, self._id)
    
    def created_experiment(self):
        # TODO: parse yaml
        return 

    def upload_classes(self):
        """
        upload class labels to the user project 
        """
        # TODO: upload class labels
        return 


    def upload_data(self):
        """
        upload data to labeling company
        """
        return

    def pending_labels(self):  
        """
        show all pending labels for a project 
        """
        return 

    def experiments(self):
        """
        retreive experiments that belong to a project
        :params: project_id - a uuid
        """
        query = gql(EXPERIMENTS_QUERY_FRAGMENT)

        params = {
            "id": str(self._id),
        }
        experiments_query  = self._client.execute(query, params)['experiments']
        #TODO: this needs to be an iterable, i.e show n records per request. - A.Y 
        project_experiments = [Experiment(self._client, extract_id(item['sk']), item) for item in experiments_query]
        return project_experiments

    def __repr__(self):
        return "<Project {}>".format(self._id)
