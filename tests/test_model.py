import requests 
import pytest
import os 
import logging

from alectio.client import AlectioClient
from alectio.exceptions import ModelExceedsChanges, ModelNotFound
from alectio.api.model import Model

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def original_model_paths():
    pwd = os.getcwd()
    paths = [
        f"{pwd}/test_files/vgg_16_original.py",
        f"{pwd}/test_files/vgg_16_modified.py",
        f"{pwd}/test_files/alex_net.py"
    ]
    # map over and eppend pwd
    return paths


@pytest.fixture
def alectio_client():
    os.environ['ALECTIO_API_KEY'] = "111111111111111"
    client = AlectioClient()
    return client


def test_model_update_file_slightly_over(original_model_paths, alectio_client):
    # original checksum: '6ab2100387efdcdd031f86d3f09dbfab'
    original_model_path = original_model_paths[0]
    modified_model_path = original_model_paths[1]
    
    model_id = "9990a570972811eaad5238c986352c36"

    original_model = alectio_client.model(model_id)
    # set the model paths
    original_model.model_path = original_model_path
    
    # pass in the graphql client ....
    new_model = Model(alectio_client._client)
    # set the model path fot the new model
    new_model.model_path = modified_model_path
    with pytest.raises(ModelExceedsChanges):
        original_model.update_model(new_model)
    return 

def test_model_update_file_over(original_model_paths, alectio_client):
    original_model_path = original_model_paths[0]
    modified_model_path = original_model_paths[2]
    
    model_id = "9990a570972811eaad5238c986352c36"
    original_model = alectio_client.model(model_id)
    # set the model paths
    original_model.model_path = original_model_path

    # pass in the graphql client ....
    new_model = Model(alectio_client._client)
    # set the model path fot the new model
    new_model.model_path = modified_model_path

    with pytest.raises(ModelExceedsChanges):
        original_model.update_model(new_model)
 
    return 


def test_model_not_found(original_model_paths, alectio_client):
    original_model_path = original_model_paths[1] # not the original anymore
    modified_model_path = original_model_paths[2]
    
    model_id = "9990a570972811eaad5238c986352c36"

    original_model = alectio_client.model(model_id)
    # set the model paths
    original_model.model_path = original_model_path

    # pass in the graphql client ....
    new_model = Model(alectio_client._client)
    # set the model path fot the new model
    new_model.model_path = modified_model_path

    with pytest.raises(ModelNotFound):
        original_model.update_model(new_model)
 
    return 


def test_model_path_not_set(original_model_paths, alectio_client):
    modified_model_path = original_model_paths[2]
    model_id = "9990a570972811eaad5238c986352c36"
    with pytest.raises(RuntimeError):
        original_model = alectio_client.model(model_id)
        # set the model paths
        # original_model.model_path = original_model_path
        # pass in the graphql client ....
        new_model = Model(alectio_client._client)
        # set the model path fot the new model
        new_model.model_path = modified_model_path
    
        original_model.update_model(new_model)
    return 
