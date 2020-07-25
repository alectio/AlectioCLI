"""
Model Interface
"""
from alectio.api.base_attribute import BaseAttribute

from alectio.tools.utils import extract_id
from alectio.exceptions import ModelNotFound, ModelExceedsChanges

from pathlib import Path

import hashlib
import difflib
import re
import sys


class Model(BaseAttribute):
    def __init__(self, client, attr={}, user_id=None, id=None):
        self.client = client
        self._attr = attr
        self._id = id
        self._model_path = "" # need to get the users model path, read path from local machine 
        super().__init__(self._attr, self._id)


    def update_model(self, other): 
        """

        A user and organization has a limited amount of models to use, if a user wants to update a model, the changes
        must not exceed a certain threshold. A user must create the model object for the new model the user intends to add 
        to the list of current models. In addtion, the user needs to specify where the existing model is located based on the checksum 
        of the original model. 

        :params: other : another model to compare againse and update the existing model

        """
        # comparing the correct objects
        if not isinstance(other, Model):
            raise RuntimeError

        # check if the user has set the paths
        if len(other._model_path) == 0 or len(self._model_path) == 0:
            raise RuntimeError

        threshold = 85

        # verify the user can locate the original model
        current_checksum = self.checksum()
        original_checksum_path = self._model_path
        original_checksum = hashlib.md5(open(original_checksum_path,'rb').read()).hexdigest()
        if original_checksum != current_checksum:
            raise ModelNotFound(current_checksum)

        # read model py files as txt
        # NOTE: at the moment we do not account on filtering comments 
        with open(self._model_path) as old_model:
            old_lines = [line.rstrip().replace(" ", "") for line in old_model]

        with open(other._model_path) as updated_model:
            new_lines = [line.rstrip().replace(" ", "") for line in updated_model]
    
        # compare the contents of the files without new lines or whitespaces 
        ratio_compare = difflib.SequenceMatcher(None, old_lines, new_lines).ratio() * 100
        if ratio_compare < threshold: 
            # show the difference between the old + new
            file_difference = difflib.unified_diff(old_lines, new_lines)
            sys.stdout.writelines(file_difference)
            raise ModelExceedsChanges(ratio_compare)
        
        # need to update the new checksum, submit mutation with the following: checksum 
        other_model_path = other._model_path
        updated_file_checksum = hashlib.md5(open(other_model_path,'rb').read()).hexdigest()

        # once its gets updated, need to return the parameters back from the mutation
        # TODO: once the mutation gets created.
        return updated_file_checksum


    def checksum(self):
        """
        retreive current model checksum
        """
        return self._attr['checksum']

    @property
    def model_path(self): 
        return self._model_path

    @model_path.setter
    def model_path(self, value): 
        self._model_path = value

    
    def __repr__(self):
        return "<Model {}>".format(self._id)

   