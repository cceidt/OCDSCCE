from django.db import models
from mongoengine import *

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
     id_class = DictField(primary_key=True)
     description = StringField(max_length=50)
     uri = URLField()

"""Clase Item"""
class Item(EmbeddedDocument):
     id_item = StringField(max_length=50)
     description = StringField(max_length=50)
     additionalClassifications = ListField(EmbeddedDocumentField(Classification))
     quantity = StringField(max_length=50)
     unit = EmbeddedDocumentField(Unit)
     classification = EmbeddedDocumentField(Classification)

"""Clase Identifier"""
class Identifier(EmbeddedDocument):
     scheme = StringField(max_length=50)
     id_ident = StringField(max_length=50)
     legalName = StringField(max_length=50)
     uri = URLField()

"""Clase Address"""
class Address(EmbeddedDocument):
     streetAddress = StringField(max_length=50)
     locality = StringField(max_length=50)
     region = StringField(max_length=50)
     postalCode = StringField(max_length=50)
     countryName = StringField(max_length=50)

"""Clase ContactPoint"""
class ContactPoint(EmbeddedDocument):
     name = StringField(max_length=50)
     email = StringField(max_length=50)
     telephone = StringField(max_length=50)
     faxNumber = StringField(max_length=50)
     url = URLField()

"""Clase Amendment"""
class Amendment(EmbeddedDocument):
     date = DateTimeField()
     changes = StringField(max_length=50)
     rationale = StringField(max_length=50)

"""Clase Documents"""
class Documents(EmbeddedDocument):
     id_document = DictField(primary_key=True)
     documentType = StringField(max_length=50)
     title = StringField(max_length=50)
     description = StringField(max_length=50)
     url = URLField()
     datePublished = DateTimeField()
     dateModified = DateTimeField()
     format = StringField(max_length=50)
     language = StringField(max_length=50)
     id_release = StringField(max_length=50)

"""Clase Milestone"""
class Milestone(EmbeddedDocument):
     id_milestone = DictField(primary_key=True)
     title = StringField(max_length=50)
     description = StringField(max_length=50)
     dueDate = DateTimeField()
     dateModified = DateTimeField()
     status = StringField(max_length=50)
     documents = ListField(EmbeddedDocumentField(Documents))
     id_release = StringField(max_length=50)

"""Clase Organization"""
class Organization(EmbeddedDocument):
     identifier = EmbeddedDocumentField(Identifier)
     #additionalIdentifiers = ListField(EmbeddedDocumentField(Identifier))
     name = StringField(max_length=50)
     address = EmbeddedDocumentField(Address)
     contactPoint = EmbeddedDocumentField(ContactPoint)

"""Clase Tender"""
class Tenders(EmbeddedDocument):
     ENQUIRIES_CHOICES = (
          ('0', 'Yes'),
          ('1', 'No'),
     )
     id_tender = StringField(max_length=50)
     title = StringField(max_length=50)
     description = StringField(max_length=50)
     status = StringField(max_length=50)
     items = ListField(EmbeddedDocumentField(Item))
     minValue = EmbeddedDocumentField(Value)
     value = EmbeddedDocumentField(Value)
     procurementMethod = StringField(max_length=50)
     procurementMethodRationale = StringField(max_length=50)
     awardCriteria = StringField(max_length=50)
     awardCriteriaDetails = StringField(max_length=50)
     submissionMethod = StringField(max_length=50)
     submissionMethodDetails = StringField(max_length=50)
     tenderPeriod = EmbeddedDocumentField(Period)
     enquiryPeriod = EmbeddedDocumentField(Period)
     hasEnquiries = StringField(max_length=50, choices=ENQUIRIES_CHOICES)
     eligibilityCriteria = StringField(max_length=50)
     awardPeriod = EmbeddedDocumentField(Period)
     numberOfTenderers = StringField(max_length=50)
     tenderers = ListField(EmbeddedDocumentField(Organization))
     procuringEntity = EmbeddedDocumentField(Organization)
     documents = ListField(EmbeddedDocumentField(Documents))
     milestones = ListField(EmbeddedDocumentField(Milestone))
     amendment = EmbeddedDocumentField(Amendment)
     deliveryAddressh = ListField(EmbeddedDocumentField(Address))
     id_release = StringField(max_length=50)

     class Meta:
        indexes = [
            ("id"),
        ]

     def __str__(self):
        return 'Tenders[id: {id}'.format(
            id=self.id)

"""Clase Budget"""
class Budget(EmbeddedDocument):
     source = URLField()
     id_budget = StringField(max_length=50)
     description = StringField(max_length=50)
     amount = StringField(max_length=50)
     #EmbeddedDocumentField(Value)
     #project = StringField(max_length=50)
     #id_project = StringField(max_length=50)
     uri = URLField()

"""Clase Planning"""
class Planning(EmbeddedDocument):
     budget = EmbeddedDocumentField(Budget)
     rationale = StringField(max_length=50)
     documents = ListField(EmbeddedDocumentField(Documents))
     id_release = StringField(max_length=50)

"""Clase Award"""
class Awards(EmbeddedDocument):
     id_award = IntField()
     title = StringField(max_length=50)
     description = StringField(max_length=50)
     status = StringField(max_length=50)
     date = DateTimeField()
     value = EmbeddedDocumentField(Value)
     suppliers = ListField(EmbeddedDocumentField(Organization))
     items = ListField(EmbeddedDocumentField(Item))
     contractPeriod = EmbeddedDocumentField(Period)
     documents = ListField(EmbeddedDocumentField(Documents))
     amendment = EmbeddedDocumentField(Amendment)
     deliveryAddressh = ListField(EmbeddedDocumentField(Address))
     id_release = StringField(max_length=50)

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

"""Clase Implementation"""
class Implementation(EmbeddedDocument):
     transactions = ListField(EmbeddedDocumentField(Transaction))
     documents = ListField(EmbeddedDocumentField(Documents))
     milestones = ListField(EmbeddedDocumentField(Milestone))

"""Clase Contract"""
class Contracts(EmbeddedDocument):
     id_contract = StringField(max_length=50)
     awardID = StringField(max_length=50)
     title = StringField(max_length=50)
     description = StringField(max_length=50)
     status = StringField(max_length=50)
     period = EmbeddedDocumentField(Period)
     value = EmbeddedDocumentField(Value)
     items = ListField(EmbeddedDocumentField(Item))
     dateSigned = DateTimeField()
     documents = ListField(EmbeddedDocumentField(Documents))
     amendment = EmbeddedDocumentField(Amendment)
     implementation = EmbeddedDocumentField(Implementation)
     deliveryAddressh = ListField(EmbeddedDocumentField(Address))
     id_release = StringField(max_length=50)

"""Clase Releases"""
class Releases(EmbeddedDocument):
     num_constancia = StringField(max_length=50)
     id_release = StringField(max_length=50)
     date = DateTimeField()
     tag = ListField()
     initiationType = StringField(max_length=50)
     planning = EmbeddedDocumentField(Planning)
     tender = EmbeddedDocumentField(Tenders)
     buyer = EmbeddedDocumentField(Organization)
     awards = ListField(EmbeddedDocumentField(Awards))
     contracts = ListField(EmbeddedDocumentField(Contracts))
     language = StringField(max_length=50)


"""Clase Package Metadata"""
class Packagemetadata(Document):
    uri = URLField()
    publishedDate = DateTimeField()
    releases = ListField(EmbeddedDocumentField(Releases))
    publisher = EmbeddedDocumentField(Organization)
    num_constancia = StringField(max_length=50)
    procurement_type = StringField(max_length=50)