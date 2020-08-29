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
    def __init(self, client, attr, id):
        self._client = client
        self._id = id
        self._data_uploaded = attr['dataUploaded']
        self._indices = attr['indices']
        self._data_type = attr['dataType']

    def indices(self):
        """
        return the indices to upload for the job
        """
        return self._indices

    def upload_data(self, data):
        """
        uploads the data to be labeled for a labeling partner. primarily used in sdk to automate the job process.
        :params: data - data interface to be uploaded: text_file, list of image paths, or numerical file,
        :params: data_type - text, numerical, or image
        :params: job_id - job uuid 
        """
        if not self._data_uploaded:
            print("data has been uploaded")
            return 

        # grab the data type from the job attr.
        if self._data_type == "text":
            base_class = TextDataUpload(self._client)
        elif self._data_type == "image":
            base_class = ImageDataUpload(self._client)
        elif self._data_type == "numerical":
            base_class = NumericalDataUpload(self._client)
        # upload all the data asynchronously 
        asyncio.get_event_loop().run_until_complete(base_class.upload_data(data, self._id))
        return None 