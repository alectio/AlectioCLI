"""
classes related to data upload.
uploading is used to keep
"""
from alectio.tools.mutations import UPLOAD_PARTNER_IMAGE_MUTATION, UPLOAD_PARTNER_NUMERICAL_MUTATION, UPLOAD_PARTNER_TEXT_MUTATION
from gql import gql
import asyncio


class BaseDataUpload():
    def __init__(self, client):
        self._client = client


class NumericalDataUpload(BaseDataUpload):
    """
    upload numerical data
    """
    def __init__(self, client):
        super().__init__(client)


    async def upload_data(self, numerical_file, indices, job_id):
        # upload numerical data.
        variables = {
            'file': open(numerical_file, 'r'),
            'records': indices,
            'jobId': job_id
        }
        response = await self._client.execute(UPLOAD_PARTNER_NUMERICAL_MUTATION, variables=variables)
        print(await response.json())
        return

class ImageDataUpload(BaseDataUpload):
    """
    upload image data
    """
    def __init__(self, client):
        super().__init__(client)

    async def upload_data(self, image_path_list, indices, job_id):
        # upload all the images asynchronously ...
        variables = {
            'files': [open(i, 'rb') for i in image_path_list],
            'records': indices,
            'jobId': job_id
        }
        response = await self._client.execute(UPLOAD_PARTNER_IMAGE_MUTATION, variables=variables)
        print(await response.json())
        return None

class TextDataUpload(BaseDataUpload):
    """
    upload text data
    """
    def __init__(self, client):
        super().__init__(client)


    async def upload_data(self, text_file, indices, job_id):
        # upload text data.
        variables = {
            'file': open(text_file, 'r'),
            'records': indices,
            'jobId': job_id
        }
        response = await self._client.execute(UPLOAD_PARTNER_TEXT_MUTATION, variables=variables)
        print(await response.json())
        return None



# create jobs once all the data has been sent.
