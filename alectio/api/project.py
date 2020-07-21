"""
Project Interface
"""
import json 
import re
import socket


from gql import gql

from alectio.api.base_attribute import BaseAttribute
from alectio.api.experiment import Experiment

from alectio.tools.utils import extract_id
from alectio.tools.fragments import EXPERIMENTS_QUERY_FRAGMENT
from alectio.tools.mutations import UPDATE_IP_PORT_MUTATION


class Project(BaseAttribute):
    def __init__(self, client, attr, user_id, id):
        self._client = client
        self._attr = attr # project attributes 
        self._prem_info = {}
        self._id = id
        self._user_id = user_id
        self._experiments = {}
        self.set_project_fields(self._attr)
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


    def update_ip_port(self, ip_addr, port):
        """
        update a project's ip and port 
        :params: ip_addr - ip address user intends to modify 
        :params: port - port the user intends to change
        """
        # check if the user inputted a valid ip port
        if port > 65535 or port < 0:
            assert "Must enter a valid port number 0 < port < 65535"

        try:
            socket.inet_aton(ip_addr)
            # legal
        except socket.error:
            # Not legal
            assert "Must enter a valid ip address x.x.x.x"

        query = gql(UPDATE_IP_PORT_MUTATION)
        params = {
            "userId": str(self._id),
            "projectId": str(self._id),
            "port": int(port), 
            "ip": ip_addr,
        }
        updated_port_ip_query = self._client.execute(query, params)
        print("updated query params")
        return None

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
        project_experiments = [Experiment(self._client, extract_id(item['sk']), item) for item in experiments_query]
        return project_experiments


    def set_project_fields(self, attr):
        """
        set project specific fields, if the fields exists 
        :params: project attributes 
        """
        if 'prem_info' in attr:
            self._prem_info = json.loads(attr['prem_info'])

    def __repr__(self):
        return "<Project {}>".format(self._id)
