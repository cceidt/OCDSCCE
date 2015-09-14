from apiRest.models import *
from django import forms
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer

class TendersSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Tenders
        fields = ('id', 'id_tender','title','description','status','items','minValue','value','procurementMethod','procurementMethodRationale','awardCriteria','awardCriteriaDetails','submissionMethod','submissionMethodDetails', 'tenderPeriod', 'enquiryPeriod', 'hasEnquiries', 'eligibilityCriteria', 'awardPeriod', 'numberOfTenderers', 'tenderers', 'procuringEntity', 'documents', 'milestones', 'amendment')

class BuyerSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Organization
        fields = ('identifier','additionalIdentifiers','name','address','contactPoint')

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
        fields = ('id','awardID','title','description','status','period','value','items','dateSigned','documents','amendment','implementation', 'id_release')

class ReleasesSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Releases
        fields = ('id_release', 'date', 'tag', 'initiationType', 'planning','tender', 'buyer', 'awards', 'language')

class PlanningSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Releases
        fields = ('planning',)

class AmendmentSerializer(EmbeddedDocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Amendment
        fields = ('date', 'changes','rationale')

class MilestoneSerializer(EmbeddedDocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Milestone
        fields = ('id','title','description','dueDate','dateModified','status','documents')

class ImplementationSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Implementation
        fields = ('id', 'transactions','documents', 'milestones')