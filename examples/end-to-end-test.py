from alectio.client import AlectioClient
from gql import gql
from gql import Client, gql
from gql.client import RetryError
from gql.transport.requests import RequestsHTTPTransport
from alectio.tools.fragments import USER_PAID_QUERY_FRAGMENT
import os

os.environ["ALECTIO_API_KEY"] = 'xAzzL81g3A0wdhYs6AbGCfkla0o4VZab39e9WhUCOq4'
os.environ['CLIENT_SECRET'] = 'SIA0R7ENSsGDdvME2xfDD2c2Cwn8MiPuBLbIlJercFFMQ2EQ'
os.environ['CLIENT_ID'] = '4mZ2yyAxJmG99KxqWp3b0xf5'

client = AlectioClient()

# creating project
print("creating alectio project.")
project = client.create_project('./examples/project.yml')
project_id = project.id

# upload class labels file
print("uploading class labels to project.")
client.upload_class_labels("./examples/mnist_labels.json", project_id)

os.environ['ALECTIO_PROJECT_ID'] = project_id

# create experiment + pass in env variable from the created project
print("creating alectio experiment.")
experiment = client.create_experiment("./examples/experiment.yml")
experiment_id = experiment.id

print("uploading sample querying strategy.")
experiment.upload_query_strategy("./examples/simple_confidence_strat.yaml")

# start the experiment.
experiment.start()
