import os
from gql import gql

from alectio.api.base_attribute import BaseAttribute
from alectio.tools.utils import extract_id
from alectio.tools.parser import ParseStrategyYaml
from alectio.tools.mutations import START_EXPERIMENT_MUTATION, UPLOAD_QUERY_STRATEGY_MUTATION
from alectio.tools.fragments import USER_PAID_QUERY_FRAGMENT


class Experiment(BaseAttribute):

    def __init__(self, client, attr, user_id, id):
        self._client = client
        self._attr = attr # experiment attributes
        self._name = attr['name']
        self._user_id = user_id
        self._id = id
        self._project_id = ""
        super().__init__(self._attr, self._id)
        self.set_project_id() # set experiment id based on partitition or sort key


    # TODO: start_auto ? if its auto al then you do not need to upload anything.

    def start(self):
        """
        start an experiment from the sdk
        """
        # parse yaml
        print("starting an experiment")
        query = gql(START_EXPERIMENT_MUTATION)
        params = {
            "userId": self._user_id,
            "projectId": self._project_id,
            "experimentId": self._id
        }

        res = self._client.execute(query, params)
        return

    def upload_query_strategy(self, strategy_path):
        """
        upload a qs before an experiment is run.
        if the user has created an experiment for manual al, then
        the user will have to upload a qs at every loop.
        if the user has created an experiment for regular al, then the
        user will have to upload a qs at the beginning.
        if the user is using auto al, then the user does not have to upload
        a qs.
        :params: a yaml file containing a strategy to use for the experiment.
        """

        # TODO: add assertion
        # if strategy_path is None or not os.path.exists(strategy_path):
        # # need to upload, the qs list + mode
        #     raise "Path to query strategies not found"


        #TODO: tell the user somewhere that if they have multiple of the same QS in expert mode they need to
        #distinguish the new QS with an _

        query = gql(USER_PAID_QUERY_FRAGMENT)
        params = {
            "id": self._user_id,
        }
        res = self._client.execute(query, params)

        #Check if the user is a free or paid user, before we allow them to upload a querying strategy.

        if (not res["user"][0]["isPaid"]):
            print("You must be a paid user to upload a YAML file containing your strategy")
            return


        # # parse yaml and check for any issues wihtin the file
        strategies = ParseStrategyYaml(strategy_path)

        experiment_mode = strategies.experiment_mode
        query_strategy_list = strategies.qs_list
        experiment_type = strategies.experiment_type

        print("this is my qs list")
        print(query_strategy_list)
        print("##################")
        print(experiment_type)
        # convert all n_rec cases to camel case for grqphql
        params = {
            "queryStratData": query_strategy_list,
            "projectId": self._project_id,
            "experimentId": self._id,
            "type": experiment_type,
            "mode": experiment_mode
        }

        query = gql(UPLOAD_QUERY_STRATEGY_MUTATION)
        # make sure the backend airlfow gets triggered
        message = self._client.execute(query, params)
        print(message)
        # send the information to the backend to process
        return


    def set_project_id(self):
        """
        return the project associated with the experiment id
        depending if the experiment comes from the get_collection query
        or a get_single query the experiment id can be fromn the
        sort key or primary key
        """
        pk = extract_id(self._attr['pk'])
        sk = extract_id(self._attr['sk'])
        self._project_id = pk
        if pk == self._id:
            self._project_id = sk
        return

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        # We capitalize the first letter of each component except the first one
        # with the 'title' method and join them together.
        return components[0] + ''.join(x.title() for x in components[1:])


    def __repr__(self):
        return "<Experiment {}>".format(self._name)




