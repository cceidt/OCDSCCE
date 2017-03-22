from singleServices.models import *
from apiRest.models import Period, Value, Item, Documents, Budget, Organization
from django import forms
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.settings import api_settings
from collections import OrderedDict


class PeriodSerializer(EmbeddedDocumentSerializer):
    startDate = serializers.DateTimeField(format=api_settings.DATETIME_FORMAT)
    endDate = serializers.DateTimeField(format=api_settings.DATETIME_FORMAT)

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = Period
        fields = ('startDate', 'endDate',)

class ValueSerializer(EmbeddedDocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = Value
        fields = ('amount', 'currency')

class TenderSerializer(EmbeddedDocumentSerializer):
    tenderPeriod = PeriodSerializer()

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = Tender
        fields = ('id','ocid','procurementMethod','title','description', 'enquiryPeriod', 'value', 'status','items','submissionMethod','tenderPeriod', 'documents')

class AwardsSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = Awards
        fields = ('id','ocid','status', 'date', 'value','suppliers', 'items','documents')

class ContractsSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = Contracts
        fields = ('id', 'ocid','awardID','status','period','value','items','dateSigned','documents')

class PlanningSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represenation

        return ret

    class Meta:
        model = Planning
        fields = ('id','ocid','budget','documents')

class BudgetSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Budget
        fields = ('source', 'id','description', 'amount')
