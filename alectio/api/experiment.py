from alectio.api.base_attribute import BaseAttribute

from alectio.tools.utils import extract_id


class Experiment(BaseAttribute):

    def __init__(self, client, id, attr={}):
        self.client = client
        self._attr = attr # experiment attributes
        self._id = id
        super().__init__(self._attr, self._id)
        

    def metrics(self):
        """
        return the metrics for an experiment
        """
        return 


    def start(self):
        # send request to alectio 
        return 

    def __repr__(self):
        return "<Experiment {}>".format(self._id)


 

  

