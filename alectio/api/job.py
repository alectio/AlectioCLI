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
    def __init__(self, client, attr, user_id,  id):
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

    def upload_data(self, data_map):
        """
        uploads the data to be labeled for a labeling partner. primarily used in sdk to automate the job process.
        :params: data_map - data interface to be uploaded: text_file, list of image paths, or numerical file,
        example: {
            "2": path_to record,
            "5": path_to_record,
            "9": path_to_record,
        }
        keys - indices to be uploaded
        values - path to the record
        :params: data_type - text, numerical, or image
        :params: job_id - job uuid
        """
        if self._data_uploaded:
            print("data has been uploaded")
            return

        records = []
        for k,v in data_map.items():
            temp = {}
            temp['id'] = k
            temp['path'] = v
            records.append(temp)

        # grab the data type from the job attr.
        if self._data_type == "text":
            base_class = TextDataUpload(self._client)
        elif self._data_type == "image":
            base_class = ImageDataUpload(self._client)
        elif self._data_type == "numerical":
            base_class = NumericalDataUpload(self._client)
        # upload all the data asynchronously
        asyncio.get_event_loop().run_until_complete(base_class.upload_data(records, self._id))
        return None

    def __repr__(self):
        return "<Job {}>".format(self._id)
