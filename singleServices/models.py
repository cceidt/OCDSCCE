from django.db import models
from mongoengine import *
from datetime import datetime
from apiRest.models import Period, Value, Item, Documents, Budget, Organization

# Create your models here.
"""Clase Tender"""
class Tender(Document):
     id = StringField(max_length=50)
     ocid = StringField(max_length=50)
     procurementMethod = StringField(max_length=50)
     title = StringField(max_length=50)
     description = StringField(max_length=50)
     enquiryPeriod = EmbeddedDocumentField(Period)
     value = EmbeddedDocumentField(Value)
     status = StringField(max_length=50)
     items = ListField(EmbeddedDocumentField(Item))
     submissionMethod = StringField(max_length=50)
     tenderPeriod = EmbeddedDocumentField(Period)
     documents = ListField(EmbeddedDocumentField(Documents))

     class Meta:
        indexes = [
            ("id"),
        ]

     def __str__(self):
        return 'Tender[id: {id}'.format(
            id=self.id)

"""Clase Planning"""
class Planning(Document):
     id = StringField(max_length=50)
     ocid = StringField(max_length=50)
     budget = EmbeddedDocumentField(Budget)
     documents = ListField(EmbeddedDocumentField(Documents))

"""Clase Award"""
class Awards(Document):
     id = IntField()
     ocid = StringField(max_length=50)
     status = StringField(max_length=50)
     date = DateTimeField()
     value = EmbeddedDocumentField(Value)
     suppliers = ListField(EmbeddedDocumentField(Organization))
     items = ListField(EmbeddedDocumentField(Item))
     documents = ListField(EmbeddedDocumentField(Documents))

     class Meta:
        indexes = [
            ("id"),
        ]

"""Clase Contract"""
class Contracts(Document):
     id = StringField(max_length=50)
     ocid = StringField(max_length=50)
     awardID = StringField(max_length=50)
     status = StringField(max_length=50)
     period = EmbeddedDocumentField(Period)
     value = EmbeddedDocumentField(Value)
     items = ListField(EmbeddedDocumentField(Item))
     dateSigned = DateTimeField()
     documents = ListField(EmbeddedDocumentField(Documents))

