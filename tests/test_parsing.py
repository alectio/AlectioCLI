import requests 
import pytest 
import os 
import logging 

from alectio.client import AlectioClient 
from alectio.exceptions import YAMLFieldNotFound, InvalidYAMLField, InvalidYAMLFieldType
from alectio.tools.parser import ParseStrategyYaml


@pytest.fixture
def original_yaml_paths():
    pwd = os.getcwd()
    paths = [
        f"{pwd}/test_files/vgg_16_original.py",
        f"{pwd}/test_files/vgg_16_modified.py",
        f"{pwd}/test_files/alex_net.py"
    ]
    # map over and eppend pwd
    return paths


def test_outer_field_not_found(original_yaml_paths):
    file = original_yaml_paths[0]
    with pytest.raises(YAMLFieldNotFound):
        # original_model.update_model(new_model)
        yaml_object = ParseStrategyYaml(file)
 
    return 

def test_outer_field_not_found(original_yaml_paths):
    file = original_yaml_paths[0]
    with pytest.raises(YAMLFieldNotFound):
        # original_model.update_model(new_model)
        yaml_object = ParseStrategyYaml(file)
 
    return 



def test_qs_field_not_found(original_yaml_paths):
    file = original_yaml_paths[0]
    with pytest.raises(InvalidYAMLField):
        # original_model.update_model(new_model)
        yaml_object = ParseStrategyYaml(file)

    return 


def test_invalid_qs_fields(original_yaml_paths):
    file = original_yaml_paths[0]
    with pytest.raises(InvalidYAMLField):
        # original_model.update_model(new_model)
        ParseStrategyYaml(file)

 
    return 


def test_invalid_type_qs_fields(original_yaml_paths):
    file = original_yaml_paths[0]
    with pytest.raises(InvalidYAMLFieldType):
        # original_model.update_model(new_model)
        ParseStrategyYaml(file)
    return 