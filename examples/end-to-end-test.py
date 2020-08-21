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

# client.create_project('project.yml')

client.upload_class_labels("mnist_labels.json", "e34cd94ce3f711ea9a1af40f243422fe")

# client.create_experiment("experiment.yml")

# client.experiment("7d4aa73ee34611eab8f3f40f243422fe").start()