# AlectioCLI

The Aletio client library provides an alternative to our platform website A user is able to view experiments, projects, and other resources associated with an Alectio account. In addition, a user is able to create resources (porojets + expermients), and is able to run an experiment from the command line.


# Install Client Library 

```python
pip3 install alectio
```




## Initialize the client
```python
from alectio.client import AlectioClient
client = AlectioClient()
```

## Projects
```python
project = client.project("project_id") # grab a single project 
for experiment in project.experiments(): # grab all the project's experiemnts 
  print(experiment)
```

```python
projects = client.projects() # grab all the projects that belong to a user 
for project in projects:
    print(project)
```

## Experiments
```python
experiments = client.experiemnts("project_id") # grab all the experiments that belong to a project
```

```python
experiment = client.experiemnts("experiment_id") # grab a single experiment
```


