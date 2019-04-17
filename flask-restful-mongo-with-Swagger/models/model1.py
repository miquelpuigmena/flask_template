from mongoengine import StringField, Document, ReferenceField, IntField, DateTimeField
from enum import Enum


class ModelReferenced1(Document):
    """
    Class to be referenced
    """
    ref_param1 = StringField(required=True)
    ref_param2 = StringField(default="Referenced second param")

class Model1(Document):
    """
    Class represtenting the model1
    """
    param1 = ReferenceField(ModelReferenced1, required=True)
    param2 = StringField(required=False)
    model1_id = StringField(required=True)
    status = IntField(required=False, default=0)
    date = DateTimeField()
