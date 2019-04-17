from mongoengine import StringField, Document, ReferenceField
from models.model1 import Model1


class Model2(Document):
    """
    Class represtenting the model2
    """
    model1 = ReferenceField(Model1, required=True)
    param = StringField(required=False)
    model2_id = StringField(required=True)
