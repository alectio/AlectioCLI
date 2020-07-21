import requests
import os 
import json

from gql import Client, gql
from gql.client import RetryError
from gql.transport.requests import RequestsHTTPTransport

from alectio.api.project import Project
from alectio.api.experiment import Experiment 
from alectio.api.model import Model 

from alectio.tools.utils import extract_id
from alectio.tools.fragments import *

from alectio.exceptions import APIKeyNotFound



#TODO: all plural objects should be iterables -  A.Y 
class AlectioClient:
    def __init__(self, environ=os.environ):
        self._environ = environ 


        if 'ALECTIO_API_KEY' not in self._environ:
            raise APIKeyNotFound

        self._api_key = self._environ['ALECTIO_API_KEY']

        # cli user settings
        self._settings = {
            'git_remote': "origin",
            # 'base_url': "https://api.alectio.com"
            'base_url': "http://localhost:5005"
        }

        self._endpoint = f'{self._settings["base_url"]}/graphql'

        # user projects + experiments.
        # self._user_experiments = {}

        # graphql client
        self._client = Client(
            transport=RequestsHTTPTransport(
                url=self._endpoint,
                verify=False,
                retries=3,
            ),
            fetch_schema_from_transport=True,
        )

        # need to retrive user_id based on token @ DEVI from OPENID 
        self._user_id = "8a90a570972811eaad5238c986352c36" # ideally this should be set already 
        # compnay id = 7774e1ca972811eaad5238c986352c36

    def projects(self, user_id):
        """
        retrieve user projects 
        :params: user_id - a uuid 
        """
        query = gql(PROJECTS_QUERY_FRAGMENT)
        params = {
            "id": str(user_id),
        }
        projects_query = self._client.execute(query, params)['projects']
        user_projects = [Project(self._client, item, self._user_id, extract_id(item['sk'])) for item in projects_query]
        return user_projects
        
    def experiments(self, project_id):
        """
        retreive experiments that belong to a project
        :params: project_id - a uuid
        """
        query = gql(EXPERIMENTS_QUERY_FRAGMENT)
        params = {
            "id": str(project_id),
        }
        experiments_query  = self._client.execute(query, params)['experiments']
        project_experiments = [Experiment(self._client, extract_id(item['sk']),  item) for item in experiments_query]
        return project_experiments

    # grab user id + project id
    def project(self, project_id):
        """
        retrieve a single user project
        :params: project_id - a uuid
        """
        # also need to pass the user id 
        query = gql(PROJECT_QUERY_FRAGMENT)
        params = {
            "userId": str(self._user_id),
            "projectId": str(project_id)
        }
        project_query = self._client.execute(query, params)['project'][0]
        user_project = Project(self._client, project_query, self._user_id, project_id)
        return user_project

    def models(self, organization_id):
        """
        retrieve models associated with a user / organization.
        :params: project_id - a uuid
        """
        query = gql(MODELS_QUERY_FRAGMENT)
        params = {
            "id": str(organization_id),
        }
        models_query  = self._client.execute(query, params)['models']
        company_models = [Model(self._client, extract_id(item['sk']), item)  for item in models_query]
        return company_models

    def model(self, model_id):
        """
        retrieve a single user model
        :params: project_id - a uuid
        """
        query = gql(MODEL_QUERY_FRAGMENT)
        params = {
            "id": str(model_id),
        }
        model_query = self._client.execute(query, params)['model'][0]
        user_model = Model(self._client, model_id, model_query)
        return user_model

    # TODO:
    def create_project(self):
        """
        create user project 
        """
        return Project("", "", "")

    # TODO:
    def create_experiment(self):
        """
        create user experient
        """
        return Experiment("", "", "")

    # TODO:
    def create_model(self, model_path):
        """
        upload model checksum and verify there are enough models to check 
        :returns: model object 
        """
        return Model("", "", "")



    # class for pagination for class elements.