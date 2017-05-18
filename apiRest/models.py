from django.db import models
from mongoengine import *
from datetime import datetime

"""Clase Period"""
class Period(EmbeddedDocument):
    startDate = DateTimeField()
    endDate = DateTimeField()

"""Clase Value """
class Value(EmbeddedDocument):
    amount = FloatField()
    currency = StringField(max_length=3)

"""Clase Unit """
class Unit(EmbeddedDocument):
     name = StringField(max_length=50)
     value = EmbeddedDocumentField(Value)

"""Clase Classification"""
class Classification(EmbeddedDocument):
     scheme = StringField(max_length=50)
     id = DictField(primary_key=True)
     description = StringField(max_length=50)
     uri = URLField()

"""Clase Item"""
class Item(EmbeddedDocument):
     id = StringField(max_length=50)
     description = StringField(max_length=50)
     classification = EmbeddedDocumentField(Classification)

"""Clase Identifier"""
class Identifier(EmbeddedDocument):
     scheme = StringField(max_length=50)
     id = StringField(max_length=50)
     legalName = StringField(max_length=50)
     uri = URLField()

"""Clase Address"""
class Address(EmbeddedDocument):
     streetAddress = StringField(max_length=50)
     locality = StringField(max_length=50)
     region = StringField(max_length=50)
     postalCode = StringField(max_length=50)
     countryName = StringField(max_length=50)

"""Clase Documents"""
class Documents(EmbeddedDocument):
     id = StringField(max_length=50)
     documentType = StringField(max_length=50)
     title = StringField(max_length=50)
     description = StringField(max_length=50)
     url = URLField()
     datePublished = DateTimeField()
     dateModified = DateTimeField()
     format = StringField(max_length=50)
     language = StringField(max_length=50)
     ocid = StringField(max_length=50)
     information_system = StringField(max_length=50)


"""Clase Organization"""
class Organization(EmbeddedDocument):
     identifier = EmbeddedDocumentField(Identifier)
     name = StringField(max_length=50)
     address = EmbeddedDocumentField(Address)

"""Clase Tender"""
class Tender(EmbeddedDocument):
     id = StringField(max_length=50)
     ocid = StringField(max_length=50)
     procurementMethod = StringField(max_length=50)
     title = StringField(max_length=50)
     description = StringField(max_length=50)
     enquiryPeriod = EmbeddedDocumentField(Period)
     value = EmbeddedDocumentField(Value)
     status = StringField(max_length=50)
     items = ListField(EmbeddedDocumentField(Item))
     submissionMethod = ListField(StringField(max_length=50))
     tenderPeriod = EmbeddedDocumentField(Period)
     documents = ListField(EmbeddedDocumentField(Documents))
     information_system = StringField(max_length=50)

     class Meta:
        indexes = [
            ("id"),
        ]

     def __str__(self):
        return 'Tender[id: {id}'.format(
            id=self.id)

"""Clase Budget"""
class Budget(EmbeddedDocument):
     source = URLField()
     id = StringField(max_length=50)
     description = StringField(max_length=50)
     amount = EmbeddedDocumentField(Value)

"""Clase Planning"""
class Planning(EmbeddedDocument):
     id = StringField(max_length=50)
     ocid = StringField(max_length=50)
     budget = EmbeddedDocumentField(Budget)
     documents = ListField(EmbeddedDocumentField(Documents))
     information_system = StringField(max_length=50)

"""Clase Award"""
class Awards(EmbeddedDocument):
     id = IntField()
     ocid = StringField(max_length=50)
     status = StringField(max_length=50)
     date = DateTimeField()
     value = EmbeddedDocumentField(Value)
     suppliers = ListField(EmbeddedDocumentField(Organization))
     items = ListField(EmbeddedDocumentField(Item))
     documents = ListField(EmbeddedDocumentField(Documents))
     information_system = StringField(max_length=50)

     class Meta:
        indexes = [
            ("id"),
        ]

"""Clase Transaction"""
class Transaction(EmbeddedDocument):
     id_transaction = StringField(max_length=50)
     source = StringField(max_length=50)
     date = DateTimeField()
     amount = EmbeddedDocumentField(Value)
     providerOrganization = EmbeddedDocumentField(Identifier)
     receiverOrganization = EmbeddedDocumentField(Identifier)
     uri = URLField()

"""Clase Contract"""
class Contracts(EmbeddedDocument):
     id = StringField(max_length=50)
     ocid = StringField(max_length=50)
     awardID = StringField(max_length=50)
     status = StringField(max_length=50)
     period = EmbeddedDocumentField(Period)
     value = EmbeddedDocumentField(Value)
     items = ListField(EmbeddedDocumentField(Item))
     dateSigned = DateTimeField()
     documents = ListField(EmbeddedDocumentField(Documents))
     information_system = StringField(max_length=50)
     
"""Clase Releases"""
class Releases(Document):
    ocid = StringField(max_length=50)
    id = StringField(max_length=50)
    uri = URLField()
    publishedDate = DateTimeField()
    language = StringField(max_length=50)
    initiationType = StringField(max_length=50)
    tag = ListField()
    date = DateTimeField()
    buyer = EmbeddedDocumentField(Organization)
    planning = EmbeddedDocumentField(Planning)
    tender = EmbeddedDocumentField(Tender)
    procurement_type = StringField(max_length=50)
    awards = ListField(EmbeddedDocumentField(Awards))
    contracts = ListField(EmbeddedDocumentField(Contracts))
    information_system = StringField(max_length=50)