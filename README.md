# AlectioCLI

```python
pip3 install alectio
```

```python
from alectio.client import AlectioClient
client = AlectioClient()
```

```python
from alectio.client import AlectioClient
project = client.project(project_id)
for experiment in project.experiments():
  print(experiments)
```

```python
experiment = client.experiment(experiment_id)
```

```python
projects = client.projects()
for project in projects:
    print(project)
```
