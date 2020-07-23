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
        self._labeling_partners = ["daivergant", "seekncheck"]

    def labeling_partner_exists(self, partner):
        """
        check if the labeling partner exists.
        :params: partner
        """
        if not partner in self._labeling_partners:
            raise "labeling partner not found"


# keep in mind we have to pass in the meta information to the backend

class NumericalDataUpload(BaseDataUpload):
    """
    upload numerical data
    """
    def __init__(self, client):
        super().__init__(client)


    async def upload_partner(self, numerical_file, partner, problem, meta={}):
        super().labeling_partner_exists(partner)
        # upload numerical data.
        variables = {
            'file': numerical_file
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

    async def upload_partner(self, image_path_list, partner, problem, meta={}):
        super().labeling_partner_exists(partner)
        # upload all the images asynchronously ... 
        variables = {
            'files': [open(i, 'rb') for i in image_path_list]
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


    async def upload_partner(self, text_file, partner, problem, meta={}):
        super().labeling_partner_exists(partner)
        # upload text data. 
        variables = {
            'file': text_file
        }
        response = await self._client.execute(UPLOAD_PARTNER_TEXT_MUTATION, variables=variables)
        print(await response.json())            
        return None 



# create jobs once all the data has been sent.