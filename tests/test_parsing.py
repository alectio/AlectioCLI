import requests 
import pytest 
import os 
import logging 

from alectio.client import AlectioClient 

from alectio.exceptions import YAMLFieldNotFound, InvalidYAMLField