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
        self._name = attr['name']
        self._id = id
        self._user_id = user_id
        self._experiments = {}
        self.set_project_fields(self._attr)
        super().__init__(self._attr, self._id)


    def update_ip_port(self, ip_addr=None, port=None):
        """
        update a project's ip and port
        :params: ip_addr - ip address user intends to modify
        :params: port - port the user intends to change
        """
        params = {
            "userId": str(self._user_id),
            "projectId": str(self._id),
            "port": None,
            "ip": None
        }

        if ip_addr is None and port is None:
            raise "No fields were set."

        # check if the user inputed a valid port  0 .. 2^16
        if not port is None:
            if port > 65535 or port < 0:
                raise "Must enter a valid port number 0 < port < 65535."
            params['port'] = int(port)

        # check if the user inputed a valid ip addres x.x.x.x where x <- 0 .. 2^8-1
        if not ip_addr is None:
            try:
                socket.inet_aton(ip_addr)
                params['ip'] = ip_addr
            except socket.error:
                raise "Must enter a valid ip address x.x.x.x"

        query = gql(UPDATE_IP_PORT_MUTATION)
        updated_port_ip_query = self._client.execute(query, params)['updateProjectIp']['project']['onPremField']
        print(updated_port_ip_query)
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
        project_experiments = [Experiment(self._client, item, self._user_id, extract_id(item['sk'])) for item in experiments_query]
        return project_experiments


    def set_project_fields(self, attr):
        """
        set project specific fields, if the fields exists
        :params: project attributes
        """
        if 'prem_info' in attr:
            self._prem_info = json.loads(attr['prem_info'])


    def __repr__(self):
        return "<Project {}>".format(self._name)

