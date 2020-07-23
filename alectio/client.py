import requests
import os 
import json
import asyncio

from gql import Client, gql
from aiogqlc import GraphQLClient

from gql.client import RetryError
from gql.transport.requests import RequestsHTTPTransport

from alectio.api.data_upload import TextDataUpload, ImageDataUpload, NumericalDataUpload
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

        # client to upload files, images, etc. 
        # uses https://pypi.org/project/aiogqlc/
        self._upload_client = GraphQLClient('http://localhost:5005/graphql')

        # need to retrive user_id based on token @ DEVI from OPENID 
        self._user_id = "8a90a570972811eaad5238c986352c36" # ideally this should be set already 
        # compnay id = 7774e1ca972811eaad5238c986352c36

    def projects(self):
        """
        retrieve user projects 
        :params: user_id - a uuid 
        """
        query = gql(PROJECTS_QUERY_FRAGMENT)
        params = {
            "id": str(self._user_id),
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

    def experiment(self, project_id):
        """
        retreive experiments that belong to a project
        :params: project_id - a uuid
        """
        query = gql(EXPERIMENT_QUERY_FRAGMENT)
        params = {
            "id": str(project_id),
        }
        experiment_query  = self._client.execute(query, params)['experiment'][0]
        user_experiment = Experiment(self._client, extract_id(experiment_query['pk']),  experiment_query) 
        return user_experiment

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

    def upload_data_to_partner(self, data, data_type, problem, partner, meta):
        """
        uploads the data to be labeled for a labeling partner. primarily used in sdk to automate the job process.
        :params: data - data interface to be uploaded: text_file, list of image paths, or numerical file,
        :params: data_type - text, numerical, or image
        :params: problem - object detection, image classsification, etc 
        :params: partner - name of the labeling partner alectio intends to send the traffic to.
        :params: meta - dictionary with meta information regarding data to be upload. i.e job_id, project_id, company_id, etc.
        """
        base_class = None 

        if data_type == "text":
            base_class = TextDataUpload(self._upload_client)
            return 
        elif data_type == "image":
            base_class = ImageDataUpload(self._upload_client)

        elif data_type == "numerical":
            base_class = NumericalDataUpload(self._upload_client)

        # upload all the data asynchronously 
        asyncio.get_event_loop().run_until_complete(base_class.upload_partner(data, partner, problem, meta))

        return None 

    # TODO:
    def create_project(self):
        """
        create user project 
        """
        return Project("", "", "", "")

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