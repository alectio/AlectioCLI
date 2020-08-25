from alectio.client import AlectioClient
from gql import gql
from gql import Client, gql
from gql.client import RetryError
from gql.transport.requests import RequestsHTTPTransport
from alectio.tools.fragments import USER_PAID_QUERY_FRAGMENT
import os

os.environ["ALECTIO_API_KEY"] = 'xAzzL81g3A0wdhYs6AbGCfkla0o4VZab39e9WhUCOq4'
os.environ['CLIENT_SECRET'] = 'SIA0R7ENSsGDdvME2xfDD2c2Cwn8MiPuBLbIlJercFFMQ2EQ'
os.environ['CLINET_ID'] = '4mZ2yyAxJmG99KxqWp3b0xf5'

client = AlectioClient()


# create project. 
client.create_project('project.yml')

# upload class labels file
client.upload_class_labels("mnist_labels.json", "7e2dd348e64c11ea8ef8f40f243422fe")

# create experiment
client.create_experiment("experiment.yml")

# upload querying strategy for experiment
client.experiment("bfb179f6e6ff11ea8786f40f243422fe").upload_query_strategy("simple_confidence_strat.yaml")

# start the experiment. 
client.experiment("bfb179f6e6ff11ea8786f40f243422fe").start()