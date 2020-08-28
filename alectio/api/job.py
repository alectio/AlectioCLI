"""
LabelJob Interface 
"""

import json 
import re
import socket
import asyncio


from gql import gql

from alectio.api.base_attribute import BaseAttribute
from alectio.api.data_upload import TextDataUpload, ImageDataUpload, NumericalDataUpload


class Job(BaseAttribute):
    def __init(self, client, id):
        self._client = client
        self._id = id
        self._data_uploaded = True


    def indices(self):
        """
        return the indices to upload for the job
        """
        return []


    def upload_data(self, data, data_type):
        """
        uploads the data to be labeled for a labeling partner. primarily used in sdk to automate the job process.
        :params: data - data interface to be uploaded: text_file, list of image paths, or numerical file,
        :params: data_type - text, numerical, or image
        :params: job_id - job uuid 
        """
        base_class = None
        if not self._data_uploaded:
            return 

        if data_type == "text":
            base_class = TextDataUpload(self._client)
        elif data_type == "image":
            base_class = ImageDataUpload(self._client)
        elif data_type == "numerical":
            base_class = NumericalDataUpload(self._client)
        # upload all the data asynchronously 
        asyncio.get_event_loop().run_until_complete(base_class.upload_partner(data, self._id))
        return None 