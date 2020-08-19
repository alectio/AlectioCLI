from alectio.client import AlectioClient
from gql import gql
from gql import Client, gql
from gql.client import RetryError
from gql.transport.requests import RequestsHTTPTransport
from alectio.tools.fragments import USER_PAID_QUERY_FRAGMENT

client = AlectioClient()

project = client.project("ea15b1aedb5f11ea904cf40f243422fe") # MNIST project
for experiment in project.experiments(): # grab all the project's experiemnts 
  print(experiment)

print("--------------------")
projects = client.projects() # grab all the projects that belong to a user 
for project in projects:
  print(project)

query = gql(USER_PAID_QUERY_FRAGMENT)

params = {
    "id": "05d10fd6ba3311eaa9038aca0501223d",
}

client = Client(
            transport=RequestsHTTPTransport(
                url="http://localhost:5005/graphql",
                verify=False,
                retries=3,
            ),
            fetch_schema_from_transport=True,
        )

res = client.execute(query, params)

print(f"the result from checking if the user is paid is: {res}")