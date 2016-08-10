from singleServices.models import *
from django import forms
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from  rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

class AwardsSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Awards
        fields = ('id_award','title','description','status', 'date', 'value','suppliers', 'items', 'contractPeriod','documents','amendment','deliveryAddressh','id_release')

class ContractsSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Contracts
        fields = ('id_contract','awardID','title','description','status','period','value','items','dateSigned','documents','amendment','implementation', 'id_release')


class PlanningSerializer(EmbeddedDocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Planning