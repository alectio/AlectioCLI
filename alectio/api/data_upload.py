"""
classes related to data upload.
uploading is used to keep 
"""


class BaseDataUpload():
    def __init__(self, client):
        self.client = client 
        self.labeling_partners = ["daivergant", "seekncheck"]

    def labeling_partner_exists(self, partner):
        if not partner in self.labeling_partners:
            raise "labeling partner not found"

class NumericalDataUpload(BaseDataUpload):
    """
    upload numerical data
    """
    def __init__(self, client):
        self.client = client 

    def upload_partner(self, numerical_file, partner):
        
        return 


class ImageDataUpload(BaseDataUpload):
    """
    upload image data 
    """
    def __init__(self, client):
        self.client = client 

    def upload_partner(self, image_path_list, partner):
        
        return 

class TextDataUpload(BaseDataUpload):
    """
    upload text data 
    """
    def __init__(self, client):
        self.client = client 

    def upload_partner(self, text_file, partner):
        return 