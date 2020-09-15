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


    async def upload_data(self, records, job_id):
        # upload numerical data.
        # TODO: review upload for numerical data
        # should upload one json ?
        variables = {
            'file': open(records, 'r'),
            'records': records,
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

    async def upload_data(self, records, job_id):
        # upload all the images asynchronously ...
        variables = {
            'files': [open(record['path'], 'rb') for record in records],
            'records': records,
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


    async def upload_data(self, records, job_id):

        # upload text data.
        variables = {
            'file': open(records, 'r'),
            'records': records,
            'jobId': job_id
        }
        response = await self._client.execute(UPLOAD_PARTNER_TEXT_MUTATION, variables=variables)
        print(await response.json())
        return None



# create jobs once all the data has been sent.
