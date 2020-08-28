import os
from alectio.client import AlectioClient


os.environ["ALECTIO_API_KEY"] = 'xAzzL81g3A0wdhYs6AbGCfkla0o4VZab39e9WhUCOq4'
os.environ['CLIENT_SECRET'] = 'SIA0R7ENSsGDdvME2xfDD2c2Cwn8MiPuBLbIlJercFFMQ2EQ'
os.environ['CLINET_ID'] = '4mZ2yyAxJmG99KxqWp3b0xf5'

client = AlectioClient()
client.init('./client_token.json')

#client.create_experiment('/Users/devitripathy/Documents/Alectio/code/AlectioCLI/alectio/experiment.yml')